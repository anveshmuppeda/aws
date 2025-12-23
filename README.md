<div align="center"> 
  <h1>🚀 AWS Complete Hands‑On Guides 🌟</h1>
  
  <a href="https://github.com/anveshmuppeda/aws">
    <img src="https://readme-typing-svg.demolab.com?font=italic&weight=700&size=18&duration=4000&pause=1500&color=FF9900&center=true&width=600&lines=Learn+AWS+with+hands-on+guides+and+real+projects." alt="Typing SVG" />
  </a>  

  <br/>

  <!-- GitHub Repo Shields -->
  <img src="https://img.shields.io/github/forks/anveshmuppeda/aws" alt="Forks"/>
  <img src="https://img.shields.io/github/stars/anveshmuppeda/aws" alt="Stars"/>
  <img src="https://img.shields.io/github/watchers/anveshmuppeda/aws" alt="Watchers"/>
  <img src="https://img.shields.io/github/last-commit/anveshmuppeda/aws" alt="Last Commit"/>
  <img src="https://img.shields.io/github/commit-activity/m/anveshmuppeda/aws" alt="Commit Activity"/>
  <img src="https://img.shields.io/github/repo-size/anveshmuppeda/aws" alt="Repo Size"/>
  <img src="https://img.shields.io/static/v1?label=Support&message=If%20Useful&style=flat&color=BC4E99" alt="Support Badge"/>


  <img src="https://awesome.re/badge.svg" alt="Awesome"/>
  <a href="https://github.com/anveshmuppeda/aws/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/anveshmuppeda/aws" alt="GitHub contributors"/>
  </a>
  <a href="https://github.com/anveshmuppeda/aws/issues">
    <img src="https://img.shields.io/github/issues/anveshmuppeda/aws" alt="Open Issues"/>
  </a>
  <a href="https://github.com/anveshmuppeda/aws/pulls">
    <img src="https://img.shields.io/github/issues-pr-raw/anveshmuppeda/aws" alt="Open PRs"/>
  </a>
  <a href="https://github.com/anveshmuppeda/aws/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/>
  </a>
</div>

---

<div align="center">
  <h2><b>Author: <a href="https://github.com/anveshmuppeda">Anvesh Muppeda</a> 
    <img src="https://avatars.githubusercontent.com/u/115966808?v=4&s=20" alt="Profile Pic"/></b>
  </h2>
  <p><i>Cloud Engineer | Kubernetes Developer | Open Source Contributor</i></p>

  <!-- Social Media Badges -->
  <a href="https://www.linkedin.com/in/anveshmuppeda/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin&style=flat" alt="LinkedIn"/>
  </a>
  <a href="https://twitter.com/Anvesh66743877">
    <img src="https://img.shields.io/badge/Twitter-Follow-blue?logo=twitter&style=flat" alt="Twitter"/>
  </a>
  <a href="https://medium.com/@muppedaanvesh">
    <img src="https://img.shields.io/badge/Medium-Blog-black?logo=medium&style=flat" alt="Medium"/>
  </a>
  <a href="mailto:muppedaanvesh@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact%20Me-red?logo=gmail&style=flat" alt="Email"/>
  </a>
  <a href="https://hub.docker.com/u/anvesh35">
    <img src="https://img.shields.io/badge/DockerHub-Profile-blue?logo=docker&style=flat" alt="DockerHub"/>
  </a>
</div>

---
# AWS Hands-On Labs Repository

