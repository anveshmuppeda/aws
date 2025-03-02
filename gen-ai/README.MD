# Generative AI (Gen-AI)

## What is Generative AI?
- **Generative AI (Gen-AI)** is a type of artificial intelligence focused on **creating new content** — like text, images, music, code, or videos — by learning patterns from the data it was trained on.
- It doesn’t just recognize existing data; it **generates something new** that mimics what it has learned.

## Examples of Generative AI tasks:
- **Text:** Writing stories, answering questions, translating languages.
- **Images:** Creating realistic pictures or artwork.
- **Audio:** Composing music or generating speech.
- **Code:** Writing or debugging programming code.
- **Video:** Producing or editing videos.

---

# Foundation Models

## What are Foundation Models?
- **Foundation Models** are large AI models trained on massive, diverse datasets — including text, images, and audio.
- These models act as a **base** or **starting point** for more specific AI applications.
- Training Foundation Models is costly and requires powerful computing resources — often costing **millions of dollars**.

## Companies developing Foundation Models:
- **OpenAI** (GPT-4, DALL·E)
- **Google** (Gemini, BERT)
- **Meta (Facebook)** (LLaMA)
- **Amazon** (Titan)
- **Anthropic** (Claude)

## Open-source vs. Commercial models:
- **Open-source models:** Free to use and modify (e.g., Meta's LLaMA, Google's BERT).
- **Commercial models:** Require a license or subscription (e.g., OpenAI's GPT-4, Anthropic's Claude).

---

# Large Language Models (LLMs)

## What are LLMs?
- **Large Language Models (LLMs)** are a specific type of **Foundation Model** focused entirely on understanding and generating text.
- They are trained on massive amounts of text data — books, articles, websites — and learn the relationships between words to produce human-like text.

## Key features of LLMs:
- **Massive scale:** Trained on billions of parameters (the "knobs" AI adjusts to learn).
- **Language tasks:** Can handle a wide range of language-related activities, including:
  - **Translation** (converting text from one language to another)
  - **Summarization** (condensing long content)
  - **Question answering**
  - **Content creation**

## How do LLMs generate text?
1. **Prompt:** The user gives an input (like a question or a sentence).
2. **Prediction:** The model predicts the most likely next word based on learned patterns.
3. **Selection:** It picks a word — not always the most obvious one — to create natural-sounding text.

### Example:
**Prompt:** "After the rain, the streets were..."

The LLM might consider several options:
- **wet** (40% probability)
- **flooded** (25%)
- **slippery** (15%)
- **empty** (10%)

It chooses one word randomly but weighted by these probabilities — making the output feel creative and varied.

---

# Foundation Models vs. LLMs: What’s the Difference?

| **Foundation Models**          | **LLMs (Large Language Models)**     |
|-------------------------------|-------------------------------------|
| Broad AI models trained on diverse data (text, images, audio, etc.). | A type of Foundation Model focused on text and language tasks. |
| Can generate text, images, audio, video, or code.                   | Specializes in text generation and understanding.              |
| Examples: GPT-4, DALL·E, Gemini.                                   | Examples: GPT-4, BERT, LLaMA.                                 |
| Used to build AI tools for many domains.                            | Used for chatbots, translators, and content creators.          |

In short:
- **All LLMs are Foundation Models** because they’re built on large datasets.
- **Not all Foundation Models are LLMs** — some create images (DALL·E) or audio (Whisper) instead of text.

---  

# Amazon Bedrock

## What is Amazon Bedrock?
- **Amazon Bedrock** helps you build **Generative AI (Gen-AI)** applications on **AWS**.
- It’s a **fully-managed service** — no need to set up or manage servers.
- You stay in **control of your data** — your data isn’t used to train the foundation models.
- **Pay-per-use** — you only pay for what you use.
- Provides **unified APIs** — simple access to multiple AI models.
- Comes with ready-to-use features like:
  - **RAG** (Retrieval-Augmented Generation) — pulls in real-time data to enhance AI responses.
  - **LLM Agents** — AI agents that can perform tasks and solve problems.
