### **1. AI vs. ML vs. Deep Learning**  
- **AI**: Broad field of creating systems that mimic human intelligence (e.g., chatbots, self-driving cars).  
- **ML**: Subset of AI where machines learn patterns from **data** (no explicit programming).  
  - *Example*: Predicting house prices using past sales data.  
- **Deep Learning (DL)**: Subset of ML using **neural networks** (layers of nodes like a brain).  
  - *Example*: Recognizing faces in photos.  

**Exam Tip**:  
- **MYCIN** (1970s AI) = Rule-based (not ML).  
- **DL** = Requires GPUs, good for images/text.  

---

### **2. Generative AI (GenAI)**  
- **What**: Creates new content (text, images, code).  
- **Key Models**:  
  - **Transformers** (e.g., GPT, BERT): Process entire sentences, not word-by-word.  
  - **Multimodal Models** (e.g., GPT-4o): Mix inputs/outputs (text + image → video).  
- **RLHF (Reinforcement Learning from Human Feedback)**: Trains models using human preferences.  
  - *Example*: Making ChatGPT’s answers sound more “human.”  

**Exam Tip**:  
- **GPT** = Text/code generation.  
- **BERT** = Reads text bidirectionally (good for translations).  

---

### **3. Machine Learning Types**  
#### **Supervised Learning**  
- **Labeled Data** (input + output pairs).  
  - **Regression**: Predicts numbers (e.g., house prices).  
  - **Classification**: Predicts categories (e.g., spam vs. not spam).  

#### **Unsupervised Learning**  
- **Unlabeled Data** (finds patterns).  
  - **Clustering**: Groups similar data (e.g., customer segments).  
  - **Association Rules**: Finds linked items (e.g., “buy chips → buy soda”).  
  - **Anomaly Detection**: Flags outliers (e.g., fraud).  

#### **Reinforcement Learning (RL)**  
- **Agent** learns by trial/error with rewards (e.g., robot in a maze).  

**Exam Tip**:  
- **Semi-supervised Learning** = Mix labeled + unlabeled data.  
- **Self-supervised Learning** = Model labels its own data (used in BERT/GPT).  

---

### **4. Key ML Terms**  
- **Training/Validation/Test Sets**:  
  - **60-80% Training** (teach the model).  
  - **10-20% Validation** (tune settings).  
  - **10-20% Test** (final evaluation).  
- **Feature Engineering**:  
  - Transform raw data → useful inputs (e.g., convert text to numbers).  
- **Overfitting** = Model memorizes training data (fails on new data).  
  - *Fix*: More data, simplify model, regularization.  
- **Underfitting** = Model too simple (fails on training data).  
  - *Fix*: Use a more complex model.  

---

### **5. Model Evaluation Metrics**  
#### **Classification**  
- **Confusion Matrix**:  
  - **Precision**: Avoid false positives (e.g., spam detection).  
  - **Recall**: Avoid false negatives (e.g., cancer diagnosis).  
  - **F1 Score**: Balance precision/recall.  
- **AUC-ROC**: Measures model performance (1 = perfect).  

#### **Regression**  
- **MAE/RMSE**: Average error (lower = better).  
- **R²**: % of variance explained (1 = perfect).  

---

### **6. AWS-Specific Tips**  
- **Amazon SageMaker Tools**:  
  - **Clarify**: Detect bias in models.  
  - **Model Monitor**: Track deployed models.  
  - **JumpStart**: Pre-built models/algorithms.  
- **Inferencing**:  
  - **Real-Time** (e.g., chatbots) vs. **Batch** (e.g., reports).  
  - **Edge Devices**: Use small models (e.g., IoT devices).  

**Exam Tip**:  
- **RLHF** is critical for aligning LLMs (like ChatGPT) with human values.  

---

### **7. When NOT to Use ML**  
- Use **code** for deterministic problems (e.g., probability calculations).  
- ML = Approximation; code = Exact solution.  

---

### **Cheat Sheet for Exam**  
| **Concept**          | **Key Point**                                  |  
|-----------------------|-----------------------------------------------|  
| **AI vs. ML**         | AI = Broad; ML = Learns from data.            |  
| **Transformers**      | Process entire sentences (GPT, BERT).         |  
| **Supervised**        | Labeled data → predictions.                   |  
| **Unsupervised**      | Finds patterns (clustering, anomalies).       |  
| **Overfitting**       | Model memorizes data → fails on new data.     |  
| **Precision vs. Recall** | Precision = Avoid false positives; Recall = Avoid false negatives. |  
| **SageMaker Clarify** | Detects bias in models.                       |  

---

### **Memorable Examples**  
- **Clustering**: Group customers by buying habits → target marketing.  
- **GANs**: Generate fake images (artist vs. critic).  
- **Reinforcement Learning**: Robot learns maze → reward for reaching exit.  
