import * as cdk from 'aws-cdk-lib';

// Define your custom interface for stack props here
export interface MyEc2StackProps extends cdk.StackProps {
  instanceName: string;
  tags?: { [key: string]: string }; // Optional tags object
  keyName?: string;  // Optional keyName for the EC2 instance
}
