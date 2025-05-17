---

### **Author**: [Sandeep Allakonda](https://www.linkedin.com/in/sandeep-allakonda)

---

## 📚 Table of Contents

- [Seamless Web Hosting with Amazon EFS | Set Up Shared Storage on Ubuntu Servers](#seamless-web-hosting-with-amazon-efs--set-up-shared-storage-on-ubuntu-servers)
- [Scaling Shared Storage: Using AWS EFS with Multiple EC2 Instances](#scaling-shared-storage-using-aws-efs-with-multiple-ec2-instances)

---

## Seamless Web Hosting with Amazon EFS | Set Up Shared Storage on Ubuntu Servers

📂 **Amazon EFS** provides scalable, elastic file storage for AWS Cloud and on-premises resources. This guide shows how to set up an EFS instance and link it to two 🖥️ Ubuntu servers to serve 🌐 web content.

---

### **Step 1: Create an Amazon EFS File System**

1. **Sign in to AWS Console**
   - Go to **Services → Elastic File System (EFS)**

2. **Create a New File System**
   - Click **Create file system**
   - Name it (e.g., `my-efs`)
   - Select your **VPC** and **Availability Zones**
   - Choose **Performance Mode** (e.g., *General Purpose*)
   - Click **Create**

---

### **Step 2: Launch Two Ubuntu EC2 Instances**

1. **Go to AWS EC2 Console**
   - Open the **EC2 Dashboard**

2. **Launch Instances**
   - Choose **Ubuntu Server** (e.g., *Ubuntu 22.04 LTS*)
   - Select **t2.micro** (for free tier)
   - Ensure instances are in the **same VPC/subnet**
   - Configure **Security Group**:
     - Allow **SSH (port 22)**
     - Allow **NFS (port 2049)**

---

### **Step 3: Mount EFS on Both Instances**

1. **Install Required Packages**

```bash
sudo apt update
sudo apt install -y nfs-common
```

2. **Get Your File System ID**
   - In AWS Console → EFS
   - Copy your **File System ID** (e.g., `fs-abc12345`)

3. **Create Mount Directory**

```bash
sudo mkdir -p /mnt/efs
```

4. **Mount EFS**

```bash
sudo mount -t nfs4 -o nfsvers=4.1 fs-abc12345.efs.<region>.amazonaws.com:/ /mnt/efs
```

> Example:
```bash
sudo mount -t nfs4 -o nfsvers=4.1 fs-07862ddce9735a46b.efs.ap-south-1.amazonaws.com:/ /mnt/efs
```

5. **Verify Mount**

```bash
df -h
```

---

### **Step 4: Configure Apache Web Server**

1. **Install Apache**

```bash
sudo apt install -y apache2
```

2. **Update Apache to Use EFS**

```bash
sudo rm -rf /var/www/html
sudo ln -s /mnt/efs /var/www/html
```

3. **Restart Apache**

```bash
sudo systemctl restart apache2
```

4. **Add Sample Web Page**

```bash
echo "<h1>SANDEEP ALLAKONDA</h1>" | sudo tee /mnt/efs/index.html
```

5. **Access the Page**

- Visit from both instance IPs:
  - `http://<server-1-ip>`
  - `http://<server-2-ip>`

---

### 🎯 Conclusion

✅ Amazon EFS is now successfully set up and mounted on both Ubuntu instances.  
🌐 Web content is served directly from EFS, allowing shared access.

**Benefits:**

- 🔁 High availability
- 📈 Auto-scalable storage
- 🧩 Real-time consistency

Perfect for web apps requiring shared file storage across instances.

---

## Scaling Shared Storage: Using AWS EFS with Multiple EC2 Instances

This guide covers setting up AWS EFS for shared access across multiple EC2 instances, ensuring scalability, high availability, and effective storage management. 🚀🔗💾

---

### What is EFS?

Amazon EFS is a fully managed, scalable file system for EC2 instances over NFS.  
✅ Unlike EBS, EFS supports simultaneous access by multiple instances.

---

### 🔑 Key Features

- ✅ Fully managed
- 📏 Auto-scalable
- 🔗 Shared access
- 💾 High durability & availability
- 🚀 Performance modes: *General Purpose*, *Max I/O*

---

### How to Set It Up

#### **Step 1: Create an EFS File System**

1. Navigate to **AWS Console → EFS**
2. Click **Create file system**
3. Set:
   - **VPC**
   - Enable backups (optional)
   - Choose performance mode

---

#### **Step 2: Launch EC2 Instances**

1. Launch **2 instances** (Amazon Linux 2 or Ubuntu)
2. Choose **t2.micro**
3. Configure **Security Group**:
   - Allow **SSH (22)** and **NFS (2049)**

---

#### **Step 3: Mount EFS**

**For Amazon Linux 2:**

```bash
sudo yum install -y amazon-efs-utils
```

**For Ubuntu:**

```bash
sudo apt update
sudo apt install -y nfs-common
```

**Mount:**

```bash
sudo mkdir /mnt/efs
sudo mount -t efs fs-xxxxxxxx:/ /mnt/efs
```

> Example:
```bash
sudo mount -t efs fs-0182de0ece525bb79:/ /mnt/efs
```

---

#### **Step 4: Serve HTML from EFS**

1. **Create Directory:**

```bash
sudo mkdir -p /mnt/efs/html
```

2. **Create HTML File:**

```bash
echo "<h1>Sandeep Allakonda</h1>" | sudo tee /mnt/efs/html/index.html
```

3. **Install Apache (Amazon Linux):**

```bash
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
```

4. **Serve from EFS:**

```bash
sudo ln -s /mnt/efs/html /var/www/html/shared
sudo systemctl restart httpd
```

---

#### **Step 5: Access Web Page**

- Open browser:
  - `http://<EC2-1-Public-IP>/shared/index.html`
  - `http://<EC2-2-Public-IP>/shared/index.html`

> You should see: **“Sandeep Allakonda”**

---

### ✅ Conclusion

You've successfully configured Amazon EFS with multiple EC2 instances!

🔧 **Use Cases**:
- Scalable web apps
- Shared file systems
- CMS setups

---
