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