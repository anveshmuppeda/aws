#!/bin/bash

# Unset previous AWS environment variables
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN

# Prompt the user for inputs
read -p "Enter AWS_ACCESS_KEY_ID: " AWS_ACCESS_KEY_ID
read -p "Enter AWS_SECRET_ACCESS_KEY: " AWS_SECRET_ACCESS_KEY
read -p "Enter AWS_DEFAULT_REGION: " AWS_DEFAULT_REGION
read -p "Enter ROLE_ARN: " ROLE_ARN

# Export the initial credentials
export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
export AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION

# Assume the role
ASSUME_ROLE_OUTPUT=$(aws sts assume-role --role-arn "$ROLE_ARN" --role-session-name AWSCLI-Session)

# Check if assume-role command was successful
if [ $? -ne 0 ]; then
    echo "Failed to assume role"
    exit 1
fi

# Extract the assumed role credentials
ROLE_ACCESS_KEY_ID=$(echo $ASSUME_ROLE_OUTPUT | awk -F 'AccessKeyId: ' '{print $2}' | awk '{print $1}')
ROLE_SECRET_ACCESS_KEY=$(echo $ASSUME_ROLE_OUTPUT | awk -F 'SecretAccessKey: ' '{print $2}' | awk '{print $1}')
ROLE_SESSION_TOKEN=$(echo $ASSUME_ROLE_OUTPUT | awk -F 'SessionToken: ' '{print $2}')

# Create a temporary file for export commands
TEMP_FILE=$(mktemp /tmp/export_commands.XXXXXX)

# Write the export commands to the temporary file
echo "export AWS_ACCESS_KEY_ID=$ROLE_ACCESS_KEY_ID" > $TEMP_FILE
echo "export AWS_SECRET_ACCESS_KEY=$ROLE_SECRET_ACCESS_KEY" >> $TEMP_FILE
echo "export AWS_SESSION_TOKEN=$ROLE_SESSION_TOKEN" >> $TEMP_FILE

# Source the temporary file to set the environment variables
source $TEMP_FILE

# Remove the temporary file
rm $TEMP_FILE

# Verify the assumed role
aws sts get-caller-identity
