# Deploying hello world lambda function to aws using serverless  

Enter serverless  
## to create serverless project  
```
sls create --template google-python --path hello-world-gpython
```

## to deploy project   
```
sls deploy
```  

## to deploy just a function  
```
sls deploy function -f <functionname>
```  

## to create new project  
run below commands  
```
sls   
```  

## to remove the entire project  
```
sls remove
```

Creating a new serverless project  

? What do you want to make? AWS - Node.js - Starter  
? What do you want to call this project? aws-node-project  

✔ Project successfully created in aws-node-project folder  

? Register or Login to Serverless Framework No  

? Do you want to deploy now? No  

What next?  
Run these commands in the project directory:  

serverless deploy    Deploy changes  
serverless info      View deployed endpoints and resources  
serverless invoke    Invoke deployed functions  
serverless --help    Discover more commands  
