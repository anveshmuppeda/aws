knife ec2 server create \
  --image ami-053b0d53c279acc90 \
  --flavor t2.micro \
  --region us-east-1 \
  --node-name my-ec2-instance \
  --run-list 'recipe[ec2_cookbook]'