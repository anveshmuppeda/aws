import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { readFile, readFileSync } from 'fs';

export class FirstCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Configure Userdata for webserver
    const userDataScript = readFileSync('./src/first-userdata.sh', 'utf8');

    // Retrieve the default VPC
    const defaultVpc = ec2.Vpc.fromLookup(this, 'DefaultVpc', {
      isDefault: true
    });

    const firstStackWebServer = new ec2.Instance(this, 'MyEC2Instance', {
      vpc: defaultVpc,
      instanceType: new ec2.InstanceType('t2.micro'),
      machineImage: ec2.MachineImage.latestAmazonLinux2(),
      keyName: 'us-east-1',
      instanceName: "firstStackWebServer"
    });

    // Add the userdata script to EC2 instance
    firstStackWebServer.addUserData(userDataScript);

  }
}


export class SecondCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Configure Userdata for webserver
    const userDataScript = readFileSync('./src/second-userdata.sh', 'utf8');

    // Retrieve the default VPC
    const defaultVpc = ec2.Vpc.fromLookup(this, 'DefaultVpc', {
      isDefault: true
    });

    const secondStackWebServer = new ec2.Instance(this, 'MyEC2Instance', {
      vpc: defaultVpc,
      instanceType: new ec2.InstanceType('t2.micro'),
      machineImage: ec2.MachineImage.latestAmazonLinux2(),
      keyName: 'us-east-1',
      instanceName: "secondStackWebServer"
    });

    // Add the userdata script to EC2 instance
    secondStackWebServer.addUserData(userDataScript);

  }
}
