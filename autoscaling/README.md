---

### **Author**: [Sandeep Allakonda](https://www.linkedin.com/in/sandeep-allakonda)

---

## 🚀 AWS Auto Scaling Tutorial: Launch Template to Auto-Healing EC2 Instances

AWS Auto Scaling is a game-changer for managing EC2 instances. It automatically adjusts the number of running instances in response to traffic changes — improving availability while optimizing cost.

In this tutorial, we’ll walk you through setting up Auto Scaling using EC2, AMIs, Launch Templates, and CloudWatch. We’ll also simulate traffic to trigger scaling events and monitor the process in action.

Let’s get started! 💡

---

### ✅ Step 1: Launch an EC2 Instance

1. Go to the **AWS EC2 Console**.
2. Click **Launch Instance**.
3. Choose an Amazon Machine Image (AMI), e.g., **Amazon Linux 2**.
4. Select an instance type like **t2.micro** (Free Tier eligible).
5. Configure storage and network settings as needed.
6. Add a **Security Group** (e.g., allow SSH and HTTP).
7. Scroll to **Advanced Details** in "Configure Instance".
8. Find the **User Data** field.
9. Paste the script:
    ```bash
    #!/bin/bash
    yum install httpd git -y
    service httpd start
    chkconfig httpd on
    cd /var/www/html
    rm -rf /var/www/html/*
    git clone https://github.com/sandeepallakonda/Analog-Digital-Clock.git
    cp -r Analog-Digital-Clock/* .
    rm -rf Analog-Digital-Clock
    service httpd restart
    ```
10. Launch the instance using a **key pair**.

**🟢 Result**: Apache is installed, started, and configured to serve content from the GitHub repository.

---

### 📸 Step 2: Create an AMI from Your EC2 Instance

1. Connect to the instance via SSH.
2. Install your app or any required packages.
3. *(Optional)* Install `stress` to simulate load:
    ```bash
    sudo yum install stress -y
    ```
4. From the EC2 dashboard:  
   **Instance → Actions → Image and templates → Create image**
5. Name and create the image.

📦 This AMI captures your instance configuration for reuse.

---

### 🧰 Step 3: Create a Launch Template from the AMI

1. Navigate to **Launch Templates** in EC2.
2. Click **Create launch template**.
3. Provide a name and description.
4. Select the AMI you created earlier.
5. Choose instance type (e.g., **t2.micro**).
6. Define key pair, network settings, and security group.
7. Click **Create launch template**.

🔁 This template is used by Auto Scaling to launch new instances.

---

### 📡 Step 4: Set Up CloudWatch Alarms and SNS Notifications

1. Go to **Amazon SNS** and create a topic.
2. Subscribe your email to receive alerts.
3. Confirm the email subscription.
4. Go to **CloudWatch → Alarms → Create Alarm**.
5. Choose the EC2 metric (e.g., **CPUUtilization**).
6. Set threshold (e.g., **CPU > 40% for 2 minutes**).
7. Set action to notify your SNS topic.

📬 You’ll receive alerts when conditions are met to trigger scaling.

---

### ⚙️ Step 5: Create an Auto Scaling Group

1. Navigate to **Auto Scaling Groups**.
2. Click **Create Auto Scaling group**.
3. Choose the **Launch Template** you created.
4. Define group size (e.g., min 1, desired 1, max 3).
5. Set your **VPC and Subnets**.
6. Configure **scaling policies** (based on CloudWatch alarms).
7. Enable **health checks** (EC2 and ELB if applicable).
8. Click **Create Auto Scaling group**.

🛡️ AWS now automatically manages instance count based on performance.

---

### 🔥 Step 6: Simulate Load and Trigger Auto Scaling

1. SSH into your EC2 instance.
2. Run the following to simulate CPU stress:
    ```bash
    sudo apt update
    sudo apt install stress -y
    stress --cpu 2 --timeout 300
    ```

This stresses 2 CPU cores for 5 minutes, increasing utilization and triggering CloudWatch alarms.

📈 Watch Auto Scaling launch new instances!

---

### 📊 Step 7: Monitor with CloudWatch and SNS

1. Open **CloudWatch** to monitor metrics and alarms.
2. Check email for **SNS notifications**.
3. Confirm new instances in your **Auto Scaling Group** via the EC2 dashboard.

👁️ Monitoring ensures your scaling rules are working correctly.

---

### 🔻 Step 8: Observe Auto Scaling Down

1. After the CPU load drops, CloudWatch resets the alarm.
2. Auto Scaling terminates extra instances, maintaining desired count.

💸 You're only billed for what you use — efficiency at its best!

---

### 🧠 Conclusion

You’ve now set up a complete AWS Auto Scaling environment from scratch! With **Launch Templates**, **AMIs**, **CloudWatch**, and **SNS**, your infrastructure is now self-healing and responsive to demand.

🔧 Whether you’re deploying a production app or experimenting with AWS, this is a crucial step toward mastering modern cloud-native architecture.

---
