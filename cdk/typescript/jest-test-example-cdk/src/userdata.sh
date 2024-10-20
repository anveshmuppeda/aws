#!/bin/bash

sudo su
yum update -y

yum install -y httpd
systemctl start httpd
systemctl enable httpd

echo "<h1>Welcome to My First CDK Project</h1>" > /usr/share/httpd/noindex/index.html