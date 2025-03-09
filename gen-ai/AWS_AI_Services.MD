## **1. Why Use AWS AI Managed Services?**  
- **Pre-trained models**: Ready-to-use solutions for common tasks (no ML expertise needed).  
- **Scalability & Redundancy**: Runs across multiple AWS regions/AZs for high availability.  
- **Cost-Effective**: Pay-as-you-go (token-based) or **provisioned throughput** for predictable workloads.  
- **Optimized Hardware**: Uses GPUs/CPUs tailored for AI tasks.  

---

### **2. Core AWS AI Services**  
#### **Amazon Comprehend**  
- **What**: NLP service to analyze text (sentiment, entities, topics).  
- **Key Features**:  
  - **Custom Classification**: Organize docs into your own categories (e.g., classify support emails as "billing" or "technical").  
  - **Custom Entity Recognition**: Extract business-specific terms (e.g., policy numbers, product codes).  
- **Use Cases**: Analyze customer feedback, automate document tagging.  
- **Exam Tip**: Comprehend Medical detects PHI (Protected Health Information) in clinical text.  

#### **Amazon Translate**  
- **What**: Translates text between languages (supports 75+ languages).  
- **Use Cases**: Localize apps/websites, translate user reviews.  
- **Exam Tip**: Use **Active Custom Translation** to fine-tune translations for industry jargon.  

#### **Amazon Transcribe**  
- **What**: Converts speech to text (supports multi-language audio).  
- **Key Features**:  
  - **Redact PII**: Automatically remove sensitive info (e.g., credit card numbers).  
  - **Toxicity Detection**: Flag harmful speech (hate speech, threats).  
  - **Accuracy Boosters**:  
    - **Custom Vocabulary**: Add rare words (e.g., brand names).  
    - **Custom Language Model**: Train on domain-specific data (e.g., medical terms).  
- **Use Cases**: Transcribe call center recordings, generate subtitles.  

#### **Amazon Polly**  
- **What**: Converts text to lifelike speech.  
- **Key Features**:  
  - **Lexicons**: Control pronunciation (e.g., "AWS" → "Amazon Web Services").  
  - **SSML**: Add pauses/emphasis (e.g., `<break time="1s"/>`).  
- **Use Cases**: Voice assistants, audiobooks.  

---

### **3. Vision & Media Services**  
#### **Amazon Rekognition**  
- **What**: Analyzes images/videos for objects, faces, text.  
- **Key Features**:  
  - **Custom Labels**: Train models to detect custom objects (e.g., your logo).  
  - **Content Moderation**: Flag inappropriate content (integrates with **Amazon A2I** for human review).  
  - **Celebrity Recognition**: Identify famous people in media.  
- **Use Cases**: Social media moderation, sports analytics.  

#### **Amazon Textract**  
- **What**: Extracts text/data from scanned docs (PDFs, forms, tables).  
- **Use Cases**: Digitize invoices, process insurance claims.  
- **Exam Tip**: Handles **handwritten text** and structured tables.  

---

### **4. Conversational AI & Recommendations**  
#### **Amazon Lex**  
- **What**: Build chatbots (voice/text).  
- **Key Features**:  
  - **Intent Recognition**: Understands user goals (e.g., "Book a hotel").  
  - **Slots**: Collect parameters (e.g., "Check-in date: [slot]").  
  - **Integrates with Lambda**: Trigger backend logic.  
- **Use Cases**: Customer service bots, order tracking.  

#### **Amazon Personalize**  
- **What**: Real-time recommendations (like Amazon.com).  
- **Key Features**:  
  - **Recipes**: Pre-built algorithms for use cases (e.g., "USER_PERSONALIZATION" for product recs).  
  - **User Segmentation**: Group users by behavior.  
- **Use Cases**: E-commerce product suggestions, personalized marketing.  

---

### **5. Search & Human-in-the-Loop**  
#### **Amazon Kendra**  
- **What**: ML-powered document search.  
- **Key Features**:  
  - **Natural Language Queries**: "Find sales reports from Q2 2023."  
  - **Incremental Learning**: Improves results based on user feedback.  
- **Use Cases**: Enterprise knowledge bases, legal document search.  

#### **Amazon Mechanical Turk (MTurk)**  
- **What**: Crowdsource tasks to humans (data labeling, surveys).  
- **Use Cases**: Label training data for ML models.  
- **Exam Tip**: Integrates with **Amazon A2I** (human review of AI predictions).  

#### **Amazon Augmented AI (A2I)**  
- **What**: Adds human review to AI workflows.  
- **Use Cases**: Verify Rekognition’s content moderation, audit Transcribe outputs.  

---

### **6. Healthcare-Specific Services**  
#### **Amazon Transcribe Medical**  
- **What**: HIPAA-compliant speech-to-text for medical jargon.  
- **Use Cases**: Transcribe doctor-patient conversations, clinical notes.  

#### **Amazon Comprehend Medical**  
- **What**: Extracts medical terms (drugs, conditions) from text.  
- **Use Cases**: Analyze EHRs (Electronic Health Records), detect PHI.  

---

### **Exam Cheat Sheet**  
| **Service**               | **Key Use Case**                          | **Unique Feature**                     |  
|---------------------------|-------------------------------------------|----------------------------------------|  
| **Comprehend**             | Sentiment analysis, PHI detection         | Custom entity recognition              |  
| **Transcribe**             | Speech-to-text, call center analytics     | Toxicity detection + PII redaction     |  
| **Rekognition**            | Image moderation, celebrity recognition   | Custom Labels                          |  
| **Lex**                    | Chatbots                                  | Slot fulfillment + Lambda integration  |  
| **Personalize**            | Product recommendations                  | Pre-built "recipes"                    |  
| **Textract**               | Extract data from invoices/forms          | Handwritten text support               |  
| **Kendra**                 | Enterprise document search                | Natural language queries               |  
| **A2I**                    | Human review of AI outputs               | Integrates with Rekognition/Transcribe |  

---

### **Key Terms to Remember**  
- **PHI**: Protected Health Information (handled by Comprehend Medical).  
- **SSML**: Speech Synthesis Markup Language (used in Amazon Polly).  
- **Provisioned Throughput**: Guaranteed performance for steady AI workloads.  
- **Slot**: Parameter collected by chatbots (e.g., date, location).  