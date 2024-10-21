# AWS CDK With Python  

### First bootstrap the environment:  
```console
cdk bootstrap 463470985368/us-east-1
```  

### Initialize the first python cdk app  

#### Empty App  
```console
cdk init app -l python
```  
#### Sample App  
```console
cdk init sample-app --language python
```  

## Types of Constructs in AWS CDK  

In AWS CDK (Cloud Development Kit), constructs are the basic building blocks used to model and define AWS infrastructure in code. Constructs represent AWS resources and higher-level abstractions of your cloud architecture. These constructs are then synthesized into AWS CloudFormation templates, which deploy the resources to your AWS environment.

### 1. **L1 Construct (CloudFormation-level construct)**

- **L1 constructs** are direct, low-level mappings to AWS CloudFormation resources. They give you full control over every aspect of the resource, but that means you have to manually configure every detail.
- These constructs start with `Cfn` (e.g., `CfnBucket` for an S3 bucket) and are essentially one-to-one representations of CloudFormation resources.
  
Here's how you’d create an S3 bucket using an **L1 construct**:

#### Example (L1 - CfnBucket):
```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class MyFirstCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Create an S3 bucket using an L1 construct (CfnBucket)
    new s3.CfnBucket(this, 'MyL1Bucket', {
      bucketName: 'my-l1-bucket',  // You need to manually specify bucket properties
      versioningConfiguration: {   // Manually configure versioning
        status: 'Enabled',
      },
    });
  }
}
```

#### Explanation:
- **`s3.CfnBucket`**: This is the **L1 construct**. You have to define every property manually, like the bucket name, versioning status, etc.
- You get full control, but you’re essentially working at the CloudFormation level.

### 2. **L2 Construct (Simplified, high-level abstraction)**

This was already covered in the first example (`s3.Bucket`). You get higher-level defaults, and you don’t need to worry about the nitty-gritty details. Let’s briefly revisit:

#### Example (L2 - Bucket):
```typescript
new s3.Bucket(this, 'MyL2Bucket', {
  versioned: true,  // High-level configuration, simple and clean
});
```

### 3. **L3 Construct (Patterns)**

- **L3 constructs** go beyond single resources and combine multiple resources into common architectural patterns. These are very high-level constructs that abstract entire workflows or solutions.
- They are often called **patterns** because they encapsulate multiple resources in ways that are commonly used together. For example, an L3 construct might create an S3 bucket **along with** a CloudFront distribution for serving static website content.

Let’s look at an example where an L3 construct sets up an S3 bucket **with additional services** like a CloudFront distribution (for caching) and an S3 bucket policy (for public access):

#### Example (L3 - StaticSite):
```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';

export class MyFirstCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // Create an S3 bucket to hold website files
    const myBucket = new s3.Bucket(this, 'MyWebsiteBucket', {
      websiteIndexDocument: 'index.html',  // Treats it as a website bucket
      publicReadAccess: true,              // Makes it publicly accessible
    });

    // Create a CloudFront distribution (CDN) for the bucket
    const distribution = new cloudfront.CloudFrontWebDistribution(this, 'MyCDN', {
      originConfigs: [
        {
          s3OriginSource: {
            s3BucketSource: myBucket,
          },
          behaviors: [{ isDefaultBehavior: true }],
        },
      ],
    });

    // Deploy files from local machine to the S3 bucket
    new s3deploy.BucketDeployment(this, 'DeployWebsite', {
      sources: [s3deploy.Source.asset('./website-content')], // Path to local content
      destinationBucket: myBucket,
      distribution,   // Invalidate the CloudFront cache after deployment
      distributionPaths: ['/*'],
    });
  }
}
```

#### Explanation:
- This **L3 construct** (pattern) sets up a **static website** using an S3 bucket, a CloudFront distribution for content delivery, and a deployment step to upload files to the bucket.
- It abstracts multiple AWS services into a single construct pattern (S3 + CloudFront + Deployment).
- The whole point of **L3 constructs** is that you don’t need to deal with each individual AWS service. You get a full solution with just a few lines of code!

### Comparison Summary

| **Construct Level** | **What It Represents**                          | **Example in CDK**                          |
|---------------------|--------------------------------------------------|---------------------------------------------|
| **L1**              | CloudFormation resource, lowest level of control | `s3.CfnBucket`                              |
| **L2**              | High-level resource with sensible defaults       | `s3.Bucket`                                 |
| **L3**              | Architectural pattern, combining multiple resources | S3 bucket + CloudFront + Deployment (a website pattern) |

### Key Takeaways:

1. **L1 Constructs** are detailed, low-level representations directly mapped to CloudFormation resources. You need to configure everything manually.
2. **L2 Constructs** abstract away some of the complexity, giving you sensible defaults and an easier interface.
3. **L3 Constructs** (patterns) combine multiple AWS services into ready-to-use solutions that represent common patterns, such as a static website or serverless application.

In short:
- Use **L1** if you need full control and fine-tuned customization.
- Use **L2** for most cases where you need individual resources but prefer easier-to-use interfaces.
- Use **L3** for common architectural patterns that bundle multiple services together into a single, reusable construct.

Does this help clarify the differences between L1, L2, and L3 constructs?


## Reference  
https://docs.aws.amazon.com/cdk/api/v2/python/  
