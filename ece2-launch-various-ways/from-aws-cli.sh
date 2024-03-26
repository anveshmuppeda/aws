aws ec2 run-instances \
  --image-id ami-053b0d53c279acc90 \
  --instance-type t2.micro \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=FromAWSCli}]"
