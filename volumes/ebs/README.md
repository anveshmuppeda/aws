**Author** : [Sandeep Allakonda](www.linkedin.com/in/sandeep-allakonda)  

---

# 📦 Amazon Elastic Block Store (EBS)

---

## 📌 1. What is Amazon EBS?

Amazon EBS is a block-level storage service designed to be used with EC2 instances. It offers **persistent**, **high-performance**, and **highly available** storage volumes that can be attached to EC2 instances.

**◘ Example:**  
You launch an EC2 instance to run a database. The database needs fast, reliable storage — this is where you use an EBS volume.

---

## 💽 2. Types of EBS Volumes

| Type      | Description                         | Use Case Example                      |
|-----------|-------------------------------------|---------------------------------------|
| **gp3**   | General Purpose SSD (latest gen)    | Web servers, boot volumes             |
| **gp2**   | General Purpose SSD (older)         | Legacy systems                        |
| **io1/io2** | Provisioned IOPS SSD               | High-performance DBs (e.g., SQL)      |
| **st1**   | Throughput Optimized HDD            | Big data, log processing              |
| **sc1**   | Cold HDD                            | Archiving, infrequently accessed data |

**◘ Examples:**  
• High-traffic MySQL database → use **io2**  
• Storing daily logs for analysis → use **st1**

---

## ♦ EBS Features

### • Encryption:
- Encrypts data **at rest**, **in transit**, and **in snapshots**
- Managed using **AWS KMS**

### • Resize Without Downtime:
- Increase volume size
- Change volume type or IOPS

---

## ⚡ Performance Notes:

- **gp3**: Default **125 MB/s**, **3,000 IOPS** (can provision more)
- **io2**: Up to **64,000 IOPS per volume**
- **st1/sc1**: Designed for **throughput**, not IOPS

---

# 🛠️ Step-by-Step: Adding & Mounting EBS Volume on Ubuntu EC2

---

## 🔹 Step 1: Create an EBS Volume

1. **Log in** to AWS Console.
2. **Navigate to EC2 Dashboard.**
3. Go to **Volumes** (under *Elastic Block Store*).
4. Click **Create Volume**.
   - Choose **Size**, **Type**, and **Availability Zone** (must match the EC2 instance's AZ).
5. Click **Create Volume**.

---

## 🔹 Step 2: Attach the Volume to EC2

1. In **Volumes**, select the created volume.
2. Click **Actions → Attach Volume**.
3. Select the instance and set **device name** (e.g., `/dev/xvdf`).
4. Click **Attach**.

---

## 🔹 Step 3: Connect to EC2 Instance via SSH

Use SSH to connect to your EC2 instance.

To verify the attached device:

```bash
lsblk
```

---

## 🔹 Step 4: Format and Mount the EBS Volume

### ✅ Check If It Has a Filesystem

```bash
sudo file -s /dev/xvdf
```

If unformatted, format it:

```bash
sudo mkfs -t ext4 /dev/xvdf
```

### ✅ Create a Mount Point

```bash
sudo mkdir /mnt/ebs-volume
```

### ✅ Mount the Volume

```bash
sudo mount /dev/xvdf /mnt/ebs-volume
```

---

## 🔹 Step 5: Make Mount Permanent

### ✅ Get the UUID of the Volume

```bash
sudo blkid /dev/xvdf
```

### ✅ Edit `/etc/fstab` to Auto-Mount

```bash
sudo nano /etc/fstab
```

Add an entry like this (replace with your UUID):

```bash
UUID=your-uuid-here  /mnt/ebs-volume  ext4  defaults,nofail  0  2
```

Save & exit:

- Press `CTRL + O`, then `Enter`
- Press `CTRL + X` to exit

---

## 🔹 Step 6: Verify the Mount

Check disk usage:

```bash
df -h
```

This confirms the volume is mounted correctly and available.

--

