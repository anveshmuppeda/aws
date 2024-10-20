# Day 11 
## CloudFormation Templates with Different stages based on Environments:  
Environments that are considering: 
1. Dev 
2. Test
3. Prod 

## Latest AMIs:  
### Ubuntu  
```
aws ssm get-parameters --names /aws/service/canonical/ubuntu/server/18.04/stable/current/amd64/hvm/ebs-gp2/ami-id --region ap-northeast-3
```
### Linux: 
```
aws ssm get-parameters-by-path --path "/aws/service/ami-amazon-linux-latest" --region us-east-1
aws ssm get-parameters-by-path \
    --path "/aws/service/ami-amazon-linux-latest" \
    --region region

aws ssm get-parameters-by-path \
 --path /aws/service/ami-amazon-linux-latest \
 --query 'Parameters[].Name'
```

### Syntax: 
```
    LatestAmiId:
                Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                Default: '/aws/service/canonical/ubuntu/server/jammy/stable/current/amd64/hvm/ebs-gp2/ami-id'
```