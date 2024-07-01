#!/bin/bash

sudo su
yum update -y

yum install -y httpd
systemctl start httpd
systemctl enable httpd

echo "<h1>Welcome from Second CDK Stack</h1>" > /usr/share/httpd/noindex/index.html