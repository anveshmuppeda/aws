# Let's import the existing resources to the CFT
1. First create the 2 S3 buckets using the stack `01-original-stack.yaml`.
2. Let's create another S3 bucket manually from the console. In our case we are creating the `anvesh-muppeda-demo-bucket3`.
3. Now update the newly created bucket resource on the cft `02-imported-stack.yaml`.
4. Now use the Import feature of cloudformation to import the existing resource to the cft using the `02-imported-stack.yaml`.
