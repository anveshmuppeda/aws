# AWS Certified Cloud Practitioner

## The Deployment Models of the Cloud
### Private Cloud:
- Cloud services used by a single organization, not exposed to the public.  
- Complete control.  
- Security for sensitive applications.  
- Meet specific business needs.  
### Public Cloud:
- Cloud resources owned and operated by a thirdparty cloud service provider delivered over the Internet.    
### Hybrid Cloud:
- Keep some servers on premises and extend some capabilities to the Cloud.  
- Control over sensitive assets in your private infrastructure.  
- Flexibility and costeffectiveness of the public cloud.  

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

---

## IAM 
- **Users**: mapped to a physical user, has a password for AWS Console.  
- **Groups**: contains users only  
- **Policies**: JSON document that outlines permissions for users or groups  
- **Roles**: for EC2 instances or AWS services  
- **Security**: MFA + Password Policy  
- **AWS CLI**: manage your AWS services using the command-line  
- **AWS SDK**: manage your AWS services using a programming language  
- **Access Keys**: access AWS using the CLI or SDK  
- **Audit**: IAM Credential Reports & IAM Access Advisor  

### IAM Security Tools
- IAM Credentials Report (account-level)  
  a report that lists all your account's users and the status of their various credentials. 
- IAM Access Advisor (user-level)  
  Access advisor shows the service permissions granted to a user and when those services were last accessed. 
  You can use this information to revise your policies
 --- 
 
## EC2 Section 
- **EC2 Instance**:  AMI (OS) + Instance Size (CPU + RAM) + Storage + security groups + EC2 User Data  
- **Security Groups**: Firewall attached to the EC2 instance  
- **EC2 User Data**: Script launched at the first start of an instance   
- **SSH**: start a terminal into our EC2 Instances (port 22)  
- **EC2 Instance Role**: link to IAM roles  
- **Purchasing Options**:  On-Demand, Spot, Reserved (Standard + Convertible + Scheduled), Dedicated Host, Dedicated Instance.  


### EC2 Instances Purchasing Options
- On-Demand Instances – short workload, predictable pricing, pay by second  
- Reserved (1 & 3 years)   
  - Reserved Instances – long workloads  
  - Convertible Reserved Instances – long workloads with flexible instances   
- Savings Plans (1 & 3 years) –commitment to an amount of usage, long workload  
- Spot Instances – short workloads, cheap, can lose instances (less reliable)  
- Dedicated Hosts – book an entire physical server, control instance placement  
- Dedicated Instances – no other customers will share your hardware  
- Capacity Reservations – reserve capacity in a specific AZ for any duration  

--- 

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
    EFS works with Linux EC2 instances in multi-AZ  
- **EFS-IA**: cost-optimized storage class for infrequent accessed files  
- **FSx for Windows**: Network File System for Windows servers  
- **FSx for Lustre**: High Performance Computing Linux file system  

---

## ELB & ASG  
- High Availability vs Scalability (vertical and horizontal) vs Elasticity vs Agility in the Cloud  
- Elastic Load Balancers (ELB)  
  - Distribute traffic across backend EC2 instances, can be Multi-AZ
  - Supports health checks
  - 4 types: 
    1. Classic (old)
    2. Application (HTTP – L7)
    3. Network (TCP – L4)
    4. Gateway (L3)
- Auto Scaling Groups (ASG)  
   - Implement Elasticity for your application, across multiple AZ  
   - Scale EC2 instances based on the demand on your system, replace unhealthy.  
   - Integrated with the ELB  

---

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

### S3 Storage Classes
- Amazon S3 Standard - General Purpose  
- Amazon S3 Standard-Infrequent Access (IA)  
- Amazon S3 One Zone-Infrequent Access  
- Amazon S3 Glacier Instant Retrieval  
- Amazon S3 Glacier Flexible Retrieval  
- Amazon S3 Glacier Deep Archive  
- Amazon S3 Intelligent Tiering   
- Can move between classes manually or using S3 Lifecycle configurations  

---

