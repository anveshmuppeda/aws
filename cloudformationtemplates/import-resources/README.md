# Importing Existing AWS Resources into CloudFormation Templates

This guide demonstrates how to import existing AWS resources (specifically S3 buckets) into a CloudFormation stack using the CloudFormation Import feature.

## Overview

We'll walk through the process of creating initial resources with CloudFormation, manually creating an additional resource outside of the stack, and then importing that external resource back into CloudFormation management.

## Step-by-Step Instructions

### Step 1: Deploy the Initial CloudFormation Stack

1. Create and deploy the initial CloudFormation stack using the template [01-original-stack.yaml](./01-original-stack.yaml)
2. This will provision two S3 buckets (`anvesh-muppeda-demo-bucket1` and `anvesh-muppeda-demo-bucket2`) under CloudFormation management
3. Verify the stack deployment is successful and both buckets are created

### Step 2: Create an Additional Resource Manually

1. Navigate to the AWS Management Console
2. Go to the S3 service
3. Manually create a new S3 bucket named `anvesh-muppeda-demo-bucket3`
4. Configure the bucket with private access control to match the existing buckets
5. Note that this bucket now exists outside of CloudFormation management

### Step 3: Update the CloudFormation Template

1. Modify your CloudFormation template to include the manually created resource
2. Use the updated template [02-imported-stack.yaml](./02-imported-stack.yaml) which includes:
   - All existing resources (DemoBucket1 and DemoBucket2)
   - The new resource definition for DemoBucket3
   - Updated outputs section to include the new bucket

### Step 4: Import the Existing Resource

1. In the AWS CloudFormation console, locate your existing stack
2. Select the "Stack actions" dropdown menu
3. Choose "Import resources into stack"
4. Upload the [02-imported-stack.yaml](./02-imported-stack.yaml) template
5. Map the existing `anvesh-muppeda-demo-bucket3` resource to the `DemoBucket3` resource in your template
6. Complete the import process by following the wizard prompts
7. Verify that the import was successful and all three buckets are now managed by the CloudFormation stack

## Template Files

### [01-imported-stack.yaml](./01-imported-stack.yaml)
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Demo S3 Buckets CloudFormation Stack
Resources:
  DemoBucket1:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: anvesh-muppeda-demo-bucket1
      AccessControl: Private
  DemoBucket2:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: anvesh-muppeda-demo-bucket2
      AccessControl: Private
Outputs:
  BucketName1:
    Description: Name of the demo S3 bucket 1
    Value: !Ref DemoBucket1
  BucketName2:
    Description: Name of the demo S3 bucket 2
    Value: !Ref DemoBucket2
```

### [02-imported-stack.yaml](./02-imported-stack.yaml)
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Demo S3 Buckets CloudFormation Stack
Resources:
  DemoBucket1:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: anvesh-muppeda-demo-bucket1
      AccessControl: Private
  DemoBucket2:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: anvesh-muppeda-demo-bucket2
      AccessControl: Private
  DemoBucket3:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: anvesh-muppeda-demo-bucket3
      AccessControl: Private
Outputs:
  BucketName1:
    Description: Name of the demo S3 bucket 1
    Value: !Ref DemoBucket1
  BucketName2:
    Description: Name of the demo S3 bucket 2
    Value: !Ref DemoBucket2
  BucketName3:
    Description: Name of the demo S3 bucket 3
    Value: !Ref DemoBucket3
```

## Key Points

- The import process allows you to bring existing AWS resources under CloudFormation management without recreating them
- Ensure the resource properties in your template match the actual configuration of the existing resource
- The import operation is non-destructive - it doesn't modify the existing resource, only brings it under CloudFormation control
- After import, the resource can be managed through CloudFormation updates and will be deleted when the stack is deleted

## Verification

After completing the import process, verify that:
- All three buckets appear in the CloudFormation stack resources
- The stack outputs show all three bucket names
- You can update and manage all resources through CloudFormation