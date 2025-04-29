---

### **Author**: [Sandeep Allakonda](https://www.linkedin.com/in/sandeep-allakonda)

---

## 📊 Monitoring EC2 with CloudWatch and SNS Notifications

---

### 📌 Objective

In this tutorial, we will:

- Launch an EC2 instance and host a Git-based website  
- Install the `stress` tool to simulate load  
- Connect the instance to **CloudWatch**  
- Set up a **CloudWatch Alarm** to detect CPU stress  
- Integrate **SNS** to send email notifications when stress is detected  

---

### 🛠️ Prerequisites

- An AWS account with permissions for EC2, CloudWatch, and SNS  
- A GitHub repo (or any Git repo) with your website code  
- An email address to subscribe to SNS notifications  

---

### 🧱 Step 1: Launch EC2 Instance and Set Up Git Website

1. Launch an EC2 instance:
   - **AMI**: Amazon Linux 2  
   - **Instance type**: t2.micro (Free Tier eligible)  
   - **Networking**: Enable Auto-assign Public IP  
   - **Security Group**: Allow HTTP (port 80) and SSH (port 22)  

2. Connect to your instance via SSH:
   ```bash
   ssh -i "your-key.pem" ec2-user@<your-ec2-public-ip>
   ```

3. Install Apache and Git:
   ```bash
   sudo yum update -y
   sudo yum install -y httpd git
   sudo systemctl start httpd
   sudo systemctl enable httpd
   ```

4. Clone your GitHub repo into the web root:
   ```bash
   sudo git clone https://github.com/your-repo.git /var/www/html/
   ```

📍 Your website should now be live at:  
`http://<your-ec2-public-ip>`

5. Use the `top` command to monitor real-time system usage:
   ```bash
   top
   ```

---

### 📬 Step 2: Create an SNS Topic and Subscribe

1. **Open** the Amazon SNS Console.

2. **Create a new topic**:
   - Click **Topics** → **Create topic**  
   - **Type**: Standard  
   - **Name**: `EC2-CPU-Alert`  
   - Click **Create topic**

3. **Add a subscription**:
   - **Protocol**: Email  
   - **Endpoint**: Your email address (e.g., you@example.com)  
   - Click **Create subscription**

4. **Confirm your subscription**:  
   - Check your inbox and click the confirmation link from AWS.

---

### 📈 Step 3: Create CloudWatch Alarm for High CPU

1. Go to **CloudWatch Console → Alarms → Create alarm**

2. Click **Select metric** →  
   Browse to:  
   **EC2 > Per-Instance Metrics > CPUUtilization**

3. Choose your EC2 instance and configure the alarm:
   - **Metric name**: CPUUtilization  
   - **Period**: 1 minute  
   - **Threshold**: Greater than 60  
   - **Consecutive periods**: 2

4. Under **Actions**:
   - Select: **Send a notification to your SNS topic**

5. **Name the alarm**: `EC2-CPU-Alert`  
   - Click **Create alarm**

---

### 📷 Step 4: Check CloudWatch (Without Stress)

- Wait a few minutes after creating the alarm  
- Go to **CloudWatch → Alarms**  
- Status should be **OK (green)** — no CPU spike detected yet

---

### 💥 Step 5: Simulate CPU Stress

1. SSH into your EC2 instance again:
   ```bash
   sudo yum install -y stress
   stress --cpu 2 --timeout 120
   ```

2. What happens:
   - After 1–2 minutes, the CPU load increases
   - CloudWatch detects the spike and changes the alarm state to **ALARM (red)**
   - You receive an **email notification** via SNS

3. To stop the stress process:
   ```bash
   sudo pkill stress
   ```

   Or find and kill it manually:
   ```bash
   ps aux | grep stress
   sudo kill <PID>
   ```

4. After stress is removed:
   - Go to **CloudWatch → Alarms**
   - Alarm status should return to **OK (green)**

---

### ✅ Conclusion

In this tutorial, we demonstrated how to:

- Monitor an EC2 instance using **Amazon CloudWatch**
- Set up **SNS** to receive real-time email alerts
- Simulate high CPU usage with the `stress` tool
- Validate alarm triggers and notification delivery

By implementing this setup, you gain visibility into your instance performance and can react proactively to system stress — a key step in building reliable, production-grade infrastructure. 🚀

---
