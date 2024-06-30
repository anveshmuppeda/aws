import * as cdk from 'aws-cdk-lib';
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { S3 } from 'aws-cdk-lib/aws-ses-actions';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class MyFirstS3BucketCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

  const mys3bucket = new Bucket(this, 'MyFirstS3Bucket', {
    bucketName: "my-first-s3-bucket-cdk",
    versioned: true
  });
  }
}
