### Generative AI (Gen-AI)

**Q1: What is Generative AI?**  
**A:** Generative AI (Gen-AI) is a type of artificial intelligence that creates new content—such as text, images, music, code, or videos—by learning patterns from the data it was trained on. It doesn’t just recognize existing data; it generates new content that mimics the patterns.

**Q2: Can you list some examples of tasks that Generative AI can perform?**  
**A:**  
- **Text:** Writing stories, answering questions, translating languages.  
- **Images:** Creating realistic pictures or artwork.  
- **Audio:** Composing music or generating speech.  
- **Code:** Writing or debugging programming code.  
- **Video:** Producing or editing videos.

---

### Foundation Models

**Q3: What are Foundation Models?**  
**A:** Foundation Models are large AI models trained on massive, diverse datasets (text, images, audio, etc.). They serve as a base for building more specialized AI applications and require significant computational resources and cost to train.

**Q4: Which companies are known for developing Foundation Models?**  
**A:**  
- OpenAI (e.g., GPT-4, DALL·E)  
- Google (e.g., Gemini, BERT)  
- Meta (e.g., LLaMA)  
- Amazon (e.g., Titan)  
- Anthropic (e.g., Claude)

**Q5: What is the main difference between open-source and commercial foundation models?**  
**A:**  
- **Open-source models:** Free to use and modify (e.g., Meta's LLaMA, Google's BERT).  
- **Commercial models:** Require a license or subscription (e.g., OpenAI's GPT-4, Anthropic's Claude).

---

### Large Language Models (LLMs)

**Q6: What are Large Language Models (LLMs)?**  
**A:** LLMs are a type of Foundation Model focused entirely on understanding and generating text. They are trained on massive amounts of text data and learn relationships between words to produce human-like text.

**Q7: What are some key features of LLMs?**  
**A:**  
- **Massive scale:** They have billions of parameters.  
- **Versatility in language tasks:** Capable of translation, summarization, question answering, and content creation.

**Q8: How do LLMs generate text?**  
**A:** They work by:  
1. Receiving a **prompt** (an input from the user).  
2. **Predicting** the most likely next word based on learned patterns.  
3. **Selecting** a word (based on probability weighting) to form natural-sounding text.

**Q9: What is the difference between Foundation Models and LLMs?**  
**A:**  
- **Foundation Models:** Broad models trained on diverse data types (text, images, audio, etc.) and can be adapted for various tasks.  
- **LLMs:** A subset of Foundation Models that specialize in language tasks only.

---

### Amazon Bedrock

**Q10: What is Amazon Bedrock?**  
**A:** Amazon Bedrock is a fully-managed service on AWS that helps you build Generative AI applications. It gives you access to various Foundation Models via unified APIs, handles infrastructure management, and ensures your data remains private.

**Q11: How does Amazon Bedrock ensure data privacy?**  
**A:** Bedrock creates a private copy of the foundation model for you, so your data is used only for fine-tuning and isn’t shared with or used to train the original model.

**Q12: What are some key features provided by Amazon Bedrock?**  
**A:**  
- Fully-managed service (no server management).  
- Pay-per-use pricing model.  
- Unified APIs to access multiple models.  
- Built-in features like RAG (Retrieval-Augmented Generation) and LLM Agents.  
- Support for Security, Privacy, Governance, and Responsible AI practices.

**Q13: What is Amazon Titan?**  
**A:** Amazon Titan is AWS’s own suite of high-performing Foundation Models. It offers models for text generation, image generation, and multimodal tasks and can be customized with your data via fully-managed APIs.

---

### Fine-Tuning Models in Amazon Bedrock

**Q14: What does fine-tuning mean in the context of Amazon Bedrock?**  
**A:** Fine-tuning is the process of adapting a pre-trained Foundation Model by training it further with your own data to improve performance on specific tasks. Bedrock creates a private copy of the model for this purpose.

**Q15: What are the key steps in fine-tuning a model on Amazon Bedrock?**  
**A:**  
1. Prepare training data in a specific format (e.g., prompt-response pairs) and store it in Amazon S3.  
2. Enable Provisioned Throughput for consistent, fast responses.  
3. Verify that the model you choose supports fine-tuning.

