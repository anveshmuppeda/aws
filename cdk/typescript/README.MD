# AWS Cloud Development Kit (AWS CDK)  


This guide provides steps to set up your local development environment for running an AWS CDK project. AWS CDK (Cloud Development Kit) allows you to define cloud infrastructure using familiar programming languages.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Resources](#resources)

## Introduction  
The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework for defining cloud infrastructure in code and provisioning it through AWS CloudFormation.  

The AWS CDK consists of two primary parts:   

1. AWS CDK Construct Library – A collection of pre-written modular and reusable pieces of code, called constructs, that you can use, modify, and integrate to develop your infrastructure quickly. The goal of the AWS CDK Construct Library is to reduce the complexity required to define and integrate AWS services together when building applications on AWS.  

2. AWS CDK Toolkit – A command line tool for interacting with CDK apps. Use the AWS CDK Toolkit to create, manage, and deploy your AWS CDK projects.  

The AWS CDK supports TypeScript, JavaScript, Python, Java, C#/.Net, and Go. You can use any of these supported programming languages to define reusable cloud components known as constructs. You compose these together into stacks and apps. Then, you deploy your CDK applications to AWS CloudFormation to provision or update your resources.  

![AWS Cloud Development Kit Architecture](./images/AppStacks.png)

## Prerequisites
Before you start setting up your environment, ensure you have the following prerequisites installed:

- **Install the AWS CLI**  

- **Node.js and npm**: AWS CDK is built on Node.js, so you'll need Node.js and npm installed. You can download them from [nodejs.org](https://nodejs.org/en/download/package-manager).  

- **Programming language prerequisites**: Other programming language prerequisites depend on the language that you will use to develop AWS CDK applications:  
    For TypeScript 3.8 or later  
    ```bash
    npm -g install typescript
    ```

- **AWS CDK CLI**: Install the AWS CDK command-line interface globally using npm:
  ```sh
  npm install -g aws-cdk
  ```  
  To install a specific version of the CDK CLI, use the following command structure:
  ```sh
  npm install -g aws-cdk@X.YY.Z
  ```  
  Run the following command to verify a successful installation. The AWS CDK CLI should output the version number:
  ```sh
  $ cdk --version
  ```
  If you receive an error message, try uninstalling the AWS CDK CLI by running the following:
  ```sh
  $ npm uninstall -g aws-cdk
  ```

  Then, repeat steps to reinstall the AWS CDK CLI.

- **Configure security credentials for the CDK CLI**  


## Resources   
1. [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
2. [API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)
3. [The TypeScript Workshop](https://cdkworkshop.com/20-typescript.html)
4. [AWS CDK Tutorial for Beginners - Step-by-Step Guide](https://bobbyhadz.com/blog/aws-cdk-tutorial-typescript)