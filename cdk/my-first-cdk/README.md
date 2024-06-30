# Welcome to your first CDK TypeScript project

This is first AWS CDK Project which creates a simple lambda function using typescript.
Let's get started.

Once everything is setup using this page, then follow the below commands to develop and deploy your first CDK project.

## Create a new folder
First let's create a new folder for your new project.
mkdir my-first-cdk


## Create CDK Stack  
Let's create the CDK stack inside the newly created directory using the below command.
cd my-first-cdk
cdk init --language typescript


## Update lib code  
Update the **lib/my-first-cdk-stack.ts** code with the below code.  
```ts
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';

export class MyFirstCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new lambda.Function(this, 'lambdafunction', {
      functionName: 'first-cdk-lambda',
      code: new lambda.AssetCode('src'),
      handler: 'index.handler',
      runtime: lambda.Runtime.NODEJS_16_X,
      memorySize: 128
    })
  }
}
```

## Create src directory and update the lambda function code
Mow let's create a new directory src inside my-first-cdk/
mkdir src

Now let's create a new file index.ts and update the below simple lambda function code.
```ts
export const handler = async (event: { name: string }) => {
    const result: string = event.name ? `Good Job ${event.name}!` : 'Good Job'
    return result
}
```

## Configure AWS CLI  
Now let's configure the AWS CLI to create the above stack in AWS.
```sh
aws configure
```

## Compile the TypeScript code  
Now let's compile the above typescript code into javascript using the below command.  
```sh
npm run build
```

## Run diff Command  
Check the resources that are going to create ith above stack in AWS using the below command. 
```sh
cdk diff
```

## Bootstrap the environment  
Now bootstrap the environment using the below command. This will require at the intial setup of the cdk environment.  
```sh
cdk bootstrap
```

## Deploy the CDK Stack  
The final step, now deploy the above cdk stack into AWS using the below command.
```sh
cdk deploy
```

## Test the newly created Lambda function
Using the above cdk, we have succesfully created the lambda function. 
![New Lambda Function](./../images/aws-lambda-func.png)

Configure test event using the below instructions. 
![Configure Test Event](./../images/configure-test-event.png)

Run the Test event.
![alt text](./../images/run-test-evnt.png)

```sh
Response
"Good Job Anvesh Muppeda!"
```

Using the above instructions finally we have created a AWS Lambda function using CDK typescript.  

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template