**Q16: What are the two main types of fine-tuning?**  
**A:**  
- **Instruction-based Fine-Tuning:** Uses labeled data (prompt-response pairs) to help the model learn specific tasks.  
- **Continued Pre-Training (Domain Adaptation):** Uses unlabeled data to extend the model’s knowledge in a specific domain.

**Q17: What is the difference between single-turn and multi-turn messaging in fine-tuning?**  
**A:**  
- **Single-Turn Messaging:** Involves one interaction (user prompt and single response).  
- **Multi-Turn Messaging:** Involves back-and-forth conversation, ideal for training chatbots or virtual assistants.

**Q18: What is the difference between transfer learning and fine-tuning?**  
**A:**  
- **Transfer Learning:** The broader approach of using a pre-trained model as a starting point for a related task.  
- **Fine-Tuning:** A specific form of transfer learning where the model is further trained on new data to adapt it for a specific task.

**Q19: Can you provide some examples of use cases for fine-tuning?**  
**A:**  
- **Chatbots with personality:** Adjust the AI’s tone to match your brand.  
- **Up-to-date models:** Train the AI with the latest company information.  
- **Exclusive data:** Use private data (like customer service logs) to tailor the model.  
- **Specialized tasks:** Focus the AI on specific tasks, such as sorting emails or verifying information.

---

### Evaluation of Models in Amazon Bedrock

**Q20: What is automatic evaluation in Amazon Bedrock?**  
**A:** Automatic evaluation is when the system tests your model using pre-defined tasks (e.g., text summarization, Q&A) and automatically calculates scores to assess performance.

**Q21: What are benchmark datasets, and why are they important?**  
**A:** Benchmark datasets are curated collections of data designed to evaluate different aspects of language models, such as accuracy, speed, and efficiency. They help quickly identify issues like bias or discrimination and can be customized to your business needs.

**Q22: What does human evaluation involve?**  
**A:** Human evaluation involves having real people (employees or subject-matter experts) review and rate the model’s outputs based on defined criteria like clarity and correctness. It can use methods like thumbs up/down or ranking.

**Q23: What are some automated metrics used to evaluate a model?**  
**A:**  
- **ROUGE:** Measures matching n-grams and longest common subsequences, used for summarization/translation tasks.  
- **BLEU:** Evaluates translation quality by comparing generated text to reference texts.  
- **BERTScore:** Assesses semantic similarity using vector embeddings from a BERT model.  
- **Perplexity:** Measures how well the model predicts the next word (lower is better).

**Q24: What business metrics are used to evaluate a model’s impact?**  
**A:**  
- **User Satisfaction:** Feedback on how users perceive the model’s responses.  
- **Average Revenue Per User (ARPU):** The average income generated per user.  
- **Cross-Domain Performance:** How well the model handles various tasks or industries.  
- **Conversion Rate:** How often outputs lead to desired actions (e.g., purchases).  
- **Efficiency:** How efficiently the model uses computational resources.

---

### Retrieval-Augmented Generation (RAG) & Knowledge Base

**Q25: What is Retrieval-Augmented Generation (RAG)?**  
**A:** RAG is a technique that allows an AI model to reference and use external, real-time data (from your own sources) by creating vector embeddings of that data and storing them in a database.

**Q26: What types of databases are used as RAG vector databases in Amazon Bedrock?**  
**A:**  
- **Amazon OpenSearch Service:** For real-time similarity queries and fast nearest-neighbor search.  
- **Amazon DocumentDB (with MongoDB compatibility):** A NoSQL database for storing vector embeddings.  
- **Amazon Aurora:** A high-performance, proprietary relational database.  
- **Amazon RDS for PostgreSQL:** An open-source relational database with similarity search.  
- **Amazon Neptune:** A graph database suitable for representing relationships.

**Q27: What are some common data sources used for RAG in Amazon Bedrock?**  
**A:**  
- Amazon S3  
- Confluence  
- Microsoft SharePoint  
- Salesforce  
- Web pages (e.g., your website, social media feeds)  
- And more sources as they get added over time.

**Q28: What are some practical use cases for RAG in Amazon Bedrock?**  
**A:**  
- **Customer Service Chatbot:** Uses a knowledge base (product details, FAQs) to answer queries.  
- **Legal Research and Analysis:** Retrieves laws, regulations, and legal precedents for legal queries.  
- **Healthcare Question-Answering:** Accesses clinical guidelines and research to answer medical questions.