- Built-in support for **Security, Privacy, Governance,** and **Responsible AI** practices.

---

## Foundation Models in Amazon Bedrock
- You get access to a variety of **Foundation Models (FMs)** from different providers.
- Amazon Bedrock makes a **private copy** of the FM just for you, so you can **fine-tune** it with your own data.
- **Your data stays private** — it’s not used to train the original foundation models.

---

## Choosing the Right Foundation Model
When picking a model, consider:
- **Model types** — text, images, or both (multimodal models).
- **Performance needs** — speed, accuracy.
- **Customization** — how much you want to fine-tune.
- **Model size** — larger models might be more powerful but cost more.
- **Inference options** — how the AI generates results.
- **Compliance** — if you need specific security or privacy standards.
- **Context windows** — how much information the model can process at once.
- **Latency** — how fast the model responds.

---

## Amazon Titan
- **Amazon Titan** is AWS’s own set of **high-performing Foundation Models**.
- Offers models for:
  - **Text generation**
  - **Image generation**
  - **Multimodal tasks** (using both text and images)
- **Fully-managed APIs** — simple to use.
- Can be **customized with your data** to better fit your needs.
- **Smaller models** are available too — they are more cost-effective and faster for simpler tasks.

---

# Fine-Tuning Models in Amazon Bedrock

## What is Fine-Tuning in Amazon Bedrock?
- **Fine-tuning** means **adapting a Foundation Model (FM)** by training it with **your own data** to make it better at specific tasks.
- You don’t change the original model — instead, Bedrock makes a **copy just for you** and adjusts it using your data.

## How Fine-Tuning Works
1. **Training data:**
   - Must be in a **specific format** (prompt-response pairs for instruction-based fine-tuning).
   - Needs to be stored in **Amazon S3** (AWS’s cloud storage service).
2. **Provisioned Throughput:**
   - To use your fine-tuned model, you must enable **Provisioned Throughput** — a dedicated way to get consistent, fast responses from your AI.
3. **Model compatibility:**
   - **Not all foundation models can be fine-tuned** — you need to check which models support this.

---

## Types of Fine-Tuning

### 1. **Instruction-based Fine-Tuning**
- Helps a model get better at **specific tasks** by training it with **labeled data** — examples that show the correct response to a given prompt.
- Useful when you want your AI to learn:
  - **Industry-specific language** (like medical terms or legal jargon)
  - A particular style or tone (e.g., friendly customer support vs. formal business writing)

### Example:
- **Prompt:** “What’s the return policy?”
- **Response:** “You can return items within 30 days with a receipt.”

You train the model by giving it lots of these pairs so it learns how to respond correctly.

---

### 2. **Continued Pre-Training (Domain Adaptation)**
- Extends a model’s knowledge using **unlabeled data** — this helps the model get smarter about a particular topic.
- Ideal for making the model an **expert in a field** by feeding it industry-specific documents.
- Great for:
  - Adding **specialized knowledge** (like giving it all your company’s internal guides)
  - Keeping it **up-to-date** with new data over time

### Example:
- Feeding the AI your company’s entire **AWS documentation** so it becomes an AWS specialist.

---

## Messaging in Fine-Tuning

### **Single-Turn Messaging**
- Used for tasks where the AI only needs **one interaction** to respond.
- The data format includes:
  - **system** (optional): Background info for the AI.
  - **messages**: A list of messages.
    - **role**: Either “user” or “assistant.”
    - **content**: The text for each message.

### Example:
- **User:** “What’s the weather?”
- **Assistant:** “It’s sunny.”

---

### **Multi-Turn Messaging**
- Used for **conversations** — back-and-forth exchanges between users and AI.
- Helpful for training **chatbots** or virtual assistants.
- Data must alternate between the **user** and **assistant** roles.

### Example:
- **User:** “What are your store hours?”
- **Assistant:** “We are open 9 AM to 5 PM.”
- **User:** “Are you open on weekends?”
- **Assistant:** “Yes, from 10 AM to 4 PM.”

