# Day 5  
## VPC  

### Create VPC
Name: MyVPC
IPV4 CIDR: 10.0.0.0/16


### Create Subnets  
Name: Public-1A
AZ: us-east-2a
IPV4 CIDR: 10.0.1.0/24

Name: Private-1A
AZ: us-east-2a
IPV4 CIDR: 10.0.2.0/24

Name: Public-2A
AZ: us-east-2b
IPV4 CIDR: 10.0.3.0/24

Name: Private-2A
AZ: us-east-2b
IPV4 CIDR: 10.0.4.0/24

### Enable Public IP
Enable Auto Assign Public IP to the public subnets 

### Create Internet Gateway
Name: MyIGW
VPC: MyVPC

### Attach IGW to RT
Add Internet Gateway in main route table on 0.0.0.0/0  

### Create a Private Route Table  
Name: Private-RT  
VPC: MyVPC

### Associate the subnets to PRT  
Associate Private Subnets to the Private Route Table  
Subnets: Private-1A, Private-2A  

### Create NatGW 
Name: MyNatGW
Subnet: Public-1A
Allocate EIP 

### Update Private RT 
Add the above NatGW to the Private route table on 0.0.0.0/0

### CIDR Calculator
