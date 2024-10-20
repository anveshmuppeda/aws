import * as cdk from 'aws-cdk-lib';
import { Template } from '@aws-cdk/assertions';
import { JestTestExampleCdkStack } from '../lib/jest-test-example-cdk-stack'; // Adjust the path if needed

test('Stack creates a VPC with expected properties', () => {
  // Create an instance of the stack
  const app = new cdk.App();
  const stack = new JestTestExampleCdkStack(app, 'TestStack');
  
  // Create a Template from the stack
  const template = Template.fromStack(stack);

  // Test that the stack contains a VPC
  template.hasResourceProperties('AWS::EC2::VPC', {
    CidrBlock: '10.0.0.0/16',
    EnableDnsSupport: true,
    EnableDnsHostnames: true,
  });

  // Test that the stack contains a security group
  template.hasResourceProperties('AWS::EC2::SecurityGroup', {
    GroupDescription: 'Web-Server-SG',
    SecurityGroupIngress: [
      {
        CidrIp: '0.0.0.0/0',
        FromPort: 22,
        ToPort: 22,
        IpProtocol: 'tcp',
      },
      {
        CidrIp: '0.0.0.0/0',
        FromPort: 80,
        ToPort: 80,
        IpProtocol: 'tcp',
      },
      {
        CidrIp: '0.0.0.0/0',
        FromPort: 443,
        ToPort: 443,
        IpProtocol: 'tcp',
      },
    ],
  });

  // Test that the stack contains an EC2 instance with the expected properties
  template.hasResourceProperties('AWS::EC2::Instance', {
    InstanceType: 't2.micro',
    KeyName: 'us-east-1',
    ImageId: {
      'Fn::FindInMap': [
        'AWSCloudFormation-Hardware-architecture',
        'AmazonLinux2',
        'Id',
      ],
    },
    SecurityGroupIds: [
      {
        Ref: 'web-server-sg',
      },
    ],
    SubnetId: {
      'Fn::Select': [
        0,
        {
          'Fn::GetAtt': [
            'WebAppVpc',
            'PublicSubnetIds',
          ],
        },
      ],
    },
  });
});
