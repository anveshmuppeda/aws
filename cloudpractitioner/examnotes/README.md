# AWS Certified Cloud Practitioner

## The Deployment Models of the Cloud
### Private Cloud:
• Cloud services used by a single organization, not exposed to the public.  
• Complete control.  
• Security for sensitive applications.  
• Meet specific business needs.  
### Public Cloud:
• Cloud resources owned and operated by a thirdparty cloud service provider delivered over the Internet.   
• Six Advantages of Cloud Computing.   
### Hybrid Cloud:
• Keep some servers on premises and extend some capabilities to the Cloud.  
• Control over sensitive assets in your private infrastructure.  
• Flexibility and costeffectiveness of the public cloud.  

## The Five Characteristics of Cloud Computing
1. On-demand self service:  
• Users can provision resources and use them without human interaction from the service
provider    
2. Broad network access:  
• Resources available over the network, and can be accessed by diverse client platforms  
3. Multi-tenancy and resource pooling:  
• Multiple customers can share the same infrastructure and applications with security and privacy  
• Multiple customers are serviced from the same physical resources  
4. Rapid elasticity and scalability:  
• Automatically and quickly acquire and dispose resources when needed  
• Quickly and easily scale based on demand  
5. Measured service:  
• Usage is measured, users pay correctly for what they have used  

## IAM 
• **Users**: mapped to a physical user, has a password for AWS Console.  
• **Groups**: contains users only  
• **Policies**: JSON document that outlines permissions for users or groups  
• **Roles**: for EC2 instances or AWS services  
• **Security**: MFA + Password Policy  
• **AWS CLI**: manage your AWS services using the command-line  
• **AWS SDK**: manage your AWS services using a programming language  
• **Access Keys**: access AWS using the CLI or SDK  
• **Audit**: IAM Credential Reports & IAM Access Advisor  

## EC2 Section 
• **EC2 Instance**:  AMI (OS) + Instance Size (CPU + RAM) + Storage + security groups + EC2 User Data  
• **Security Groups**: Firewall attached to the EC2 instance  
• **EC2 User Data**: Script launched at the first start of an instance   
• **SSH**: start a terminal into our EC2 Instances (port 22)  
• **EC2 Instance Role**: link to IAM roles  
• **Purchasing Options**:  On-Demand, Spot, Reserved (Standard + Convertible + Scheduled), Dedicated Host, Dedicated Instance.  

### EC2 Instances Purchasing Options
• On-Demand Instances – short workload, predictable pricing, pay by second  
• Reserved (1 & 3 years)   
  • Reserved Instances – long workloads  
  • Convertible Reserved Instances – long workloads with flexible instances   
• Savings Plans (1 & 3 years) –commitment to an amount of usage, long workload  
• Spot Instances – short workloads, cheap, can lose instances (less reliable)  
• Dedicated Hosts – book an entire physical server, control instance placement  
• Dedicated Instances – no other customers will share your hardware  
• Capacity Reservations – reserve capacity in a specific AZ for any duration  


## EC2 Instance Storage  
- **EBS volumes**:  
  - network drives attached to one EC2 instance at a time  
  - Mapped to an Availability Zones  
  - Can use EBS Snapshots for backups / transferring EBS volumes across AZ  
- **AMI**: create ready-to-use EC2 instances with our customizations  
- **EC2 Image Builder**: automatically build, test and distribute AMIs  
- **EC2 Instance Store**:  
  - High performance hardware disk attached to our EC2 instance  
  - Lost if our instance is stopped / terminated  
- **EFS**: network file system, can be attached to 100s of instances in a region  
- **EFS-IA**: cost-optimized storage class for infrequent accessed files  
- **FSx for Windows**: Network File System for Windows servers  
- **FSx for Lustre**: High Performance Computing Linux file system  

## ELB & ASG  
- High Availability vs Scalability (vertical and horizontal) vs Elasticity vs Agility in the Cloud  
- Elastic Load Balancers (ELB)  
  - Distribute traffic across backend EC2 instances, can be Multi-AZ
  - Supports health checks
  - 4 types: Classic (old), Application (HTTP – L7), Network (TCP – L4), Gateway (L3)
- Auto Scaling Groups (ASG)  
   - Implement Elasticity for your application, across multiple AZ  
   - Scale EC2 instances based on the demand on your system, replace unhealthy.  
   - Integrated with the ELB  

## Amazon S3  
- Buckets vs Objects: global unique name, tied to a region  
- S3 security: IAM policy, S3 Bucket Policy (public access), S3 Encryption  
- S3 Websites: host a static website on Amazon S3  
- S3 Versioning: multiple versions for files, prevent accidental deletes  
- S3 Replication: same-region or cross-region, must enable versioning  
- S3 Storage Classes: Standard, IA, 1Z-IA, Intelligent, Glacier (Instant, Flexible, Deep)  
- Snow Family: import data onto S3 through a physical device, edge computing  
- OpsHub: desktop application to manage Snow Family devices  
- Storage Gateway: hybrid solution to extend on-premises storage to S3  


## Databases & Analytics Summary in AWS  
- Relational Databases - OLTP: RDS & Aurora (SQL)  
- Differences between Multi-AZ, Read Replicas, Multi-Region  
- In-memory Database: ElastiCache  
- Key/Value Database: DynamoDB (serverless) & DAX (cache for DynamoDB)  
- Warehouse - OLAP: Redshift (SQL)  
- Hadoop Cluster: EMR  
- Athena: query data on Amazon S3 (serverless & SQL)  
- QuickSight: dashboards on your data (serverless)  
- DocumentDB: “Aurora for MongoDB” (JSON – NoSQL database)  
- Amazon QLDB: Financial Transactions Ledger (immutable journal, cryptographically verifiable)  
- Amazon Managed Blockchain: managed Hyperledger Fabric & Ethereum blockchains  
- Glue: Managed ETL (Extract Transform Load) and Data Catalog service  
- Database Migration: DMS  
- Neptune: graph database  

## Other Compute  
- Docker: container technology to run applications  
- ECS: run Docker containers on EC2 instances  
- Fargate:  
  - Run Docker containers without provisioning the infrastructure  
  - Serverless offering (no EC2 instances)  
- ECR: Private Docker Images Repository  
- Batch: run batch jobs on AWS across managed EC2 instances  
- Lightsail: predictable & low pricing for simple application & DB stacks  


## Lambda Summary
- Lambda is Serverless, Function as a Service, seamless scaling, reactive  
- Lambda Billing:   
  - By the time run x by the RAM provisioned   
  - By the number of invocations   
- Language Support: many programming languages except (arbitrary) Docker  
- Invocation time: up to 15 minutes  
- Use cases:  
  - Create Thumbnails for images uploaded onto S3  
  - Run a Serverless cron job  
- API Gateway: expose Lambda functions as HTTP API   
