### **Core Machine Learning Concepts**
1. **Self-Supervised Learning**
   - Models use **unlabeled data** to generate their own labels (e.g., predicting the next word in a sentence).
   - Used by **Foundation Models (FMs)** like those in Amazon Bedrock.

2. **Supervised vs. Unsupervised Learning**
   - **Supervised**: Uses labeled data (input-output pairs). Example: Image classification.
   - **Unsupervised**: Finds patterns in unlabeled data. Example: Clustering news articles.
   - **Reinforcement Learning**: Models learn by maximizing rewards (e.g., game-playing AI).

3. **Model Customization in Amazon Bedrock**
   - **Provisioned Throughput**: Required for fine-tuning or continued pre-training of models.
   - **Continued Pre-training**: Trains models on domain-specific unlabeled data to improve domain knowledge.
   - **Fine-tuning**: Supervised learning process using labeled data to adapt models to specific tasks.

4. **Model Fitting Issues**
   - **Underfitting (High Bias)**: Poor performance on both training and test data (too simple).
   - **Overfitting (High Variance)**: Performs well on training data but poorly on new data (memorizes data).

---

### **AWS Services & Features**
1. **Amazon Bedrock Tools**
   - **Watermark Detection**: Identifies AI-generated images (prevents misinformation).
   - **Guardrails**: Filters harmful content and PII in generative AI apps.
   - **Knowledge Bases**: Enables **RAG (Retrieval-Augmented Generation)** by linking FMs to private data sources.

2. **Amazon SageMaker Suite**
   - **Clarify**: Detects bias and explains model predictions.
   - **Model Monitor**: Tracks performance of deployed models (detects data drift).
   - **JumpStart**: Prebuilt models/algorithms for quick deployment.
   - **Model Dashboard**: Central hub to monitor model endpoints and performance.

3. **Other AWS AI Services**
   - **Translate**: Real-time text translation (supports multilingual apps).
   - **Comprehend**: NLP for sentiment analysis, entity recognition.
   - **Forecast**: Time-series forecasting for inventory/pricing predictions.
   - **Lex**: Build conversational chatbots (e.g., customer support).

---

### **Model Evaluation & Optimization**
1. **Inference Parameters**
   - **Temperature**: Controls creativity (0 = deterministic, 1 = creative).
   - **Top-P**: Limits token selection to most probable options.

2. **Evaluation Metrics**
   - **BLEU Score**: Measures translation quality (compares to human references).
   - **ROUGE**: Evaluates text summarization (measures n-gram overlaps).
   - **Shapley Values**: Explains individual predictions (local explainability).
   - **Partial Dependence Plots (PDP)**: Shows global feature impacts.

3. **Cost Optimization**
   - Reduce input tokens (cost scales with token count).
   - Avoid unnecessary model retraining (use RAG instead).

---

### **Model Architectures**
1. **Multimodal Models**
   - Process multiple input types (text, images, audio) and generate mixed outputs.

2. **Generative Models**
   - **Diffusion Models**: Add/remove noise iteratively (used in image generation).
   - **GANs**: Generator creates fake data; discriminator evaluates it.
   - **VAEs**: Encode data into latent space, then decode to generate outputs.

3. **Model Types**
   - **LLMs (Large Language Models)**: Specialize in text tasks (summarization, chat).
   - **Foundation Models**: General-purpose (text, images, etc.).

---

### **Use Case Solutions**
1. **Bias Mitigation**
   - Augment data for underrepresented groups (balance training data).

2. **Translation Quality**
   - Use **BLEU score** (industry standard for machine translation).

3. **Search & Retrieval (RAG)**
   - **Amazon OpenSearch**: Fast vector similarity searches for RAG workflows.

4. **Interpretable Models**
   - **Decision Trees**: Transparent decision-making (vs. "black-box" neural networks).

---

### **Key Differences**
- **Supervised vs. Self-Supervised Learning**: 
  - Supervised uses labeled data; self-supervised creates its own labels.
- **Shapley Values vs. PDP**: 
  - Shapley explains individual predictions; PDP shows global trends.
- **Foundation Models vs. LLMs**: 
  - FMs are general-purpose; LLMs specialize in language tasks.

---