Welcome to the AWS Hands-On Labs Repository – a one-stop resource for learning, exploring, and mastering AWS services through practical, step-by-step labs and CloudFormation guides. This repository is built to serve everyone—from beginners to seasoned professionals—by providing clear, easy-to-follow examples that cover a wide range of AWS services and infrastructure-as-code tools.  

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Key Components](#key-components)
  - [AWS CDK](#aws-cdk)
  - [cdk8s](#cdk8s)
  - [CloudFormation Templates and Guides](#cloudformation-templates-and-guides)
  - [Additional Services and Projects](#additional-services-and-projects)
- [AWS Interview Questions](#awsinterviewquestions)
- [My Blogs On AWS](#my-blogs-on-aws)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contribution Guidelines](#contribution-guidelines)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

## Overview

This repository is curated to provide a comprehensive collection of hands-on labs for a diverse set of AWS services. Our goal is to support learners, cloud architects, developers, and DevOps engineers by offering practical examples and detailed guides that help you build proficiency in:
- **Infrastructure as Code:** Dive into AWS CDK, cdk8s, and CloudFormation to learn how to design and deploy robust cloud architectures.
- **Service-Specific Labs:** From basic VPC and EC2 examples to advanced use cases such as Lambda functions, API Gateways, S3 Buckets, and beyond.
- **Step-by-Step Guides:** Each lab includes well-commented code, clear instructions, and an explanation of best practices to help you understand the underlying AWS services.
- **Hands-On Learning:** Experiment with our templates and guides to quickly set up, deploy, and validate your own cloud solutions.

## Repository Structure

The repository is structured to ensure ease of navigation. Here is an overview of the main directories:

```
/aws
├── README.md                   # This file
├── cdk                         # Hands-on labs and CDK constructs for different AWS services
│   ├── hello-world-l1          # Example 1: Simple AWS CDK application
│   ├── hello-world-l2          # Example 2: Advanced CDK constructs and patterns
│   ├── hello-world-l3          # Example 3: Complex multi-stack examples
│   └── simple-lambda-apigateway# Single Lambda/API Gateway example
├── cdk8s                       # Labs demonstrating Kubernetes infrastructure with cdk8s
│   └── basic-app               # Example: Define Kubernetes manifests using code
├── cloudformationtemplates     # All CloudFormation templates and solution guides
│   ├── vpc                     # VPC and networking-related examples
│   ├── lambda                  # Lambda function and serverless app examples
│   └── etc.
├── projects                    # Additional sample projects for node, Python, and serverless deployments
│   ├── aws-node-project
│   ├── lambda
│   └── serverless
└── docs                        # Documentation, class slides, and additional resources
```

Each main folder is self-contained, with a `README.md` that offers context, instructions, and references to the relevant steps.

## Key Components

### AWS CDK

- **What it is:** AWS CDK allows you to define cloud infrastructure in your favorite programming language and deploy it through AWS CloudFormation.
- **What You’ll Find:** Multiple labs under `cdk` that showcase best practices for using AWS CDK—ranging from basic stack creation to constructing multi-tier architectures.
- **Learn More:** Each CDK lab provides a detailed guide on setting up, running, and testing your deployments.

### cdk8s

- **What it is:** cdk8s is an open-source framework that enables you to define Kubernetes applications and generate standard YAML manifests using familiar programming languages.
- **What You’ll Find:** Under the `cdk8s` folder, you will see sample applications demonstrating how to create and manage Kubernetes resources programmatically.
- **Learn More:** Each lab contains instructions and code samples that walk you through the process of container orchestration and deployment.

### CloudFormation Templates and Guides

- **What they are:** CloudFormation provides a proven way to model and provision AWS infrastructure using declarative templates.
- **What You’ll Find:** The `cloudformationtemplates` folder contains a comprehensive collection of templates, from simple networking stacks to complex multi-service deployments. These templates are complemented by step-by-step guides.
- **Learn More:** Our documentation includes usage instructions, parameter explanations, and best practices for organizing and deploying CloudFormation stacks.

### Additional Services and Projects

- **Projects Folder:** Explore sample projects that integrate various AWS services. Whether you prefer Node.js, Python, or serverless architectures, you will find hands-on samples that demonstrate real-world scenarios.
- **Documentation and Classes:** The `docs` folder includes additional resources such as class slides, diagrams, and diagrams to supplement your learning.


## Interview Questions
[click here](./qa/README.md)


## How to Use This Repository

1. **Browse the Directory:** Start by navigating to the directory that matches your interest (e.g., CDK labs, CloudFormation templates).
2. **Follow the Guides:** Each sub-folder comes with its own README that provides the context, prerequisites, and step-by-step instructions.
3. **Run the Code:** Clone the repository, set up your environment as per the guide, and run the sample labs.
4. **Experiment and Expand:** Use these examples as a foundation to experiment with your own AWS services and configurations. Feedback and improvements are always welcome!

## Contribution Guidelines

We welcome contributions from everyone! Whether you are adding new labs, improving existing documentation, or suggesting new service demos, your help is invaluable. To contribute:

- **Fork the Repository:** Create your own branch for new features or fixes.
- **Follow the Coding Standards:** Consistency is key—maintain the same directory structure and coding style used throughout the repo.
- **Document Your Changes:** Update or add relevant documentation so users can understand your contribution.
- **Submit a Pull Request:** Once you’re happy with your changes, submit a pull request with a clear description of your updates.
- **Open Issues:** If you have questions or suggestions, feel free to open an issue to discuss improvements with the community.

## Roadmap

Our roadmap is driven by community needs and the evolving AWS ecosystem:
- **Expand Service Labs:** We plan to add more hands-on labs for additional AWS services.
- **Enhance Guides:** Detailed best practices and troubleshooting sections are in the works.
- **Interactive Learning:** Future updates may include interactive tutorials and video walkthroughs.
- **Community Collaboration:** We encourage you to share your ideas and contribute to our growing ecosystem!

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

For questions, suggestions, or discussions, please reach out:
- **GitHub Issues:** Use the repository’s [issue tracker](https://github.com/anveshmuppeda/aws/issues) to report bugs or request new features.

---

Thank you for exploring the AWS Hands-On Labs Repository. Let’s build, learn, and innovate together on the cloud!

---
