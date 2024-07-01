#!/bin/bash

sudo su
yum update -y

yum install -y nginx
systemctl start nginx
systemctl enable nginx

chmod 0666 /usr/share/nginx/html

echo "<h1>Welcome to My First CDK Project</h1>" > /usr/share/nginx/html/index.html