## Databases & Analytics Summary in AWS  
- Relational Databases - OLTP: RDS & Aurora (SQL)  
- Differences between Multi-AZ, Read Replicas, Multi-Region  
- In-memory Database: ElastiCache  
- Key/Value Database: DynamoDB (serverless) & DAX (cache for DynamoDB)  
- Warehouse - OLAP(online analytical processing): Redshift (SQL)  
  Redshift is based on PostgreSQL, but it’s not used for OLTP, it's OLAP. Load data once every hour, not every second
- Hadoop Cluster: **EMR**(Elastic MapReduce) 
  EMR helps creating Hadoop clusters (Big Data) to analyze and process vast amount of data, The clusters can be made of hundreds of EC2 instances.   
- Athena: query data on Amazon S3 (serverless & SQL)  
  Serverless query service to analyze data stored in Amazon S3   
- QuickSight: dashboards on your data (serverless)  
- DocumentDB: “Aurora for MongoDB” (JSON – NoSQL database)  
- Amazon QLDB(Quantum Ledger Database): Financial Transactions Ledger (immutable journal, cryptographically verifiable)  
- Amazon Managed Blockchain: managed Hyperledger Fabric & Ethereum blockchains  
- Glue: Managed ETL (Extract Transform Load) and Data Catalog service  
- Database Migration: DMS(Database Migration Service)  
- Neptune: graph database  

---

## Other Compute  
- Docker: container technology to run applications  
- ECS: run Docker containers on EC2 instances  
- Fargate:  
  - Run Docker containers without provisioning the infrastructure  
  - Serverless offering (no EC2 instances)  
- ECR: Private Docker Images Repository  
- Batch: run batch jobs on AWS across managed EC2 instances  
- Lightsail: predictable & low pricing for simple application & DB stacks  
  - Great for people with little cloud experience!
  - Simpler alternative to using EC2, RDS, ELB, EBS, Route 53…

---

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

---

## AWS Elastic Beanstalk  
- Elastic Beanstalk is a developer centric view of deploying an application on AWS  
- It uses all the component’s like: EC2, ASG, ELB, RDS, etc…  
- But it’s all in one view that’s easy to make sense of!  
- We still have full control over the configuration
- Beanstalk = Platform as a Service (PaaS)  
- Beanstalk is free but you pay for the underlying instances  

---

## Deployment 
- CloudFormation: (AWS only)  
- Infrastructure as Code, works with almost all of AWS resources  
- Repeat across Regions & Accounts  
- Beanstalk: (AWS only)  
- Platform as a Service (PaaS), limited to certain programming languages or Docker  
- Deploy code consistently with a known architecture: ex, ALB + EC2 + RDS  
- CodeDeploy (hybrid): deploy & upgrade any application onto servers  
- Systems Manager (hybrid): patch, configure and run commands at scale without SSH  
- OpsWorks (hybrid): managed Chef and Puppet in AWS  

---

## Developer Services 
- CodeCommit: Store code in private git repository (version controlled)  
- CodeBuild: Build & test code in AWS  
- CodeDeploy: Deploy code onto servers  
- CodePipeline: Orchestration of pipeline (from code to build to deploy)  
  - Code => Build => Test => Provision => Deploy  
- CodeArtifact: Store software packages / dependencies on AWS  
- CodeStar: Unified view for allowing developers to do CICD and code  
  - “Quick way” to get started to correctly set-up CodeCommit, CodePipeline CodeBuild, CodeDeploy, Elastic Beanstalk, EC2, etc…   
- Cloud9: Cloud IDE (Integrated Development Environment) with collab  
- AWS CDK: Define your cloud infrastructure using a programming language  

---

## Global Applications in AWS  
- Global DNS: Route 53  
  - Great to route users to the closest deployment with least latency  
  - Great for disaster recovery strategies  
- Global Content Delivery Network (CDN): CloudFront
  - Replicate part of your application to AWS Edge Locations – decrease latency  
  - Cache common requests – improved user experience and decreased latency  
- S3 Transfer Acceleration  
  - Accelerate global uploads & downloads into Amazon S3   
- AWS Global Accelerator  
  - Improve global application availability and performance using the AWS global network   
- AWS Outposts  
  - Deploy Outposts Racks in your own Data Centers to extend AWS services
- AWS WaveLength
  - Brings AWS services to the edge of the 5G networks
  - Ultra-low latency applications
- AWS Local Zones
  - Bring AWS resources (compute, database, storage, …) closer to your users
  - Good for latency-sensitive applications

