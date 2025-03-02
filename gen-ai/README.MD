# Generative AI  

This document provides an overview of key concepts in Generative AI, Foundation Models, Large Language Models (LLMs), and Amazon Bedrock. It also covers evaluation techniques and the use of Retrieval-Augmented Generation (RAG) in Bedrock.

## Table of Contents

- [Generative AI (Gen-AI)](#generative-ai-gen-ai)
  - [What is Generative AI?](#what-is-generative-ai)
  - [Examples of Generative AI Tasks](#examples-of-generative-ai-tasks)
- [Foundation Models](#foundation-models)
  - [What are Foundation Models?](#what-are-foundation-models)
  - [Companies Developing Foundation Models](#companies-developing-foundation-models)
  - [Open-Source vs. Commercial Models](#open-source-vs-commercial-models)
- [Large Language Models (LLMs)](#large-language-models-llms)
  - [What are LLMs?](#what-are-llms)
  - [Key Features of LLMs](#key-features-of-llms)
  - [How LLMs Generate Text](#how-llms-generate-text)
- [Foundation Models vs. LLMs](#foundation-models-vs-llms)
- [Amazon Bedrock](#amazon-bedrock)
  - [What is Amazon Bedrock?](#what-is-amazon-bedrock)
  - [Foundation Models in Amazon Bedrock](#foundation-models-in-amazon-bedrock)
  - [Choosing the Right Foundation Model](#choosing-the-right-foundation-model)
  - [Amazon Titan](#amazon-titan)
- [Fine-Tuning Models in Amazon Bedrock](#fine-tuning-models-in-amazon-bedrock)
  - [What is Fine-Tuning in Amazon Bedrock?](#what-is-fine-tuning-in-amazon-bedrock)
  - [How Fine-Tuning Works](#how-fine-tuning-works)
  - [Types of Fine-Tuning](#types-of-fine-tuning)
    - [Instruction-based Fine-Tuning](#instruction-based-fine-tuning)
    - [Continued Pre-Training (Domain Adaptation)](#continued-pre-training-domain-adaptation)
  - [Messaging in Fine-Tuning](#messaging-in-fine-tuning)
    - [Single-Turn Messaging](#single-turn-messaging)
    - [Multi-Turn Messaging](#multi-turn-messaging)
  - [Key Points About Fine-Tuning](#key-points-about-fine-tuning)
  - [Transfer Learning vs. Fine-Tuning](#transfer-learning-vs-fine-tuning)
  - [Use Cases for Fine-Tuning](#use-cases-for-fine-tuning)
- [Evaluation of Models in Amazon Bedrock](#evaluation-of-models-in-amazon-bedrock)
  - [Automatic Evaluation](#automatic-evaluation)
  - [Benchmark Datasets](#benchmark-datasets)
  - [Human Evaluation](#human-evaluation)
  - [Automated Metrics](#automated-metrics)
  - [Business Metrics](#business-metrics)
- [Retrieval-Augmented Generation (RAG) & Knowledge Base](#retrieval-augmented-generation-rag--knowledge-base)
  - [What is RAG?](#what-is-rag)
  - [RAG Vector Databases – Types](#rag-vector-databases--types)
  - [RAG Data Sources](#rag-data-sources)
  - [RAG Use Cases](#rag-use-cases)

---

## Generative AI (Gen-AI)

### What is Generative AI?
- **Generative AI (Gen-AI)** is a type of artificial intelligence focused on **creating new content**—like text, images, music, code, or videos—by learning patterns from the data it was trained on.
- It doesn’t just recognize existing data; it **generates something new** that mimics what it has learned.

### Examples of Generative AI Tasks
- **Text:** Writing stories, answering questions, translating languages.
- **Images:** Creating realistic pictures or artwork.
- **Audio:** Composing music or generating speech.
- **Code:** Writing or debugging programming code.
- **Video:** Producing or editing videos.

---

## Foundation Models

### What are Foundation Models?
- **Foundation Models** are large AI models trained on massive, diverse datasets—such as text, images, and audio.
- They act as a **base** or **starting point** for developing more specific AI applications.
- Training these models is costly and requires powerful computing resources—often costing **millions of dollars**.

### Companies Developing Foundation Models
- **OpenAI** (GPT-4, DALL·E)
- **Google** (Gemini, BERT)
- **Meta (Facebook)** (LLaMA)
- **Amazon** (Titan)
- **Anthropic** (Claude)

### Open-Source vs. Commercial Models
- **Open-source models:** Free to use and modify (e.g., Meta's LLaMA, Google's BERT).
- **Commercial models:** Require a license or subscription (e.g., OpenAI's GPT-4, Anthropic's Claude).

---

## Large Language Models (LLMs)

### What are LLMs?
- **Large Language Models (LLMs)** are a specific type of **Foundation Model** focused entirely on understanding and generating text.
- They are trained on massive amounts of text data—books, articles, websites—and learn relationships between words to produce human-like text.

### Key Features of LLMs
- **Massive scale:** Trained on billions of parameters (the "knobs" the AI adjusts to learn).
- **Language tasks:** Can perform translation, summarization, question answering, and content creation.

### How LLMs Generate Text
1. **Prompt:** The user provides an input (e.g., a question or sentence).
2. **Prediction:** The model predicts the most likely next word based on learned patterns.
3. **Selection:** It randomly chooses a word, weighted by probability, to form natural-sounding text.

**Example:**

*Prompt:* "After the rain, the streets were..."

Possible completions might be:
- **wet** (40% probability)
- **flooded** (25%)
- **slippery** (15%)
- **empty** (10%)

---

## Foundation Models vs. LLMs: What’s the Difference?

| **Foundation Models**                                                      | **LLMs (Large Language Models)**                                      |
|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| Broad AI models trained on diverse data (text, images, audio, etc.).        | A type of Foundation Model focused solely on text and language tasks. |
| Can generate text, images, audio, video, or code.                          | Specializes in text generation and understanding.                   |
| Examples: GPT-4, DALL·E, Gemini.                                           | Examples: GPT-4, BERT, LLaMA.                                          |
| Used to build AI tools for various domains.                               | Used for chatbots, translators, and content creation.                |

- **All LLMs are Foundation Models** because they’re built on large datasets.
- **Not all Foundation Models are LLMs**—some generate images (like DALL·E) or audio (like Whisper) instead of text.

---

## Amazon Bedrock

### What is Amazon Bedrock?
- **Amazon Bedrock** helps you build **Generative AI (Gen-AI)** applications on **AWS**.
- It’s a **fully-managed service**—you don’t need to set up or manage servers.
- **Data Privacy:** Your data remains private and isn’t used to train the original foundation models.
- **Pay-per-use:** You only pay for what you use.
- **Unified APIs:** Offers simple access to multiple AI models.
- **Ready-to-use Features:**  
  - **RAG** (Retrieval-Augmented Generation) for real-time data integration.
  - **LLM Agents** that perform tasks and solve problems.
- Built-in support for **Security, Privacy, Governance,** and **Responsible AI** practices.

### Foundation Models in Amazon Bedrock
- Provides access to various **Foundation Models (FMs)** from different providers.
- Amazon Bedrock creates a **private copy** of the FM for you, which you can then **fine-tune** with your own data.
- **Data Privacy:** Your data stays private—it isn’t used to train the original FM.

### Choosing the Right Foundation Model
Consider the following factors:
- **Model Types:** Text, images, or multimodal (both).
- **Performance Needs:** Speed and accuracy.
- **Customization:** Degree of fine-tuning required.
- **Model Size:** Larger models may be more powerful but cost more.
- **Inference Options:** How the AI generates results.
- **Compliance:** Security or privacy standards.
- **Context Windows:** How much information can be processed at once.
- **Latency:** How fast the model responds.

### Amazon Titan
- **Amazon Titan** is AWS’s own set of **high-performing Foundation Models**.
- Offers models for:
  - **Text Generation**
  - **Image Generation**
  - **Multimodal Tasks** (text and images)
- Provides **fully-managed APIs** that are easy to use.
- **Customization:** Titan models can be fine-tuned with your data.
- Smaller models are also available for cost-effectiveness and faster performance on simpler tasks.

---

## Fine-Tuning Models in Amazon Bedrock

### What is Fine-Tuning in Amazon Bedrock?
- **Fine-tuning** adapts a Foundation Model (FM) by training it with **your own data** to improve performance on specific tasks.
- The original model remains unchanged; Bedrock creates a **private copy** for customization.

### How Fine-Tuning Works
1. **Training Data:**  
   - Must be in a **specific format** (e.g., prompt-response pairs).
   - Stored in **Amazon S3**.
2. **Provisioned Throughput:**  
   - Enable this feature for consistent, fast responses.
3. **Model Compatibility:**  
   - Not all FMs support fine-tuning, so verify compatibility.

### Types of Fine-Tuning

#### Instruction-based Fine-Tuning
- Trains the model using **labeled data** (prompt-response pairs) for specific tasks.
- **Use Case:** Learning industry-specific language or a desired tone.

**Example:**  
- **Prompt:** “What’s the return policy?”  
- **Response:** “You can return items within 30 days with a receipt.”

#### Continued Pre-Training (Domain Adaptation)
- Uses **unlabeled data** to expand the model’s knowledge in a particular domain.
- **Use Case:** Feeding the model industry-specific documents to make it an expert.

**Example:**  
- Feeding the model your company’s AWS documentation so it becomes an AWS specialist.

### Messaging in Fine-Tuning

#### Single-Turn Messaging
- For tasks needing **one interaction**.
- Data format includes:
  - **System (optional):** Background info.
  - **Messages:** List with roles (user/assistant) and content.

**Example:**  
- **User:** “What’s the weather?”  
- **Assistant:** “It’s sunny.”

#### Multi-Turn Messaging
- For **conversational tasks** with back-and-forth interactions.
- Useful for training chatbots.

**Example:**  
- **User:** “What are your store hours?”  
- **Assistant:** “We are open 9 AM to 5 PM.”  
- **User:** “Are you open on weekends?”  
- **Assistant:** “Yes, from 10 AM to 4 PM.”

### Key Points About Fine-Tuning
- **Cost:** Fine-tuning can be expensive due to the need for consistent performance (Provisioned Throughput).
- **Simplicity:** Instruction-based fine-tuning is usually cheaper and requires less data.
- **Expertise:** You may need machine learning engineers to prepare data, train, and evaluate the model.

### Transfer Learning vs. Fine-Tuning
- **Transfer Learning:** Using a pre-trained model as a starting point for a related task.
- **Fine-Tuning:** A specific form of transfer learning where the model is adapted with new data.

### Use Cases for Fine-Tuning
- **Chatbots with Personality:** Tailor the tone to match your brand.
- **Up-to-Date Models:** Keep the model current with the latest information.
- **Exclusive Data:** Train with private data like customer service logs.
- **Specialized Tasks:** Focus the model on tasks like sorting emails or verifying information.

---

## Evaluation of Models in Amazon Bedrock

### Automatic Evaluation
- **What It Is:**  
  The system automatically tests your model using pre-defined tasks.
- **Built-In Task Types:**  
  - Text Summarization
  - Question & Answer
  - Text Classification
  - Open-Ended Text Generation
- **Datasets:**  
  Use your own or built-in curated prompt datasets.
- **Outcome:**  
  The system calculates scores automatically to assess quality.

### Benchmark Datasets
- **What They Are:**  
  Curated datasets designed specifically for evaluating language models.
- **Purpose:**  
  - Measure accuracy, speed, and efficiency.
  - Detect biases and discrimination quickly.
- **Customization:**  
  You can also create benchmark datasets specific to your business needs.

### Human Evaluation
- **What It Is:**  
  Real people (employees or subject-matter experts) review and rate the model’s outputs.
- **Process:**  
  - Define evaluation metrics (e.g., clarity, correctness).
  - Use methods like thumbs up/down or ranking.
  - Option to use built-in tasks or custom tasks.

### Automated Metrics
- **ROUGE:**  
  - **Purpose:** Evaluates summarization and translation.
  - **Methods:**  
    - ROUGE-N: Counts matching n-grams.
    - ROUGE-L: Longest common subsequence.
- **BLEU:**  
  - **Purpose:** Evaluates translation quality.
  - **Methods:** Considers precision and penalizes overly short outputs.
- **BERTScore:**  
  - **Purpose:** Measures semantic similarity using BERT embeddings.
- **Perplexity:**  
  - **Purpose:** Measures how well the model predicts the next word (lower is better).

### Business Metrics
- **User Satisfaction:**  
  Gauges how happy users are with the responses.
- **Average Revenue Per User (ARPU):**  
  Measures the average revenue generated per user.
- **Cross-Domain Performance:**  
  Assesses the model’s performance across various tasks.
- **Conversion Rate:**  
  Tracks how often outputs lead to desired actions (e.g., purchases).
- **Efficiency:**  
  Evaluates computational and resource efficiency.

---

## Retrieval-Augmented Generation (RAG) & Knowledge Base

### What is RAG?
- **RAG Explained:**  
  RAG allows a foundation model to reference and incorporate external, real-time data—like having the model “google” for up-to-date information.
- **How It Works:**  
  Amazon Bedrock creates vector embeddings (numerical representations) from your external data and stores them in a database. The model then retrieves relevant information when needed.

### RAG Vector Databases – Types
- **Amazon OpenSearch Service:**  
  Search and analytics database ideal for real-time similarity queries and kNN search.
- **Amazon DocumentDB (with MongoDB compatibility):**  
  NoSQL database suitable for fast similarity queries.
- **Amazon Aurora:**  
  A high-performance, proprietary relational database on AWS.
- **Amazon RDS for PostgreSQL:**  
  An open-source relational database with similarity search capabilities.
- **Amazon Neptune:**  
  A graph database that is great for representing relationships.

### RAG Data Sources
- **Amazon S3:** Cloud storage for data files.
- **Confluence:** Collaboration tool for documentation.
- **Microsoft SharePoint:** Platform for managing documents.
- **Salesforce:** Customer relationship management system.
- **Web Pages:** Your website, social media feeds, etc.
- **Others:** Additional sources can be added over time.

### RAG – Use Cases in Amazon Bedrock
- **Customer Service Chatbot:**  
  - **Knowledge Base:** Stores product details, features, FAQs, etc.
  - **Benefit:** Enables the chatbot to retrieve and deliver accurate answers.
- **Legal Research and Analysis:**  
  - **Knowledge Base:** Contains laws, regulations, case precedents, and legal opinions.
  - **Benefit:** Helps the chatbot provide relevant legal information.
- **Healthcare Question-Answering:**  
  - **Knowledge Base:** Includes clinical guidelines, research, and disease information.
  - **Benefit:** Supports answering complex medical queries with up-to-date data.
