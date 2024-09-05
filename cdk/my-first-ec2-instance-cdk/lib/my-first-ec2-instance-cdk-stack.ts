import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { MyEc2StackProps } from '../interface/cdk-app-config'; // Import the interface
import { Tags } from 'aws-cdk-lib'; // Import the Tags API

export class MyFirstEc2InstanceCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: MyEc2StackProps) {
    super(scope, id, props);

    // Retrieve the default VPC
    const defaultVpc = ec2.Vpc.fromLookup(this, 'DefaultVpc', {
      isDefault: true
    });

    // Create the EC2 instance using the instanceName from props
    const myFirstEC2Instance = new ec2.Instance(this, 'MyEC2Instance', {
      vpc: defaultVpc,
      instanceType: new ec2.InstanceType('t2.micro'),
      machineImage: ec2.MachineImage.latestAmazonLinux2(),
      instanceName: props.instanceName,  // Use the instanceName from the interface props
      keyName: props.keyName             // Use the keyName from props
    });
    // Apply tags to the EC2 instance
    if (props.tags) {
      for (const [key, value] of Object.entries(props.tags)) {
        Tags.of(myFirstEC2Instance).add(key, value);
      }
    }
  }
}
