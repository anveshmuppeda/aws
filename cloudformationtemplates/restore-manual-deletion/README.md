# Let's restore the Manual Deleted Resources back to the CFT  
1. First create the 3 S3 buckets using the stack `01-s3-stack.yaml`.  
2. Once three buckets are created, let's delete any one of the bucket manually from the console. In our case we are deleting the `anvesh-muppeda-demo-bucket2`. 
3. Now let's try to deploy the same stack again, this time it won't give us any error, since there were no changes from the previous template and to the deleted bucket resource. 
4. Now I am updating the deleted resource on the cft by adding the tags `02-s3-stack.yaml`. And deploying using the shell script `stack-creation.sh`. 
5. But this time it will give the error by saying the bucket doesn not exist.
```
Resource handler returned message: "The specified bucket does not exist (Service: S3, Status Code: 404, Request ID: 85TGA9Z2PVKFD2FT, Extended Request ID: GTaJonyOgUrNIazo7JfTplWOkR9WZcnDPuz6nBF6VzRKsWR0+T2b91guLjOWWjOKQtXinnhuuzP3H9eyFBL73nHk01B8JMZi) (SDK Attempt Count: 1)" (RequestToken: c457c24d-197a-f0bd-ed70-0ddbae623362, HandlerErrorCode: NotFound)
```
6. To fix this we need to rename the bucket name to new one `anvesh-muppeda-demo-bucket4` from `anvesh-muppeda-demo-bucket2`. for this let's use the `03-s3-stack.yaml`.
7. Now deploy the stack using the shell script `stack-creation.sh` it should get deployed successfully.
8. Then we can rename our bucket name to original i.e., `anvesh-muppeda-demo-bucket2` from `anvesh-muppeda-demo-bucket4`. for this let's use the `04-s3-stack.yaml`.
9. Now deploy the stack using the shell script `stack-creation.sh` it should get deployed successfully.
10. Now we have restored the manually deleted resource back to the cft.