---

## Integration Section 
- SQS:
  - Queue service in AWS   
  - Multiple Producers, messages are kept up to 14 days  
  - Multiple Consumers share the read and delete messages when done  
  - Used to decouple applications in AWS
- SNS:
  - Notification service in AWS  
  - Subscribers: Email, Lambda, SQS, HTTP, Mobile…   
  - Multiple Subscribers, send all messages to all of them  
  - No message retention  
- Kinesis: real-time data streaming, persistence and analysis  
- Amazon MQ: managed message broker for ActiveMQ and RabbitMQ in the cloud (MQTT, AMQP.. protocols)  

---

## Monitoring  
- CloudWatch:  
  - Metrics: monitor the performance of AWS services and billing metrics  
  - Alarms: automate notification, perform EC2 action, notify to SNS based on metric  
  - Logs: collect log files from EC2 instances, servers, Lambda functions…  
  - Events (or EventBridge): react to events in AWS, or trigger a rule on a schedule  
- CloudTrail: audit API calls made within your AWS account  
- CloudTrail Insights: automated analysis of your CloudTrail Events  
- X-Ray: trace requests made through your distributed applications 
  - AWS X-Ray Visual analysis of our applications 
- AWS Health Dashboard: status of all AWS services across all regions  
- AWS Account Health Dashboard: AWS events that impact your infrastructure  
- Amazon CodeGuru: automated code reviews and application performance recommendations.
  - Provides two functionalities
  - CodeGuru Reviewer
  - CodeGuru Profiler  

---

## VPC  
- VPC – Virtual Private Cloud 
- Subnets – Tied to an AZ, network partition of the VPC  
- Internet Gateway – at the VPC level, provide Internet Access  
- NAT Gateway / Instances – give internet access to private subnets  
- NACL – Stateless, subnet rules for inbound and outbound   
- Security Groups – Stateful, operate at the EC2 instance level or ENI  
- VPC Peering – Connect two VPC with non overlapping IP ranges, nontransitive  
- Elastic IP –fixed public IPv4, ongoing cost if not in-use  
- VPC Endpoints – Provide private access to AWS Services within VPC  
- PrivateLink – Privately connect to a service in a 3rd party VPC  
- VPC Flow Logs – network traffic logs  
- Site to Site VPN –VPN over public internet between on-premises DC and AWS.  
- Client VPN – OpenVPN connection from your computer into your VPC.  
- Direct Connect – direct private connection to AWS.  
- Transit Gateway – Connect thousands of VPC and on-premises networks together.  

---

## Shared Responsibility on AWS  
- Shield: Automatic DDoS Protection + 24/7 support for advanced  
- WAF: Firewall to filter incoming requests based on rules   
  - AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.  
- KMS: Encryption keys managed by AWS  
- CloudHSM: Hardware encryption, we manage encryption keys  
- AWS Certificate Manager: provision, manage, and deploy SSL/TLS Certificates  
  - AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.
- Artifact: Get access to compliance reports such as PCI, ISO, etc…  
- GuardDuty: Find malicious behavior with VPC, DNS & CloudTrail Logs  
- Inspector: find software vulnerabilities in EC2, ECR Images, and Lambda functions  
- Config: Track config changes and compliance against rules  
- Macie: Find sensitive data (ex: PII data) in Amazon S3 buckets  
- CloudTrail: Track API calls made by users within account  
- AWS Security Hub: gather security findings from multiple AWS accounts  
- Amazon Detective: find the root cause of security issues or suspicious activities  
  - Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities.
- AWS Abuse: Report AWS resources used for abusive or illegal purposes  
- Root user privileges:  
  - Change account settings  
  - Close your AWS account  
  - Change or cancel your AWS Support plan   
  - Register as a seller in the Reserved Instance Marketplace  

- Penetration Testing is allowed without prior approval on 8 services. DDoS, port flooding and protocol flooding are examples of prohibited activities.
- 

----

## AWS Machine Learning   
- Rekognition: face detection, labeling, celebrity recognition  
- Transcribe: audio to text (ex: subtitles)  
- Polly: text to audio  
- Translate: translations  
- Lex: build conversational bots – chatbots  
- Connect: cloud contact center  
- Comprehend: natural language processing  
- SageMaker: machine learning for every developer and data scientist  
  - Amazon SageMaker is a fully managed service that provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly.  
