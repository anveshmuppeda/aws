# Let's restore the Manual Deleted Resources back to the CFT  
1. First create the 3 S3 buckets using the stack 01-s3-stack.yaml.  
2. Once three buckets are created, let's delete any one of the bucket manually from the console. In our case we are deleting the `anvesh-muppeda-demo-bucket2`. 
3. Now let's try to deploy the same stack again, this time it won't give us any error, since there were no changes from the previous template and to the deleted bucket resource. 
4. 