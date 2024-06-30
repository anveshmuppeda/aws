# Getting Started with AWS CDK TypeScript Project  
Welcome to your first AWS CDK project! This guide will help you create a simple Lambda function using TypeScript. Let's dive in step-by-step.

## Setting Up Your Project  
Once everything is setup using this page, then follow the below commands to develop and deploy your first CDK project.

### 1. Create a New Folder  

Start by creating a new folder for your project:
```sh
mkdir my-first-cdk
cd my-first-cdk
```

### 2. Initialize CDK Stack  
Inside your project directory, initialize the CDK stack with TypeScript:
```sh
cdk init --language typescript
```  

## Writing Your CDK Stack  

### 3. Update Stack code   
Update the **lib/my-first-cdk-stack.ts** file with the following TypeScript code to define a Lambda function:  
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

## Developing Your Lambda Function  
### 4. Create Source Directory and Lambda Function  
Create a `src` directory inside `my-first-cdk/` and add an `index.ts` file with your Lambda function code:  

```ts
export const handler = async (event: { name: string }) => {
    const result: string = event.name ? `Good Job ${event.name}!` : 'Good Job'
    return result
}
```

## AWS Configuration and Deployment  
### 5. Configure AWS CLI  
Ensure your AWS CLI is configured with:   
```sh
aws configure
```

### 6. Compile TypeScript Code  
Compile TypeScript to JavaScript using:  
```sh
npm run build
```

### 7. Review Changes  
Review the resources to be created with:  
```sh
cdk diff
```

### 8. Bootstrap the Environment  
Bootstrap your environment initially with:  
```sh
cdk bootstrap
```

### 9. Deploy Your CDK Stack  
Deploy your CDK stack to AWS:  
```sh
cdk deploy
```

## 10. Test the newly created Lambda function
After deployment, test your Lambda function:  
![New Lambda Function](./../images/aws-lambda-func.png)  

**Configure test event using the below instructions.**  
![Configure Test Event](./../images/configure-test-event.png)

**Run the Test event.**
![alt text](./../images/run-test-evnt.png)

```sh
Response
"Good Job Anvesh Muppeda!"
```

**Congratulations! You've successfully created an AWS Lambda function using AWS CDK and TypeScript.** 

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `npx cdk deploy`  deploy this stack to your default AWS account/region
* `npx cdk diff`    compare deployed stack with current state
* `npx cdk synth`   emits the synthesized CloudFormation template  
