(Due to technical issues, the search service is temporarily unavailable.)

Here’s the updated document with **Key Exam Takeaways** added to each section and integration of the previous response’s content (Tokenization, Context Window, Embeddings, Guardrails, Agents, Pricing, etc.):

---

# Generative AI  

This document provides an overview of key concepts in Generative AI, Foundation Models, Large Language Models (LLMs), and Amazon Bedrock. It also covers evaluation techniques and the use of Retrieval-Augmented Generation (RAG) in Bedrock.

## Table of Contents  
- [Generative AI (Gen-AI)](#generative-ai-gen-ai)  
- [Foundation Models](#foundation-models)  
- [Large Language Models (LLMs)](#large-language-models-llms)  
- [Foundation Models vs. LLMs](#foundation-models-vs-llms)  
- [Amazon Bedrock](#amazon-bedrock)  
- [Fine-Tuning Models in Amazon Bedrock](#fine-tuning-models-in-amazon-bedrock)  
- [Evaluation of Models in Amazon Bedrock](#evaluation-of-models-in-amazon-bedrock)  
- [Retrieval-Augmented Generation (RAG) & Knowledge Base](#retrieval-augmented-generation-rag--knowledge-base)  
- [GenAI Core Concepts](#genai-core-concepts)  
- [Amazon Bedrock Advanced Features](#amazon-bedrock-advanced-features)  

---

## Generative AI (Gen-AI)  

### What is Generative AI?  
- **Generative AI (Gen-AI)** creates new content (text, images, audio) by learning patterns from training data.  
- **Key Exam Takeaway**: Gen-AI generates new content, unlike traditional AI that only recognizes patterns.  

### Examples of Generative AI Tasks  
- **Text**: Stories, translations, code.  
- **Images**: Art, realistic photos.  
- **Audio**: Music, speech.  
- **Key Exam Takeaway**: Gen-AI works across text, images, audio, and video.  

---

## Foundation Models  

### What are Foundation Models?  
- **Foundation Models (FMs)** are large models trained on diverse datasets (text, images, audio).  
- **Key Exam Takeaway**: FMs are the base for building specialized AI applications.  

### Companies Developing Foundation Models  
- OpenAI (GPT-4), Google (Gemini), Amazon (Titan), Meta (LLaMA).  
- **Key Exam Takeaway**: Commercial models (e.g., GPT-4) require licenses; open-source models (e.g., LLaMA) are free.  

---

## Large Language Models (LLMs)  

### What are LLMs?  
- **LLMs** are Foundation Models specialized in text generation/understanding.  
- **Key Exam Takeaway**: All LLMs are Foundation Models, but not all FMs are LLMs.  

### Key Features of LLMs  
- Massive scale (billions of parameters), language tasks (translation, summarization).  
- **Key Exam Takeaway**: LLMs predict the next word using probability.  

---

## Foundation Models vs. LLMs  

| **Foundation Models**       | **LLMs**                      |  
|------------------------------|-------------------------------|  
| Broad (text, images, audio)  | Text-only focus               |  
| Examples: DALL·E, GPT-4      | Examples: GPT-4, LLaMA        |  
| **Key Exam Takeaway**: LLMs are a subset of Foundation Models.  

---

## Amazon Bedrock  

### What is Amazon Bedrock?  
- Fully-managed service to build Gen-AI apps on AWS.  
- **Key Exam Takeaway**: Bedrock offers pay-per-use pricing and data privacy.  

### Foundation Models in Amazon Bedrock  
- Access models from AWS (Titan), Anthropic (Claude), etc.  
- **Key Exam Takeaway**: Bedrock creates private copies of FMs for fine-tuning.  

### Amazon Titan  
- AWS’s high-performing FMs for text, images, and multimodal tasks.  
- **Key Exam Takeaway**: Titan models can be fine-tuned with custom data.  

---

## Fine-Tuning Models in Amazon Bedrock  

### What is Fine-Tuning?  
- Adapting FMs with custom data for specific tasks.  
- **Key Exam Takeaway**: Instruction-based fine-tuning uses labeled data; domain adaptation uses unlabeled data.  

### Model Improvement Techniques (Cost Order)  
1. **Prompt Engineering** (no cost).  
2. **RAG** (external data lookup).  
3. **Fine-Tuning** (labeled data).  
4. **Domain Adaptation** (expensive).  
- **Key Exam Takeaway**: RAG is cheaper than fine-tuning.  

---

## Evaluation of Models in Amazon Bedrock  

### Automatic Evaluation  
- Tests models using tasks like summarization, Q&A.  
- **Key Exam Takeaway**: Use ROUGE for summarization, BLEU for translation.  

### Business Metrics  
- User satisfaction, conversion rates, ARPU.  
- **Key Exam Takeaway**: Track metrics like latency and token usage in CloudWatch.  

---

## Retrieval-Augmented Generation (RAG) & Knowledge Base  

### What is RAG?  
- Lets FMs pull real-time data from external sources.  
- **Key Exam Takeaway**: RAG reduces hallucinations by grounding responses in external data.  

### RAG Vector Databases  
- OpenSearch, Aurora, Neptune.  
- **Key Exam Takeaway**: Use OpenSearch for real-time similarity searches.  

---

## GenAI Core Concepts  

### Tokenization  
- Splits text into tokens (words or subwords).  
- **Key Exam Takeaway**: Subword tokenization handles rare/long words (e.g., "unhappiness" → "un" + "happiness").  

### Context Window  
- Number of tokens an LLM can process at once.  
- **Key Exam Takeaway**: Larger windows = more memory but higher compute costs.  

### Embeddings  
- Converts text/images to vectors (numbers).  
- **Key Exam Takeaway**: Similar words (e.g., "king" and "queen") have similar embeddings.  

---

## Amazon Bedrock Advanced Features  

### Guardrails  
- Filters harmful content and PII.  
- **Key Exam Takeaway**: Guardrails reduce hallucinations and enforce safety.  

### Agents  
- Perform multi-step tasks (e.g., booking flights).  
- **Key Exam Takeaway**: Agents use RAG to fetch real-time data.  

### Pricing  
- **On-Demand**: Pay per token.  
- **Batch**: Up to 50% discount for bulk jobs.  
- **Key Exam Takeaway**: Smaller models = lower costs.  

---
