# CloudFormation: Restoring Manually Deleted Resources - Hands-On Guide

## Overview

This guide demonstrates how to restore AWS resources that were manually deleted outside of CloudFormation back into stack management. When resources are deleted manually from the AWS Console, CloudFormation loses track of them, leading to deployment errors. This hands-on tutorial uses S3 buckets as an example to show the restoration process.

## Problem Scenario

When a CloudFormation-managed resource is manually deleted:
- CloudFormation still believes the resource exists
- Subsequent deployments may succeed if there are no changes to the deleted resource
- Any modifications to the deleted resource will cause deployment failures
- The stack becomes inconsistent with actual AWS resources

## Prerequisites

- AWS CLI configured with appropriate permissions
- CloudFormation stack deployment script (`stack-creation.sh`)
- Access to AWS S3 and CloudFormation services

## Clone the Repository

```bash
git clone https://github.com/anveshmuppeda/aws.git
cd aws/cloudformationtemplates/restore-manual-deletion
```

## Step-by-Step Restoration Process

### Step 1: Initial Stack Deployment

Deploy the initial stack with three S3 buckets using `[01-s3-stack.yaml](./01-s3-stack.yaml)`:

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
      #AccessControl: Private  # Note: AccessControl commented out
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
Transform: AWS::Serverless-2016-10-31
```

**Command:**
```bash
./stack-creation.sh 01-s3-stack.yaml
```

**Expected Result:** Three S3 buckets created successfully.

### Step 2: Simulate Manual Deletion

1. Navigate to AWS S3 Console
2. Manually delete `anvesh-muppeda-demo-bucket2`
3. Verify the bucket is removed from AWS but still exists in CloudFormation template

### Step 3: Test Deployment Without Changes

Deploy the same stack again using `01-s3-stack.yaml`:

```bash
./stack-creation.sh 01-s3-stack.yaml
```

**Expected Result:** Deployment succeeds because CloudFormation detects no changes and doesn't attempt to modify the deleted resource.

### Step 4: Trigger the Error

Attempt to modify the deleted resource by adding the `AccessControl` property back to `DemoBucket2` in `[02-s3-stack.yaml](./02-s3-stack.yaml)`:

```yaml
# Key change: AccessControl property added to DemoBucket2
DemoBucket2:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: anvesh-muppeda-demo-bucket2
    AccessControl: Private  # This line was uncommented
```

**Command:**
```bash
./stack-creation.sh 02-s3-stack.yaml
```

**Expected Error:**
```
Resource handler returned message: "The specified bucket does not exist 
(Service: S3, Status Code: 404, Request ID: 85TGA9Z2PVKFD2FT, 
Extended Request ID: GTaJonyOgUrNIazo7JfTplWOkR9WZcnDPuz6nBF6VzRKsWR0+T2b91guLjOWWjOKQtXinnhuuzP3H9eyFBL73nHk01B8JMZi) 
(SDK Attempt Count: 1)" (RequestToken: c457c24d-197a-f0bd-ed70-0ddbae623362, 
HandlerErrorCode: NotFound)
```

### Step 5: Restoration Solution - Rename Strategy

Use `[03-s3-stack.yaml](./03-s3-stack.yaml)` to temporarily rename the deleted resource:

```yaml
# Key change: Bucket name changed from anvesh-muppeda-demo-bucket2 to anvesh-muppeda-demo-bucket4
DemoBucket2:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: anvesh-muppeda-demo-bucket4  # Temporary new name
    AccessControl: Private
```

**Command:**
```bash
./stack-creation.sh 03-s3-stack.yaml
```

**Expected Result:** New bucket `anvesh-muppeda-demo-bucket4` created successfully.

### Step 6: Restore Original Name

Use `[04-s3-stack.yaml](./04-s3-stack.yaml)` to restore the original bucket name:

```yaml
# Final change: Bucket name restored to original anvesh-muppeda-demo-bucket2
DemoBucket2:
  Type: AWS::S3::Bucket
  Properties:
    BucketName: anvesh-muppeda-demo-bucket2  # Original name restored
    AccessControl: Private
```

**Command:**
```bash
./stack-creation.sh 04-s3-stack.yaml
```

**Expected Result:** 
- `anvesh-muppeda-demo-bucket4` is deleted
- `anvesh-muppeda-demo-bucket2` is recreated
- Stack is fully restored with all original resource names

## Key Concepts Explained

### Why This Works

1. **CloudFormation State Management**: CloudFormation maintains its own state separate from AWS resources
2. **Resource Replacement**: When you change a resource's name or key properties, CloudFormation replaces the resource
3. **Two-Step Process**: The temporary rename forces CloudFormation to create a new resource, then renaming back completes the restoration

### Important Considerations

- **Data Loss**: This process will recreate the resource, losing any data that was in the original bucket
- **Dependencies**: Consider any resources that depend on the deleted resource
- **Permissions**: Ensure your CloudFormation execution role has permissions to create/delete the resources
- **Naming Conflicts**: Ensure temporary names don't conflict with existing resources

## Alternative Approaches

### 1. Import Existing Resources
If the resource still exists but CloudFormation lost track:
```bash
aws cloudformation create-change-set --stack-name <stack-name> \
  --change-set-name import-change-set \
  --change-set-type IMPORT \
  --resources-to-import file://resources-to-import.json \
  --template-body file://template.yaml
```

### 2. Stack Drift Detection
Check for drift before making changes:
```bash
aws cloudformation detect-stack-drift --stack-name <stack-name>
aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id <detection-id>
```

### 3. Remove from Stack
If restoration isn't needed, remove the resource from the template entirely.

## Best Practices

1. **Regular Drift Detection**: Periodically check for stack drift
2. **Resource Tagging**: Tag all CloudFormation resources for easier identification
3. **Access Controls**: Limit manual access to CloudFormation-managed resources
4. **Backup Strategy**: Implement proper backup procedures for critical resources
5. **Change Management**: Use proper change management processes to avoid manual deletions

## Troubleshooting

### Common Issues

**Issue**: "Resource already exists" error during restoration
**Solution**: Use a temporary name first, then rename back

**Issue**: Dependencies prevent resource deletion
**Solution**: Identify and temporarily modify dependent resources

**Issue**: IAM permissions errors
**Solution**: Ensure CloudFormation role has necessary permissions for create/delete operations

## Sample Shell Script

```bash
#!/bin/bash
# stack-creation.sh
STACK_NAME="s3-demo-stack"
TEMPLATE_FILE=$1

if [ -z "$1" ]; then
    echo "Usage: $0 <template-file>"
    exit 1
fi

echo "Deploying stack: $STACK_NAME with template: $TEMPLATE_FILE"

aws cloudformation deploy \
    --template-file "$TEMPLATE_FILE" \
    --stack-name "$STACK_NAME" \
    --capabilities CAPABILITY_IAM \
    --no-fail-on-empty-changeset

echo "Deployment complete!"
```

## Conclusion

This hands-on guide demonstrates a practical approach to restoring manually deleted CloudFormation resources. The key insight is using resource replacement through naming changes to force CloudFormation to recreate the resource under management. While this approach works well for stateless resources like S3 buckets, careful consideration is needed for resources with persistent data or complex dependencies.

Remember that prevention is better than restoration - implement proper access controls and change management processes to minimize the risk of manual resource deletions in the first place.