- Forecast: build highly accurate forecasts  
- Kendra: ML-powered search engine  
- Personalize: real-time personalized recommendations  
  - Amazon Personalize is a machine learning service that makes it easy for developers to create individualized recommendations for customers using their applications.  
- Textract: detect text and data in documents  

---

## Account Best Practices 
- Operate multiple accounts using **Organizations**
- Use **SCP** (service control policies) to restrict account power
- Easily setup multiple accounts with best-practices with **AWS Control Tower**
- Use **Tags** & Cost Allocation Tags for easy management & billing
- IAM guidelines: MFA, least-privilege, password policy, password rotation
- **Config** to record all resources configurations & compliance over time
- **CloudFormation** to deploy stacks across accounts and regions
- **Trusted Advisor** to get insights, Support Plan adapted to your needs
- Send Service Logs and Access Logs to S3 or CloudWatch Logs
- **CloudTrail** to record API calls made within your account
- If your Account is compromised: change the root password, delete and rotate all passwords / keys, contact the AWS support
- Allow users to create pre-defined stacks defined by admins using **AWS Service Catalog**.  

---

## Billing and Costing Tools 
- **Compute Optimizer**: recommends resources’ configurations to reduce cost.  
   AWS Compute Optimizer recommends optimal AWS resources for your workloads to reduce costs and improve performance by using machine learning to analyze historical utilization metrics.  
- **Pricing Calculator**: cost of services on AWS 
    The AWS Simple Monthly Calculator is an easy-to-use online tool that enables you to estimate their architecture solution monthly cost of AWS services for your use case based on your expected usage. It is being replaced by AWS Pricing Calculator.
- **Billing Dashboard**: high level overview + free tier dashboard
- **Cost Allocation Tags**: tag resources to create detailed reports
- **Cost and Usage Reports**: most comprehensive billing dataset
- **Cost Explorer**: View current usage (detailed) and forecast usage
- **Billing Alarms**: in us-east-1 – track overall and per-service billing
- **Budgets**: more advanced – track usage, costs, RI, and get alerts
- **Savings Plans**: easy way to save based on long-term usage of AWS
- **Cost Anomaly Detection**: detect unusual spends using Machine Learning
- **Service Quotas**: notify you when you’re close to service quota threshold


- **CloudFront** pricing is different across different geographic regions.  
- The added data storage by **EBS Snapshots** are added cost in GB per month to EBS pricing. Other EBS pricing factors are: Volume type, Provisioned storage volume, IOPS, etc.  
- Compute Savings Plans provide the most flexibility and help to reduce your costs by up to 66% in exchange for a commitment to a consistent amount of usage for a 1 or 3 year term. These plans automatically apply to EC2 instance usage regardless of instance family, size, AZ, region, OS or tenancy, and also apply to Fargate or Lambda usage.  

---

## Trusted Advisor  
AWS Trusted Advisor is an online tool that provides you real time guidance to help you provision your resources following AWS best practices, including performance, security, and fault tolerance, but also cost optimization and service limits.  

• No need to install anything – high level AWS account assessment  
• Analyze your AWS accounts and provides recommendation on 5 categories  
1. Cost optimization
2. Performance
3. Security
4. Fault tolerance
5. Service limits

## Trusted Advisor – Support Plans
### 7 CORE CHECKS - Basic & Developer Support plan  
1. S3 Bucket Permissions
2. Security Groups – Specific Ports Unrestricted
3. IAM Use (one IAM user minimum)
4. MFA on Root Account
5. EBS Public Snapshots
6. RDS Public Snapshots
7. Service Limits

### FULL CHECKS - Business & Enterprise Support plan
- Full Checks available on the 5 categories
- Ability to set CloudWatch alarms when reaching limits
- Programmatic Access using AWS Support API

---

## Support plans 
1. AWS Basic Support Plan  
2. AWS Developer Support Plan 
3. AWS Business Support Plan (24/7) - is the most cost-effective option that offers 24x7 phone, email, and chat support
4. AWS Enterprise On-Ramp Support Plan (24/7)
5. AWS Enterprise Support Plan (24/7)

---

