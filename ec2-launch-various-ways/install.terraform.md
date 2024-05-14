# Install Terraform  


### Steps to install terraform on Ubuntu / Ubuntu cloud server :   

```Install unzip```

```sudo apt-get install unzip```  

### Confirm the latest version number on the terraform website:   

```https://www.terraform.io/downloads.html```

### Download latest version of the terraform (substituting newer version number if needed)  
```
wget https://releases.hashicorp.com/terraform/1.0.7/terraform_1.0.7_linux_amd64.zip
Extract the downloaded file archive
```  
```
unzip terraform_1.0.7_linux_amd64.zip
```  

### Move the executable into a directory searched for executables  

```sudo mv terraform /usr/local/bin/```

###  Run it  

```terraform --version ```