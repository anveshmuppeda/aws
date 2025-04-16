
---

**Author**: [Sandeep Allakonda](https://www.linkedin.com/in/sandeep-allakonda)

---

## 📚 Table of Contents

- [Amazon Elastic Block Store (EBS)](#amazon-elastic-block-store-ebs)
- [How to Partition, Format and Mount an EBS Volume on EC2](#how-to-partition,-format-and-mount-an-ebs-volume-on-ec2)

---

## Amazon Elastic Block Store (EBS)

### 📌 1. What is Amazon EBS?

Amazon EBS is a **block-level storage** service designed for EC2 instances. It provides:

- **Persistent**
- **High-performance**
- **Highly available**

storage volumes.

**🔸 Example:**  
Launching a database server? Use EBS for fast, durable disk storage.

---

### 💽 2. Types of EBS Volumes

| Type       | Description                          | Use Case                          |
|------------|--------------------------------------|-----------------------------------|
| **gp3**    | General Purpose SSD (latest gen)     | Boot volumes, web servers         |
| **gp2**    | General Purpose SSD (older gen)      | Legacy workloads                  |
| **io1/io2**| Provisioned IOPS SSD                 | High-performance databases (SQL)  |
| **st1**    | Throughput Optimized HDD             | Big data, log processing          |
| **sc1**    | Cold HDD                             | Archiving, infrequent access      |

**🔹 Examples:**  
- High-performance DB → use **io2**  
- Daily logs or big data → use **st1**

---

### 🧩 Key EBS Features

#### 🔐 Encryption
- Encryption **at rest**, **in transit**, and in **snapshots**
- Managed via **AWS KMS**

#### 📈 Resize Without Downtime
- Increase size
- Modify type or IOPS  
*(No need to stop the instance!)*

---

### ⚡ Performance Notes

- **gp3**: 125 MB/s & 3,000 IOPS (default, can be provisioned higher)
- **io2**: Up to 64,000 IOPS per volume
- **st1/sc1**: Focused on **throughput**, not IOPS

---

## 🛠️ Step-by-Step: Add & Mount EBS on Ubuntu EC2

---

### 🔹 Step 1: Create an EBS Volume

1. Log in to AWS Console
2. Go to **EC2 Dashboard → Volumes**
3. Click **Create Volume**
   - Choose **Size**, **Type**, **Availability Zone**
4. Click **Create Volume**

---

### 🔹 Step 2: Attach the Volume

1. Select the volume → **Actions → Attach Volume**
2. Pick your instance
3. Set a device name (e.g., `/dev/xvdf`)
4. Click **Attach**

---

### 🔹 Step 3: Connect via SSH

```bash
ssh -i your-key.pem ec2-user@your-ec2-ip
lsblk
```

---

### 🔹 Step 4: Format & Mount the Volume

#### ✅ Check for existing filesystem

```bash
sudo file -s /dev/xvdf
```

#### ✅ Format (if empty)

```bash
sudo mkfs -t ext4 /dev/xvdf
```

#### ✅ Create mount point

```bash
sudo mkdir /mnt/ebs-volume
```

#### ✅ Mount the volume

```bash
sudo mount /dev/xvdf /mnt/ebs-volume
```

---

### 🔹 Step 5: Make Mount Persistent

#### ✅ Get UUID

```bash
sudo blkid /dev/xvdf
```

#### ✅ Edit `/etc/fstab`

```bash
sudo nano /etc/fstab
```

Add:

```fstab
UUID=your-uuid-here  /mnt/ebs-volume  ext4  defaults,nofail  0  2
```

Save and exit:
- `CTRL + O`, `Enter`
- `CTRL + X`

---

### 🔹 Step 6: Verify

```bash
df -h
```

---

## How to Partition, Format and Mount an EBS Volume on EC2

---

### 🧠 What is EBS?

Amazon EBS provides **persistent block storage** for EC2 — like a hard disk in the cloud.

---

### 🧩 What is a Partition?

A partition divides a disk into logical units — OS, app data, backups, etc. Think of it like slices of cake 🍰.

---

### ✅ Step 1: Launch EC2 Instance

- Choose **Amazon Linux 2** or preferred OS
- Use **t2.micro** for testing
- Set up networking & key pair

---

### ✅ Step 2: Create & Attach EBS Volume

1. Go to **Volumes → Create Volume**
2. Choose size (e.g., 10 GiB), AZ
3. After creation → **Actions → Attach**
4. Attach to EC2 with `/dev/xvdf`

---

### ✅ Step 3: Partition the Volume

```bash
sudo fdisk /dev/xvdf
```

Commands in `fdisk`:

1. `m` → Help menu  
2. `n` → New partition  
   - `p` for primary  
   - Partition #1 → +5G  
3. Repeat for second partition  
4. `w` → Save and exit

Check:

```bash
lsblk
```

---

### ✅ Step 4: Format the Partitions

Use XFS for high performance:

```bash
sudo mkfs -t xfs /dev/xvdf1
sudo mkfs -t xfs /dev/xvdf2
```

---

### ✅ Step 5: Mount the Partitions

```bash
sudo mkdir /mnt/volume1
sudo mkdir /mnt/volume2

sudo mount /dev/xvdf1 /mnt/volume1
sudo mount /dev/xvdf2 /mnt/volume2

df -h
```

---

### ✅ Summary

You’ve now:

- ✅ Created & attached EBS
- ✅ Partitioned it
- ✅ Formatted with XFS
- ✅ Mounted to EC2

This makes your EC2 setup scalable, flexible, and production-ready.

---