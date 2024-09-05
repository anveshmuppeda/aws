#!/usr/bin/env node
// import 'source-map-support/register';
// import * as cdk from 'aws-cdk-lib';
// import { MyFirstEc2InstanceCdkStack } from '../lib/my-first-ec2-instance-cdk-stack';

// const app = new cdk.App();
// new MyFirstEc2InstanceCdkStack(app, 'MyFirstEc2InstanceCdkStack', {
//   /* If you don't specify 'env', this stack will be environment-agnostic.
//    * Account/Region-dependent features and context lookups will not work,
//    * but a single synthesized template can be deployed anywhere. */

//   /* Uncomment the next line to specialize this stack for the AWS Account
//    * and Region that are implied by the current CLI configuration. */
//   // env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
//   env: {
//     region: 'us-east-1',
//     account: '472901755127'
//   }
//   /* Uncomment the next line if you know exactly what Account and Region you
//    * want to deploy the stack to. */
//   // env: { account: '123456789012', region: 'us-east-1' },

//   /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
// });
import * as cdk from 'aws-cdk-lib';
import { MyFirstEc2InstanceCdkStack } from '../lib/my-first-ec2-instance-cdk-stack';
import { MyEc2StackProps } from '../interface/cdk-app-config';  // Import the interface

const app = new cdk.App();

// Get the instance name from the context defined in cdk.json
const instanceName = app.node.tryGetContext('instanceName');
const tags = app.node.tryGetContext('tags');
const keyName = app.node.tryGetContext('keyName');

// Define the props and pass instanceName from context
const stackProps: MyEc2StackProps = {
  instanceName: instanceName,
  tags: tags,
  keyName: keyName,  // Add keyName to the props
  env: {
    region: 'us-east-1',
    account: '472901755127'
  }
};

// Instantiate the stack with the provided props
new MyFirstEc2InstanceCdkStack(app, 'MyFirstEc2InstanceCdkStack', stackProps);