---

## Key Points About Fine-Tuning
- **Cost:** Fine-tuning and running custom models can be expensive — you’ll need **Provisioned Throughput** for consistent performance.
- **Simplicity:** **Instruction-based fine-tuning** is usually **cheaper** than continued pre-training since it requires less data and computing power.
- **Expertise:** You may need **machine learning engineers** to prepare data, train, and evaluate the model.

---

## Transfer Learning vs. Fine-Tuning
- **Transfer Learning** is the broader idea of using a **pre-trained model** and tweaking it for a new, related task.
- **Fine-Tuning** is a **specific type of transfer learning** — adapting a model with new data.

---

## Use Cases for Fine-Tuning
- **Chatbots with personality:** Adjust AI to match your brand’s tone — friendly, professional, or humorous.
- **Up-to-date models:** Train the AI with the latest info — like recent company policies.
- **Exclusive data:** Use private data (customer service logs, emails) so the AI knows your business.
- **Specialized tasks:** Focus AI on tasks like sorting emails or verifying information.

---

### 1. **Automatic Evaluation**

- **What It Is:**  
  The system automatically tests your AI model without needing humans to review every output.

- **How It Works:**  
  - **Built-In Task Types:**  
    It comes with pre-defined tasks like:
    - **Text Summarization:** Condensing long pieces of text.
    - **Question & Answer:** Responding to questions.
    - **Text Classification:** Sorting text into categories.
    - **Open-Ended Text Generation:** Producing creative or varied text.
    
  - **Datasets:**  
    You can either provide your own dataset of prompts or use one that Amazon Bedrock offers. These datasets are collections of examples that help measure how well the model performs.

- **Outcome:**  
  The system then automatically calculates scores using various metrics (which we’ll detail later) to check for quality control.

---

### 2. **Benchmark Datasets**

- **What They Are:**  
  These are specially curated sets of data designed to test different aspects of language models.

- **Why They’re Important:**  
  - They cover a wide range of topics, complexity levels, and language phenomena.
  - They help measure key aspects like accuracy, speed, and efficiency.
  - Some benchmark datasets are designed to quickly highlight if a model might be biased or discriminatory.

- **Customization:**  
  You can also create your own benchmark dataset that is tailored to your specific business needs.

---

### 3. **Human Evaluation**

- **What It Is:**  
  Instead of relying solely on automatic scores, real people evaluate the model’s outputs.

- **Who Can Evaluate:**  
  - Your company’s employees.
  - Subject-Matter Experts (SMEs) who understand the context.
  
- **How It’s Done:**  
  - **Define Metrics:** You decide what makes an output “good” (e.g., clarity, correctness).
  - **Evaluation Methods:** This can be as simple as giving a thumbs up or down, ranking outputs, or using more detailed criteria.
  - **Task Types:** You can choose the same built-in tasks as automatic evaluation, or even create a custom task if needed.

---

### 4. **Automated Metrics**

These metrics are calculated by the system to quantify how well the model performs:

- **ROUGE:**  
  - **Purpose:** Mainly for summarization or translation.
  - **How It Works:**  
    - **ROUGE-N:** Counts matching groups of words (n-grams) between the generated text and a reference text.
    - **ROUGE-L:** Looks for the longest sequence of words that appears in both texts.

- **BLEU:**  
  - **Purpose:** Typically used to evaluate translation quality.
  - **How It Works:**  
    - It compares the generated text with one or more reference texts, considering both the number of matching words and whether the text is too short.

- **BERTScore:**  
  - **Purpose:** Evaluates semantic similarity.
  - **How It Works:**  
    - Uses a pre-trained BERT model to generate vector representations (embeddings) for both texts and then compares them using cosine similarity, capturing nuances beyond just word matching.

- **Perplexity:**  
  - **Purpose:** Measures how well the model predicts the next word in a sentence.
  - **How It Works:**  
    - Lower perplexity indicates that the model is better at predicting what comes next, which usually means better language understanding.

---

### 5. **Business Metrics**

