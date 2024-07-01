import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import { readFile, readFileSync } from 'fs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class WebAppNetworkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpcCidr = '10.0.0.0/16';

    // Configure Userdata for webserver
    const userDataScript = readFileSync('./src/userdata.sh', 'utf8');

    // Import an existing key pair (replace 'your-key-pair-name' with the actual key name)
    //const keyPair = ec2.KeyPair.fromKeyName(this, 'ImportedKeyPair', 'your-key-pair-name');

    // const keyPair = ec2.KeyPair.fromKeyPairName(this,'ImportedKeyPair', 'your-key-pair-name' );

    // Create VPC
    const newWebAppVpc = new ec2.Vpc(this, 'WebAppVpc', {
      cidr: vpcCidr,
      natGateways: 0,
      vpcName: "WebAppVpc",
      maxAzs: 1, // Limit to 1 availability zone
      subnetConfiguration: [
        {
          name: 'public-subnet-1',
          subnetType: ec2.SubnetType.PUBLIC,
          cidrMask: 24,
        },
        {
          name: 'private-subnet-1',
          subnetType: ec2.SubnetType.PRIVATE_ISOLATED,
          cidrMask: 26,
        }
      ],
    });

    // Create a new public security group
    const webServerSG = new ec2.SecurityGroup(this, 'web-server-sg',{
      securityGroupName: "Web-Server-SG",
      vpc: newWebAppVpc,
      allowAllOutbound: true,
    });

    // Allow PORT 22 in SG
    webServerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(22),
      'Allow SSH accesss',
    );

    // Allow HTTP traffic i.e., PORT 80
    webServerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
      'Allow HTTP traffic Access'
    );

    // Allow HTTPS traffic i.e., PORT 443
    webServerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(443),
      'Allow HTTPS traffic Access'
    );

    // Create Web Server i.e., ec2 instance
    const WebServer = new ec2.Instance(this, 'WebServer', {
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
      vpc: newWebAppVpc,
      machineImage: new ec2.AmazonLinuxImage({
        generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
        edition: ec2.AmazonLinuxEdition.STANDARD,
        virtualization: ec2.AmazonLinuxVirt.HVM,
      }),
      keyName: 'us-east-1',
      // keyName: keyPair.keyName,
      vpcSubnets: {
        subnetType: ec2.SubnetType.PUBLIC,
        availabilityZones: ['us-east-1a']
      },
      securityGroup: webServerSG,
    });

    // Add the userdata script to EC2 instance
    WebServer.addUserData(userDataScript);
    
  }
}
