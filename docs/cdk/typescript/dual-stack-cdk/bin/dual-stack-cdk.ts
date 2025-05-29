#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
// import { DualStackCdkStack } from '../lib/dual-stack-cdk-stack';
import { FirstCdkStack } from '../lib/dual-stack-cdk-stack';
import { SecondCdkStack } from '../lib/dual-stack-cdk-stack';

const app = new cdk.App();
new FirstCdkStack(app, 'FirstCdkStack', {
  env: {
    region: 'us-east-1',
    account: '472901755127'
  }
});

new SecondCdkStack(app, 'SecondCdkStack', {
  env: {
    region: 'us-east-1',
    account: '472901755127'
  }
});