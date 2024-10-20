provider "aws" {
  region = "us-east-1"  # Specify your desired AWS region
}

resource "aws_instance" "ec2-from-terraform" {
  ami           = "ami-053b0d53c279acc90"  # Specify the AMI ID of the instance you want to launch
  instance_type = "t2.micro"  # Specify the instance type
  tags = {
    Name        = "FromTerraform"
  }
}

