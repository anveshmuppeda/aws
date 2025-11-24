# Hands-On Guide: Implementing VPC Flow Logs with AWS CDK (Python)

## Introduction

VPC Flow Logs is a powerful feature in AWS that captures information about IP traffic going to and from network interfaces in your VPC. This data is crucial for network monitoring, security analysis, and troubleshooting connectivity issues.

In this hands-on guide, we'll build a complete VPC infrastructure with Flow Logs enabled using AWS CDK with Python. By the end of this tutorial, you'll have a working demo environment that captures and logs all network traffic to CloudWatch Logs.

## What You'll Build

- A custom VPC with public and private subnets
- Internet Gateway for public internet access
- Route tables with proper associations
- Security groups for EC2 instances
- EC2 instances in both public and private subnets
- **VPC Flow Logs streaming to CloudWatch Logs**

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    VPC (10.10.0.0/16)                   │
│                                                         │
│  ┌─────────────────────┐  ┌────────────────────────┐  │
│  │  Public Subnet      │  │  Private Subnet        │  │
│  │  (10.10.0.0/24)     │  │  (10.10.10.0/24)       │  │
│  │                     │  │                        │  │
│  │  ┌──────────────┐   │  │  ┌──────────────┐     │  │
│  │  │ EC2 Instance │   │  │  │ EC2 Instance │     │  │
│  │  │  (Public)    │   │  │  │  (Private)   │     │  │
│  │  └──────────────┘   │  │  └──────────────┘     │  │
│  └─────────────────────┘  └────────────────────────┘  │
│           │                                            │
│           │ Internet Gateway                           │
│           ▼                                            │
│      ┌─────────┐                                      │
│      │   IGW   │                                      │
│      └─────────┘                                      │
│                                                         │
│  VPC Flow Logs ──────────────────────────────────────► │
└───────────────────────────────────────────────────────┘
                                                    │
                                                    ▼
                                        ┌─────────────────────┐
                                        │  CloudWatch Logs    │
                                        │  Log Group          │
                                        └─────────────────────┘
```

## Prerequisites

Before we begin, ensure you have:

1. **AWS Account** with appropriate permissions
2. **AWS CLI** installed and configured
3. **Python 3.7+** installed
4. **Node.js** (for AWS CDK CLI)
5. **AWS CDK** installed globally
6. **Git** installed
7. An **EC2 Key Pair** named "demo" (or update the code with your key pair name)

## Step 1: Install AWS CDK

If you haven't already installed AWS CDK, run:

```bash
npm install -g aws-cdk
```

Verify the installation:

```bash
cdk --version
```

## Step 2: Clone the Repository

Clone the repository containing the code:

```bash
git clone https://github.com/anveshmuppeda/aws.git
cd aws/cdk/python/vpc-flow-logs
```

## Step 3: Set Up Python Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate.bat
```

## Step 4: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```
aws-cdk-lib>=2.0.0
constructs>=10.0.0
```

## Step 5: Understanding the Code Structure

The project structure should look like this:

```
vpc-flow-logs/
├── app.py                          # CDK app entry point
├── cdk.json                        # CDK configuration
├── requirements.txt                # Python dependencies
└── vpc_flow_logs/
    ├── __init__.py
    └── vpc_flow_logs_stack.py     # Main stack definition
```

## Step 6: Create the Stack File

Create `vpc_flow_logs/vpc_flow_logs_stack.py` with the following code:

```python
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_logs as logs,
    RemovalPolicy
)


class VpcFlowLogsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        app_prefix = "vpc-flowlogs-demo"

        # Create Demo VPC
        self.demo_vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"{app_prefix}-vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[]  # We'll create subnets manually
        )

        ### VPC FLOW LOGS SETUP ###
        
        # Create CloudWatch Log Group for VPC Flow Logs
        flow_logs_log_group = logs.LogGroup(
            self,
            "VPCFlowLogsLogGroup",
            log_group_name=f"/aws/vpc/flowlogs/{app_prefix}",
            retention=logs.RetentionDays.ONE_WEEK,
            removal_policy=RemovalPolicy.DESTROY
        )
        
        # Create IAM Role for VPC Flow Logs
        flow_logs_role = iam.Role(
            self,
            "VPCFlowLogsRole",
            assumed_by=iam.ServicePrincipal("vpc-flow-logs.amazonaws.com"),
            description="Role for VPC Flow Logs to write to CloudWatch"
        )
        
        # Attach policy to allow writing to CloudWatch Logs
        flow_logs_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:DescribeLogGroups",
                    "logs:DescribeLogStreams"
                ],
                resources=[flow_logs_log_group.log_group_arn]
            )
        )
        
        # Enable VPC Flow Logs
        ec2.CfnFlowLog(
            self,
            "VPCFlowLog",
            resource_type="VPC",
            resource_id=self.demo_vpc.vpc_id,
            traffic_type="ALL",
            log_destination_type="cloud-watch-logs",
            log_destination=flow_logs_log_group.log_group_arn,
            deliver_logs_permission_arn=flow_logs_role.role_arn,
            tags=[{"key": "Name", "value": f"{app_prefix}-flow-log"}]
        )
        
        ### END VPC FLOW LOGS SETUP ###
        
        # Create Internet Gateway
        self.igw = ec2.CfnInternetGateway(
            self,
            "InternetGateway",
            tags=[{"key": "Name", "value": f"{app_prefix}-igw"}]
        )
        
        # Attach Internet Gateway to VPC
        ec2.CfnVPCGatewayAttachment(
            self,
            "IGWAttachment",
            vpc_id=self.demo_vpc.vpc_id,
            internet_gateway_id=self.igw.ref
        )

        # Get availability zones (first 1)
        azs = self.availability_zones[:1]

        # Create Public Subnets
        self.public_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PublicSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i}.0/24",
                vpc_id=self.demo_vpc.vpc_id,
                map_public_ip_on_launch=True,
                tags=[{"key": "Name", "value": f"{app_prefix}-public-subnet-{i+1}"}]
            )
            self.public_subnets.append(subnet)
        
        # Create Private Subnets
        self.private_subnets = []
        for i, az in enumerate(azs):
            subnet = ec2.CfnSubnet(
                self,
                f"PrivateSubnet{i+1}",
                availability_zone=az,
                cidr_block=f"10.10.{i+10}.0/24",
                vpc_id=self.demo_vpc.vpc_id,
                map_public_ip_on_launch=False,
                tags=[{"key": "Name", "value": f"{app_prefix}-private-subnet-{i+1}"}]
            )
            self.private_subnets.append(subnet)
        
        # Create Public Route Table
        self.public_route_table = ec2.CfnRouteTable(
            self,
            "PublicRouteTable",
            vpc_id=self.demo_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-public-rt"}]
        )
        
        # Add route to Internet Gateway
        ec2.CfnRoute(
            self,
            "PublicRoute",
            route_table_id=self.public_route_table.ref,
            destination_cidr_block="0.0.0.0/0",
            gateway_id=self.igw.ref
        )
        
        # Associate public subnets with public route table
        for i, subnet in enumerate(self.public_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PublicSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.public_route_table.ref
            )
        
        # Create Private Route Table
        self.private_route_table = ec2.CfnRouteTable(
            self,
            "PrivateRouteTable",
            vpc_id=self.demo_vpc.vpc_id,
            tags=[{"key": "Name", "value": f"{app_prefix}-private-rt"}]
        )
        
        # Associate private subnets with private route table
        for i, subnet in enumerate(self.private_subnets):
            ec2.CfnSubnetRouteTableAssociation(
                self,
                f"PrivateSubnetRTAssoc{i+1}",
                subnet_id=subnet.ref,
                route_table_id=self.private_route_table.ref
            )
        
        ### SECURITY GROUPS ###
        
        # Create Security Group for Public EC2 instances
        public_ec2_sg = ec2.SecurityGroup(
            self,
            "PublicEC2SecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-public-ec2-sg",
            description="Security group for Public EC2 instances",
            allow_all_outbound=True
        )
        
        public_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        # Create Security Group for Private EC2 instances
        private_ec2_sg = ec2.SecurityGroup(
            self,
            "PrivateEC2SecurityGroup",
            vpc=self.demo_vpc,
            security_group_name=f"{app_prefix}-private-ec2-sg",
            description="Security group for Private EC2 instances",
            allow_all_outbound=True
        )
        
        private_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH from anywhere"
        )
        
        private_ec2_sg.add_ingress_rule(
            peer=ec2.Peer.ipv4("10.20.0.0/16"),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP from Private VPC"
        )

        ### EC2 INSTANCES ###
        
        amzn_linux = ec2.MachineImage.latest_amazon_linux2023(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            cpu_type=ec2.AmazonLinuxCpuType.X86_64
        )
        
        # Create instances (one public, one private)
        ec2.CfnInstance(
            self,
            "PublicInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.public_subnets[0].ref,
            security_group_ids=[public_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{app_prefix}-public-instance"}]
        )
        
        ec2.CfnInstance(
            self,
            "PrivateInstance",
            instance_type="t2.micro",
            image_id=amzn_linux.get_image(self).image_id,
            key_name="demo",
            subnet_id=self.private_subnets[0].ref,
            security_group_ids=[private_ec2_sg.security_group_id],
            tags=[{"key": "Name", "value": f"{app_prefix}-private-instance"}]
        )
```

## Step 7: Create the App Entry Point

Create `app.py`:

```python
#!/usr/bin/env python3
import aws_cdk as cdk
from vpc_flow_logs.vpc_flow_logs_stack import VpcFlowLogsStack

app = cdk.App()
VpcFlowLogsStack(app, "VpcFlowLogsStack")

app.synth()
```

## Step 8: Initialize the __init__.py File

Create `vpc_flow_logs/__init__.py`:

```python
# Empty file or add your package-level imports
```

## Step 9: Bootstrap CDK (First Time Only)

If this is your first time using CDK in your AWS account/region, bootstrap it:

```bash
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

Replace `ACCOUNT-NUMBER` with your AWS account ID and `REGION` with your desired region (e.g., `us-east-1`).

## Step 10: Synthesize the CloudFormation Template

Generate the CloudFormation template:

```bash
cdk synth
```

This command will output the CloudFormation template to the `cdk.out` directory. Review it to ensure everything looks correct.

## Step 11: Deploy the Stack

Deploy your stack to AWS:

```bash
cdk deploy
```

You'll be prompted to approve the IAM changes. Type `y` and press Enter.

The deployment will take approximately 3-5 minutes. You'll see output showing the progress of resource creation.

## Step 12: Verify the Deployment

### Check VPC Flow Logs

1. Go to the AWS Console → **VPC** → **Your VPCs**
2. Select the VPC named `vpc-flowlogs-demo-vpc`
3. Click on the **Flow logs** tab
4. You should see a flow log with status **Active**

### Check CloudWatch Logs

1. Go to **CloudWatch** → **Log groups**
2. Find the log group `/aws/vpc/flowlogs/vpc-flowlogs-demo`
3. Click on it to view log streams
4. After a few minutes, you'll start seeing log streams with network traffic data

### Check EC2 Instances

1. Go to **EC2** → **Instances**
2. You should see two instances:
   - `vpc-flowlogs-demo-public-instance`
   - `vpc-flowlogs-demo-private-instance`

## Step 13: Generate Traffic for Testing

To generate some traffic and see it in the flow logs:

### SSH into the Public Instance

```bash
ssh -i /path/to/demo.pem ec2-user@<PUBLIC_INSTANCE_IP>
```

### Generate Some Network Traffic

```bash
# Ping Google DNS
ping -c 10 8.8.8.8

# Make HTTP requests
curl http://example.com

# Try connecting to the private instance
ping <PRIVATE_INSTANCE_IP>
```

## Step 14: View Flow Logs in CloudWatch

1. Go to **CloudWatch** → **Log groups** → `/aws/vpc/flowlogs/vpc-flowlogs-demo`
2. Click on any log stream
3. You'll see entries like:

```
2 123456789012 eni-1234567890abcdef0 203.0.113.1 10.10.0.5 443 49152 6 20 4249 1418530010 1418530070 ACCEPT OK
```

### Understanding Flow Log Fields

The default format includes:
- **version**: Flow log version
- **account-id**: AWS account ID
- **interface-id**: Network interface ID
- **srcaddr**: Source IP address
- **dstaddr**: Destination IP address
- **srcport**: Source port
- **dstport**: Destination port
- **protocol**: IANA protocol number
- **packets**: Number of packets
- **bytes**: Number of bytes
- **start**: Start time (Unix timestamp)
- **end**: End time (Unix timestamp)
- **action**: ACCEPT or REJECT
- **log-status**: Logging status (OK, NODATA, SKIPDATA)

## Step 15: Query Flow Logs with CloudWatch Insights

Use CloudWatch Logs Insights to analyze your flow logs:

1. Go to **CloudWatch** → **Logs Insights**
2. Select the log group `/aws/vpc/flowlogs/vpc-flowlogs-demo`
3. Try this query to see top talkers:

```
fields @timestamp, srcaddr, dstaddr, bytes
| filter action = "ACCEPT"
| stats sum(bytes) as totalBytes by srcaddr, dstaddr
| sort totalBytes desc
| limit 10
```

4. Click **Run query**

### More Useful Queries

**Find rejected connections:**

```
fields @timestamp, srcaddr, dstaddr, srcport, dstport, protocol
| filter action = "REJECT"
| sort @timestamp desc
| limit 20
```

**Traffic by protocol:**

```
fields @timestamp, protocol, bytes
| stats sum(bytes) as totalBytes by protocol
| sort totalBytes desc
```

**Top destination ports:**

```
fields @timestamp, dstport, bytes
| stats sum(bytes) as totalBytes by dstport
| sort totalBytes desc
| limit 10
```

## Understanding the Components

### 1. CloudWatch Log Group

```python
flow_logs_log_group = logs.LogGroup(
    self,
    "VPCFlowLogsLogGroup",
    log_group_name=f"/aws/vpc/flowlogs/{app_prefix}",
    retention=logs.RetentionDays.ONE_WEEK,
    removal_policy=RemovalPolicy.DESTROY
)
```

- **Purpose**: Stores the flow log data
- **Retention**: Set to 1 week (configurable)
- **Removal Policy**: Set to DESTROY for demo (use RETAIN in production)

### 2. IAM Role for Flow Logs

```python
flow_logs_role = iam.Role(
    self,
    "VPCFlowLogsRole",
    assumed_by=iam.ServicePrincipal("vpc-flow-logs.amazonaws.com"),
    description="Role for VPC Flow Logs to write to CloudWatch"
)
```

- **Purpose**: Allows VPC Flow Logs service to write to CloudWatch
- **Permissions**: CreateLogGroup, CreateLogStream, PutLogEvents

### 3. VPC Flow Log Configuration

```python
ec2.CfnFlowLog(
    self,
    "VPCFlowLog",
    resource_type="VPC",
    resource_id=self.demo_vpc.vpc_id,
    traffic_type="ALL",
    log_destination_type="cloud-watch-logs",
    log_destination=flow_logs_log_group.log_group_arn,
    deliver_logs_permission_arn=flow_logs_role.role_arn,
)
```

- **resource_type**: Can be VPC, Subnet, or NetworkInterface
- **traffic_type**: ALL (accepted + rejected), ACCEPT, or REJECT
- **log_destination_type**: cloud-watch-logs or s3

## Cost Considerations

### VPC Flow Logs Pricing

1. **Data Ingestion**: Charged per GB ingested into CloudWatch Logs
2. **Storage**: Charged for stored log data
3. **Data Transfer**: No additional charges for flow logs themselves

### Estimated Monthly Costs (for this demo)

- **VPC Flow Logs**: ~$0.50 - $2.00 (depending on traffic volume)
- **CloudWatch Logs**: ~$0.50 - $1.00 (for 1GB with 1-week retention)
- **EC2 Instances**: ~$15.00 for 2 t2.micro instances (744 hours/month)
- **Total**: ~$16 - $18/month

> **Note**: These are estimates. Actual costs may vary based on usage.

## Best Practices

### 1. Use Appropriate Traffic Types

```python
traffic_type="REJECT"  # Only log rejected traffic to reduce costs
```

### 2. Set Retention Policies

```python
retention=logs.RetentionDays.ONE_WEEK  # Adjust based on compliance needs
```

### 3. Filter Logs at Creation

You can use custom log formats to capture only the fields you need:

```python
log_format="${srcaddr} ${dstaddr} ${action}"
```

### 4. Use S3 for Long-Term Storage

For compliance or long-term analysis, consider storing flow logs in S3:

```python
log_destination_type="s3"
log_destination="arn:aws:s3:::my-flow-logs-bucket"
```

### 5. Enable Flow Logs on Specific Subnets

Instead of VPC-level, you can enable on specific subnets:

```python
resource_type="Subnet"
resource_id=self.public_subnets[0].ref
```

## Troubleshooting

### Issue 1: No Data in CloudWatch Logs

**Solution:**
- Wait 10-15 minutes after deployment for data to appear
- Generate traffic by SSH-ing into instances and running commands
- Check IAM role permissions

### Issue 2: Deployment Fails with Key Pair Error

**Solution:**
- Ensure you have a key pair named "demo" in your AWS account
- Or update the `key_name` parameter in the code to match your key pair

### Issue 3: EC2 Instances Not Launching

**Solution:**
- Check your AWS account limits for EC2 instances
- Ensure you have available Elastic IPs
- Verify you have permission to launch instances

### Issue 4: CDK Deploy Fails

**Solution:**
```bash
# Clear CDK cache
rm -rf cdk.out

# Re-synthesize
cdk synth

# Try deploying again
cdk deploy
```

## Cleanup

To avoid ongoing charges, destroy the stack when you're done:

```bash
cdk destroy
```

Type `y` to confirm deletion.

**Important**: This will delete:
- VPC and all associated networking resources
- EC2 instances
- CloudWatch Log Group (and all logs)
- IAM roles and policies

## Advanced Configurations

### Custom Log Format

To capture specific fields:

```python
ec2.CfnFlowLog(
    self,
    "VPCFlowLog",
    # ... other parameters ...
    log_format="${version} ${vpc-id} ${subnet-id} ${instance-id} ${interface-id} ${account-id} ${type} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${pkt-srcaddr} ${pkt-dstaddr} ${protocol} ${bytes} ${packets} ${start} ${end} ${action} ${tcp-flags} ${log-status}"
)
```

### Multiple Flow Logs

Enable flow logs for different traffic types:

```python
# Log only rejected traffic
ec2.CfnFlowLog(
    self,
    "VPCFlowLogReject",
    resource_type="VPC",
    resource_id=self.demo_vpc.vpc_id,
    traffic_type="REJECT",
    # ... other parameters ...
)

# Log only accepted traffic
ec2.CfnFlowLog(
    self,
    "VPCFlowLogAccept",
    resource_type="VPC",
    resource_id=self.demo_vpc.vpc_id,
    traffic_type="ACCEPT",
    # ... other parameters ...
)
```

### Subnet-Level Flow Logs

```python
for i, subnet in enumerate(self.public_subnets):
    ec2.CfnFlowLog(
        self,
        f"PublicSubnetFlowLog{i+1}",
        resource_type="Subnet",
        resource_id=subnet.ref,
        traffic_type="ALL",
        # ... other parameters ...
    )
```

## Use Cases

### 1. Security Analysis

- Detect unauthorized access attempts
- Identify suspicious traffic patterns
- Monitor for data exfiltration

### 2. Network Troubleshooting

- Debug connectivity issues
- Analyze traffic patterns
- Identify bandwidth bottlenecks

### 3. Compliance and Auditing

- Meet regulatory requirements
- Maintain audit trails
- Generate compliance reports

### 4. Cost Optimization

- Identify unused resources
- Analyze data transfer costs
- Optimize network architecture

## Integration with Other AWS Services

### VPC Flow Logs + AWS Security Hub

Flow logs can feed into Security Hub for centralized security monitoring.

### VPC Flow Logs + Amazon Athena

Query flow logs stored in S3 using SQL:

```sql
SELECT srcaddr, dstaddr, bytes 
FROM vpc_flow_logs 
WHERE action = 'REJECT' 
ORDER BY bytes DESC 
LIMIT 10;
```

### VPC Flow Logs + AWS Lambda

Trigger Lambda functions based on flow log patterns for automated responses.

## Conclusion

You've successfully implemented VPC Flow Logs using AWS CDK! You now have:

✅ A fully functional VPC with public and private subnets  
✅ VPC Flow Logs capturing all network traffic  
✅ CloudWatch Logs storing flow log data  
✅ EC2 instances for testing and generating traffic  
✅ Knowledge of how to query and analyze flow logs  

## Next Steps

1. **Explore Advanced Queries**: Experiment with CloudWatch Logs Insights
2. **Set Up Alarms**: Create CloudWatch alarms for suspicious traffic
3. **Automate Analysis**: Build Lambda functions to process flow logs
4. **Optimize Costs**: Fine-tune log retention and filters
5. **Integrate with SIEM**: Connect flow logs to your security tools

## About the Author

Feel free to connect with me for more AWS and DevOps content!

---

**Found this helpful? Please give it a ⭐ on GitHub and share with your network!**

**Questions or feedback? Leave a comment below!**

