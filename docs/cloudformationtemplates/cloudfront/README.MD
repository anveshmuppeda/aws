# **How to Use Amazon CloudFront Cache Invalidation: A Step-by-Step Demo**

Amazon CloudFront is a powerful content delivery network (CDN) that accelerates the delivery of your web content by caching it at edge locations worldwide. However, when you update your content, you need to ensure that users receive the latest version. This is where **cache invalidation** comes into play. In this blog, I’ll walk you through a step-by-step demo of how to set up CloudFront, use cache invalidation, and ensure your users always see the latest content.

---

## **What We’ll Cover**
1. Setting up a simple website using an S3 bucket.
2. Creating a CloudFront distribution.
3. Testing the caching behavior.
4. Performing cache invalidation to update content.

---

## **Step 1: Create a Simple Website and Upload It to S3**

To begin, I created a simple website with a single [inde.html](./website/index.html) file. Here’s how you can do it:

1. Create an [inde.html](./website/index.html) file.

2. Create an S3 bucket named `anveshmuppeda-cloudfront-demo` (or any name of your choice) in the `us-east-1` region.

3. Upload the [inde.html](./website/index.html) file to the S3 bucket.

---

## **Step 2: Create a CloudFront Distribution**

Next, I set up a CloudFront distribution to serve the website from the S3 bucket. Here’s how:

1. Go to the **CloudFront** console and click **Create Distribution**.
2. For **Origin Domain**, select the S3 bucket you created (`anveshmuppeda-cloudfront-demo.s3.us-east-1.amazonaws.com`).
3. Set **Origin Access** to **Origin Access Control (OAC)** and create a new OAC with the same name as the S3 bucket.
4. Disable **Web Application Firewall (WAF)** for this demo.
5. Set the **Default Root Object** to [inde.html](./website/index.html) since this is the entry point for our website.
6. Click **Create Distribution**.

It may take a few minutes for the distribution to deploy. Once it’s ready, you’ll see a **Distribution Domain Name** (e.g., `https://d2b2ak8zu9hbi0.cloudfront.net`).

---

## **Step 3: Allow CloudFront to Access the S3 Bucket**

At this point, if you try to access the CloudFront distribution URL, you’ll see an **Access Denied** error. This is because the S3 bucket is private, and CloudFront doesn’t have permission to access it. To fix this:

1. Go to your CloudFront distribution, navigate to **Origins**, and select your origin.
2. Click **Edit** and copy the policy from the **Origin Access Control Settings** section.
3. Go to your S3 bucket, navigate to **Permissions**, and edit the bucket policy.
4. Paste the copied policy and save the changes.

Now, CloudFront can access the S3 bucket, and you should be able to view your website by visiting the CloudFront distribution URL.

---

## **Step 4: Understanding CloudFront Caching**

When you access your website through CloudFront, the content is served from the nearest **edge location**, not directly from the S3 bucket. For example:
- If your S3 bucket is hosted in **us-east-1 (N. Virginia)** and a user accesses it from **India**, the content is delivered from the nearest edge location in India.
- The edge location caches the content for a default period of **24 hours (86400 seconds)**. This means that subsequent requests from users in the same region will be served from the cache, reducing latency and improving performance.

You can view or modify the cache settings by navigating to your CloudFront distribution, selecting **Behaviors**, and editing the default behavior. Under **Cache Key and Origin Requests**, you’ll find the **Default TTL (Time to Live)** setting.

---

## **Step 5: Testing Cache Behavior**

Let’s test how caching works:

1. Initially, your website displays **Version: v1.0.0**.
2. Update the [inde.html](./website/index.html) file to **Version: v2.0.0** and upload it to the S3 bucket.
3. Access the CloudFront distribution URL again. You’ll still see **v1.0.0** because the edge location is serving the cached version.

---

## **Step 6: Performing Cache Invalidation**

To ensure users see the latest version of your content, you need to **invalidate the cache**. Here’s how:

1. Go to your CloudFront distribution and navigate to **Invalidations**.
2. Click **Create Invalidation**.
3. In the **Object Paths** field, enter `/*` to invalidate all objects in the distribution.
4. Click **Create Invalidation**.

Once the invalidation is complete, refresh the CloudFront distribution URL. You’ll now see the updated content (**v2.0.0**).

---

## **Why Cache Invalidation Matters**

Cache invalidation is crucial for ensuring that users always receive the latest version of your content. Without it, users might see outdated information, which can lead to a poor experience. For example:
- If you’re running an e-commerce site and update product prices, users might see old prices until the cache expires.
- If you’re publishing news articles, users might see outdated news.

By manually invalidating the cache, you can ensure that updates are reflected immediately.

---

## **Real-World Example: Serving Content Globally**

Imagine you’re hosting a website in **N. Virginia (us-east-1)** and have users in **India**. Here’s how CloudFront works:
1. A user in India requests your website.
2. CloudFront routes the request to the nearest edge location (e.g., Mumbai).
3. If the content isn’t cached, the edge location fetches it from the S3 bucket in N. Virginia.
4. The edge location caches the content and serves it to the user.
5. Subsequent requests from users in India are served from the Mumbai edge location, reducing latency.

Without cache invalidation, users in India would continue to see the cached version even after you update the content. By using cache invalidation, you can ensure that all users, regardless of their location, see the latest version.

---

## **Conclusion**

Amazon CloudFront is a powerful tool for delivering content quickly and efficiently. However, caching can sometimes lead to outdated content being served to users. By understanding and using **cache invalidation**, you can ensure that your users always see the latest version of your website.

In this demo, we:
1. Created a simple website and hosted it on S3.
2. Set up a CloudFront distribution.
3. Tested caching behavior.
4. Performed cache invalidation to update content.

I hope this guide helps you get started with CloudFront and cache invalidation. If you have any questions or suggestions, feel free to reachout to me!