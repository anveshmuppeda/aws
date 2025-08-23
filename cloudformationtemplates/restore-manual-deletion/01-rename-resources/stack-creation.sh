#!/bin/bash

STACK_NAME="s3-demo-stack"
TEMPLATE_FILE="01-s3-stack.yaml"
REGION="us-east-1"

# Check if stack exists
aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" > /dev/null 2>&1

if [ $? -ne 0 ]; then
  echo "Stack does not exist. Creating stack..."
  aws cloudformation create-stack \
    --stack-name "$STACK_NAME" \
    --template-body file://$TEMPLATE_FILE \
    --region "$REGION" \
    --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
else
  echo "Stack exists. Updating stack..."
  aws cloudformation update-stack \
    --stack-name "$STACK_NAME" \
    --template-body file://$TEMPLATE_FILE \
    --region "$REGION" \
    --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
fi