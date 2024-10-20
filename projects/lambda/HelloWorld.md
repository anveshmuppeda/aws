# Hello World using AWS Lambda  
Let us start with Hello World using AWS Lambda.   

## Create HelloWorldFunction  
Go to AWS Lambda Console  
Select Create Function   
Function Name: HelloWorldFunction  
We will use Python3 as a runtime environment.  

Now hello world funciton is created  

## Deploy and test HelloWorldFunction  
Go to AWS Console and use the Lambda template.  
Deploy and Test and make sure it is successful.   

### Here are the default names that are used.  
Program Name: lambda_function  
Function Name: lambda_handler  

We can change the names of the file, function etc. However, we need to ensure that Handler details as part of Runtime Settings are updated.  
 
Let us rename the file name to main.py and validate. We will revert the name back to lambda_function.py.  


## Deploy Project to AWS Lambda console from local  
Let us understand how we can deploy the locally developed Lambda Function to AWS Lambda Web Console.  

You need to build the zip file with the source code using the below command.  

``` zip -r hellolambda.zip lambda_function.py ```  

Use AWS Lambda Web Console to upload the Zip file.  

You can review the source code in Python scripts and test the function by creating a test event.  