In addition to technical performance, models are also evaluated on how they impact your business. Key business metrics include:

- **User Satisfaction:**  
  - **What It Measures:**  
    - How happy your users are with the model’s responses (e.g., via surveys or feedback).

- **Average Revenue Per User (ARPU):**  
  - **What It Measures:**  
    - The average income generated from each user, which helps see the financial impact of the AI app.

- **Cross-Domain Performance:**  
  - **What It Measures:**  
    - How well the model performs across various types of tasks or industries. For example, an ecommerce platform might need the model to handle product descriptions, customer queries, and recommendations all at once.

- **Conversion Rate:**  
  - **What It Measures:**  
    - How often the model’s output leads to a desired action (e.g., a purchase), which is critical for sales and marketing applications.

- **Efficiency:**  
  - **What It Measures:**  
    - How efficiently the model runs in terms of computation and resource use. This could be important for reducing operational costs or improving performance on production systems.

---

**In Summary:**  
Amazon Bedrock evaluates a model using two main methods: automatic evaluation with built-in datasets and tasks, and human evaluation by experts. It uses a mix of technical metrics (like ROUGE, BLEU, BERTScore, and perplexity) to measure quality, and business metrics (such as user satisfaction, ARPU, cross-domain performance, conversion rate, and efficiency) to ensure the model brings real value to your organization.


---  

### What is RAG (Retrieval-Augmented Generation)?

- **RAG Explained:**  
  RAG lets your AI model (a foundation model) look up and use information that isn't part of its original training data. Think of it as giving the model the ability to "google" for real-time data.

- **How It Works:**  
  Amazon Bedrock automatically creates "vector embeddings" (a way to represent your data numerically) from your external data and stores them in a database. When the model needs fresh or specific information, it can quickly search this database to find what it needs.

---

### Types of Databases for RAG (Vector Databases)

These are different kinds of databases where the vector embeddings (numerical representations of your data) can be stored and searched:

- **Amazon OpenSearch Service:**  
  A search and analytics database that can handle millions of embeddings, making it great for real-time similarity searches.

- **Amazon DocumentDB (with MongoDB compatibility):**  
  A NoSQL database that supports fast similarity queries and storing large amounts of vector data.

- **Amazon Aurora:**  
  A relational database developed by AWS, designed for high performance.

- **Amazon RDS for PostgreSQL:**  
  An open-source relational database that can also be used for similarity searches.

- **Amazon Neptune:**  
  A graph database, useful for data that is best represented as a network or relationships.

---

### Data Sources for RAG

These are the places where your real-time or updated data can come from:

- **Amazon S3:** Cloud storage for files and data.
- **Confluence:** A collaboration tool often used for documentation.
- **Microsoft SharePoint:** A platform for sharing and managing documents.
- **Salesforce:** A customer relationship management tool that stores business data.
- **Web Pages:** Your website, social media feeds, or any online content.
- **Others:** More sources may be added over time.

---

### Use Cases for RAG in Amazon Bedrock

By combining RAG with these external data sources, you can build powerful applications such as:

- **Customer Service Chatbot:**  
  - **Knowledge Base:** Stores product details, features, troubleshooting guides, and FAQs.
  - **How It Helps:** The chatbot can quickly retrieve relevant information to answer customer queries accurately.

- **Legal Research and Analysis:**  
  - **Knowledge Base:** Contains laws, regulations, case precedents, and legal opinions.
  - **How It Helps:** A legal chatbot can provide accurate and timely legal information for specific queries.

- **Healthcare Question-Answering:**  
  - **Knowledge Base:** Includes clinical guidelines, research papers, disease information, and treatment protocols.
  - **How It Helps:** A healthcare chatbot can answer complex medical questions using up-to-date clinical data.

---

**In Summary:**  
Amazon Bedrock uses RAG to let AI models tap into external, real-time data sources. It creates vector embeddings from your data and stores them in various types of databases. This setup is useful for building chatbots and other applications that need to access up-to-date information—whether for customer service, legal research, or healthcare queries.

---