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


Exam Alert:

Note the following regarding the techniques to improve the performance of a Foundation Model (FM):

Prompt engineering does NOT change the weights of the FM. Retrieval-Augmented Generation (RAG) does NOT change the weights of the FM. Fine-tuning DOES change the weights of the FM.

The training set is used to train the model, the validation set is used for tuning hyperparameters and selecting the best model during the training process, and the test set is used for evaluating the final performance of the model on unseen data.








multimodal model:
A multimodal model is an artificial intelligence system designed to process and understand multiple types of data, such as text, images, audio, and video. Unlike unimodal models, which handle a single type of data, multimodal models can integrate and make sense of information from various sources, allowing them to perform more complex and versatile tasks.
Multimodal models represent a significant advancement in AI, enabling the integration and understanding of multiple types of data. By combining different modalities, these models can perform a wide range of complex tasks, making them highly versatile and powerful tools in various fields.

multi-modal embedding model:
A multi-modal embedding model is the most suitable choice for this task because it enables the integration of multiple types of data, such as text and images, into a unified representation. This allows the chatbot to effectively process and understand queries containing both text and visual content by aligning them in a shared embedding space, facilitating more accurate and context-aware responses.
You can generate embeddings for your content and store them in a vector database. When an end user submits any combination of text and image as a search query, the model generates embeddings for the search query and matches them to the stored embeddings to provide relevant search and recommendations results to end users. For example, a stock photography company with hundreds of millions of images can use the model to power its search functionality, so users can search for images using a phrase, image, or a combination of image and text. You can further customize the model to enhance its understanding of your unique content and provide more meaningful results using image-text pairs for fine-tuning.

multi-modal generative model:
multi-modal generative model can generate outputs based on multiple types of input data, it is more complex and typically used for generating new content rather than interpreting and responding to queries. In addition, it is costlier to build and maintain a multi-modal generative model compared to a multi-modal embedding model. A multi-modal embedding model is more efficient for understanding and processing combined text and image inputs, whereas a generative model may be excessive if the primary goal is to process and respond to existing multi-modal queries.

A text-only language model
- A text-only language model cannot handle image data because it is designed to process and generate text exclusively. This model lacks the capability to understand or incorporate visual information, making it unsuitable for a chatbot that needs to interpret both text and images in user queries.

convolutional neural network (CNN):
For Image
 A convolutional neural network (CNN) is designed specifically for image recognition and processing tasks and is highly effective for analyzing visual data. However, it cannot process text-based inputs and therefore cannot fulfill the requirement of handling multi-modal queries that include both text and images. A CNN would need to be combined with other models to process text, which adds complexity without directly addressing the multi-modal nature of the queries.

RNNs
For video analysis


Asynchronous inference
Asynchronous inference is the most suitable choice for this scenario. It allows the company to process smaller payloads without requiring real-time responses by queuing the requests and handling them in the background. This method is cost-effective and efficient when some delay is acceptable, as it frees up resources and optimizes compute usage. Asynchronous inference is ideal for scenarios where the payload size is less than 1 GB and immediate results are not critical.

Batch inference - Batch inference is generally used for processing large datasets all at once. While it does not require immediate responses, it is typically more efficient for handling larger payloads (several gigabytes or more). For smaller payloads of less than 1 GB, batch inference might be overkill and less cost-efficient compared to asynchronous inference.

Real-time inference - Real-time inference is optimized for scenarios where low latency is essential, and responses are needed immediately. It is not suitable for cases where the system can afford to wait for responses, as it might lead to higher costs and resource consumption without providing any additional benefit for this particular use case.

Serverless inference - Serverless inference is a good choice for workloads with unpredictable traffic or sporadic requests, as it scales automatically based on demand. However, it may not be as cost-effective for scenarios where workloads are predictable, and some waiting time is acceptable. Asynchronous inference provides a more targeted solution for handling delayed responses at a lower cost.



TOP P
Top P represents the percentage of most likely candidates that the model considers for the next token. Choose a lower value to decrease the size of the pool and limit the options to more likely outputs. Choose a higher value to increase the size of the pool and allow the model to consider less likely outputs

TOP K
The inference parameter Top K represents the number of most likely candidates that the model considers for the next token.

temperature
Use lower temperature if you want more deterministic responses, and use higher temperature if you want creative or different responses for the same prompt on Amazon Bedrock. So, this option is incorrect.

Stop sequence
Stop sequence - Stop sequences specify the sequences of characters that stop the model from generating further tokens. If the model generates a stop sequence that you specify, it will stop generating after that sequence.

Response length
Response length represents the minimum or maximum number of tokens to return in the generated response.




Supervised learning
Supervised learning involves training a model on a labeled dataset to predict outcomes based on input features. While effective for tasks like image recognition or language translation.

Unsupervised learning
Unsupervised learning is designed to identify patterns and structures in data without any predefined labels, making it useful for tasks such as clustering or dimensionality reduction.

incremental training
incremental training is useful for updating a model with new data continuously, it focuses on enhancing a single model's performance with its own data rather than learning from the data of other models. This approach is not designed for optimizing multiple models by leveraging knowledge across different use cases, making it less suitable for the company’s objective.

Self-supervised learning
Self-supervised learning is effective for tasks where labeled data is scarce or unavailable, as it allows models to learn useful representations from large amounts of unlabeled data. However, it does not directly address the need to optimize multiple models using the latest data from other models. This approach is more suitable for foundational training rather than model optimization across different use cases.

Semi-supervised learning
Semi-supervised learning is when you apply both supervised and unsupervised learning techniques to a common problem. This technique relies on using a small amount of labeled data and a large amount of unlabeled data to train systems. First, the labeled data is used to partially train the machine learning algorithm. After that, the partially trained algorithm labels the unlabeled data. This process is called pseudo-labeling. The model is then re-trained on the resulting data mix without being explicitly programmed.

Reinforcement learning
Reinforcement learning is designed for scenarios where a model needs to learn a sequence of actions to achieve a specific goal by maximizing cumulative rewards. It is primarily used in decision-making problems, such as game playing or robotic control. It is not well-suited for optimizing multiple models by learning from the latest data of other models, as it does not involve leveraging cross-model data or knowledge sharing.


Feature engineering for structured data typically includes tasks like normalization, handling missing values, and encoding categorical variables. For unstructured data, such as text or images, feature engineering involves different tasks like tokenization (breaking down text into tokens), vectorization (converting text or images into numerical vectors), and extracting features that can represent the content meaningfully.

Feature Engineering
Feature Engineering is the process of selecting, modifying, or creating new features from raw data to enhance the performance of machine learning models. It is crucial because it can lead to significant improvements in model accuracy and efficiency by providing the model with better representations of the data.

Hyperparameter tuning:
Hyperparameter tuning is the process of selecting the best set of hyperparameters for a machine learning model. Hyperparameters are the external configurations of the model that are set before training and cannot be learned from the data. Feature Engineering is not related to Hyperparameter tuning.
Hyperparameter tuning is the most effective solution in this scenario because it allows the company to adjust the settings that control the learning process of the model. By fine-tuning hyperparameters, such as increasing regularization or early stopping or adjusting dropout rates, the model can avoid overfitting to the training data and better generalize to new, unseen data in production. This approach helps improve the model's performance across various data distributions.

K-Means is an unsupervised learning algorithm used to partition a dataset into distinct clusters by minimizing the variance within each cluster. KNN, on the other hand, is a supervised learning algorithm that classifies new data points based on the majority class among its k-nearest neighbors in the training data.

K-Means is an unsupervised learning algorithm, and KNN is a supervised learning algorithm.

K-Means does not require labeled data; it is used for clustering. KNN, however, requires labeled data for classification.





Fraud identification
Within a large set of transactional data, there’s a subset of labeled data where experts have confirmed fraudulent transactions. For a more accurate result, the machine learning solution would train first on the unlabeled data and then with the labeled data.

Sentiment analysis
When considering the breadth of an organization’s text-based customer interactions, it may not be cost-effective to categorize or label sentiment across all channels. An organization could train a model on the larger unlabeled portion of data first, and then a sample that has been labeled. This would provide the organization with a greater degree of confidence in customer sentiment across the business.

Incorrect options:

Neural network - A neural network solution is a more complex supervised learning technique. To produce a given outcome, it takes some given inputs and performs one or more layers of mathematical transformation based on adjusting data weightings. An example of a neural network technique is predicting a digit from a handwritten image.

Clustering - Clustering is an unsupervised learning technique that groups certain data inputs, so they may be categorized as a whole. There are various types of clustering algorithms depending on the input data. An example of clustering is identifying different types of network traffic to predict potential security incidents.

Dimensionality reduction - Dimensionality reduction is an unsupervised learning technique that reduces the number of features in a dataset. It’s often used to preprocess data for other machine learning functions and reduce complexity and overheads. For example, it may blur out or crop background features in an image recognition application.


semi-supervised learning Techniques/example
Fraud identification
Sentiment analysis

Supervised learning technique
Neural network
Decision tree

unsupervised learning technique
Clustering
Dimensionality reduction






Amazon SageMaker Feature Store - Amazon SageMaker Feature Store is a fully managed, purpose-built repository to store, share, and manage features for machine learning (ML) models. Features are inputs to ML models used during training and inference. For example, in an application that recommends a music playlist, features could include song ratings, listening duration, and listener demographics.

Amazon SageMaker JumpStart - Amazon SageMaker JumpStart is a machine learning (ML) hub that can help you accelerate your ML journey. With SageMaker JumpStart, you can evaluate, compare, and select Foundation Models (FMs) quickly based on pre-defined quality and responsibility metrics to perform tasks like article summarization and image generation. Pretrained models are fully customizable for your use case with your data, and you can easily deploy them into production with the user interface or SDK.

Amazon SageMaker Canvas - SageMaker Canvas offers a no-code interface that can be used to create highly accurate machine learning models —without any machine learning experience or writing a single line of code. SageMaker Canvas provides access 

Amazon SageMaker Ground Truth
To train a machine learning model, you need a large, high-quality, labeled dataset. Ground Truth helps you build high-quality training datasets for your machine learning models. With Ground Truth, you can use workers from either Amazon Mechanical Turk, a vendor company that you choose, or an internal, private workforce along with machine learning to enable you to create a labeled dataset. You can use the labeled dataset output from Ground Truth to train your models. You can also use the output as a training dataset for an Amazon SageMaker model.

Amazon SageMaker Clarify
Amazon SageMaker Clarify provides tools to help explain how machine learning (ML) models make predictions. These tools can help ML modelers and developers and other internal stakeholders understand model characteristics as a whole prior to deployment and to debug predictions provided by the model after it's deployed.

Amazon SageMaker Model Monitor:
 - Amazon SageMaker Model Monitor monitors the quality of Amazon SageMaker machine learning models in production.

SageMaker Model Cards:
You can use Amazon SageMaker Model Cards to document critical details about your machine learning (ML) models in a single place for streamlined governance and reporting. You can catalog details such as the intended use and risk rating of a model, training details and metrics, evaluation results and observations, and additional call-outs such as considerations, recommendations, and custom information.

AI Service Cards:
AI Service Cards are a form of responsible AI documentation that provides customers with a single place to find information on the intended use cases and limitations, responsible AI design choices, and deployment and performance optimization best practices for AI services from AWS.

SageMaker Model Dashboard
 - Amazon SageMaker Model Dashboard is a centralized portal, accessible from the SageMaker console, where you can view, search, and explore all of the models in your account. You can track which models are deployed for inference and if they are used in batch transform jobs or hosted on endpoints.

Model inference is the process of a model generating an output (response) from a given input (prompt).

SageMaker Model evaluation
Model Evaluation - Model evaluation refers to assessing the performance of a machine learning model using specific metrics such as accuracy, precision, recall, or F1 score. Model evaluation does not involve exploratory tasks like calculating statistics or visualizing data; instead, it focuses on validating the effectiveness of a trained model. Therefore, this phase does not align with the company's current activities.
Model evaluation is the process of evaluating and comparing model outputs to determine the model that is best suited for a use case.

SageMaker Role Manager:
 provides a baseline set of permissions for ML activities and personas through a catalog of prebuilt AWS Identity and Access Management (IAM) policies.

Capture model information -
 SageMaker Model Cards is a repository for model information in the Amazon SageMaker Console and helps you centralize and standardize model documentation so you can implement ML responsibly.

Track model behavior -
 SageMaker Model Dashboard gives you a comprehensive overview of deployed models and endpoints so that you can track resources and model behavior violations in one place. You can monitor model behavior in four dimensions: data quality, model quality, bias drift, and feature attribution drift.


Diffusion Model - Diffusion models create new data by iteratively making controlled random changes to an initial data sample. They start with the original data and add subtle changes (noise), progressively making it less similar to the original. This noise is carefully controlled to ensure the generated data remains coherent and realistic. After adding noise over several iterations, the diffusion model reverses the process. Reverse denoising gradually removes the noise to produce a new data sample that resembles the original.

Generative adversarial network (GAN) - GANs work by training two neural networks in a competitive manner. The first network, known as the generator, generates fake data samples by adding random noise. The second network, called the discriminator, tries to distinguish between real data and the fake data produced by the generator. During training, the generator continually improves its ability to create realistic data while the discriminator becomes better at telling real from fake. This adversarial process continues until the generator produces data that is so convincing that the discriminator can't differentiate it from real data.

Variational autoencoders (VAE) - VAEs use two neural networks—the encoder and the decoder. The encoder neural network maps the input data to a mean and variance for each dimension of the latent space. It generates a random sample from a Gaussian (normal) distribution. This sample is a point in the latent space and represents a compressed, simplified version of the input data. The decoder neural network takes this sampled point from the latent space and reconstructs it back into data that resembles the original input.


Interpretability is about understanding the internal mechanisms of a machine learning model, whereas explainability focuses on providing understandable reasons for the model's predictions and behaviors to stakeholders

Interpretability:
Interpretability refers to how easily a human can understand the reasoning behind a model's predictions or decisions. It's about making the inner workings of a machine learning model transparent and comprehensible.

Explainability:
Explainability goes a step further by providing insights into why a model made a specific prediction, especially when the model itself is complex and not inherently interpretable. It involves using methods and tools to make the predictions of complex models understandable to humans.




Confusion matrix
Confusion matrix is a tool specifically designed to evaluate the performance of classification models by displaying the number of true positives, true negatives, false positives, and false negatives. This matrix provides a detailed breakdown of the model's performance across all classes, making it the most suitable choice for evaluating a classification model's accuracy and identifying potential areas for improvement. It provides a comprehensive overview of the model's performance by detailing how many instances were correctly or incorrectly classified in each category. This enables the company to understand where the model is performing well and where it may need adjustments, such as improving the classification of specific material types.

Root Mean Squared Error (RMSE) - Root Mean Squared Error (RMSE) is a metric commonly used to measure the average error in regression models by calculating the square root of the average squared differences between predicted and actual values. However, RMSE is not suitable for classification tasks, as it is designed to measure continuous outcomes, not discrete class predictions.

Mean Absolute Error (MAE) - Mean Absolute Error (MAE) measures the average magnitude of errors in a set of predictions without considering their direction. MAE is typically used in regression tasks to quantify the accuracy of a continuous variable's predictions, not for classification tasks where the outputs are categorical rather than continuous.

Correlation matrix - Correlation matrix measures the statistical correlation between different variables or features in a dataset, typically used to understand the relationships between continuous variables. A correlation matrix is not designed to evaluate the performance of a classification model, as it does not provide any insight into the accuracy or errors of categorical predictions.







Exploratory Data Analysis (EDA)
The company is in the Exploratory Data Analysis (EDA) phase, which involves examining the data through statistical summaries and visualizations to identify patterns, detect anomalies, and form hypotheses. This phase is crucial for understanding the dataset’s structure and characteristics, making it the most appropriate description of the current activities. Tasks like calculating statistics and visualizing data are fundamental to EDA, helping to uncover patterns, detect outliers, and gain insights into the data before any modeling is done. EDA serves as the foundation for building predictive models by providing a deep understanding of the data.

Data Preparation - This option is incorrect because data preparation involves cleaning and preprocessing the data to make it suitable for analysis or modeling. This may include handling missing values, removing duplicates, or transforming variables, but it does not typically involve calculating statistics and visualizing data. While data preparation is an important step, it does not encompass the exploratory analysis activities described in the question.

Data Augmentation - Data augmentation is a technique used primarily in machine learning to artificially increase the size and variability of the training dataset by creating modified versions of the existing data, such as flipping images or adding noise. It is not related to the tasks of calculating statistics or visualizing data, which are part of EDA.

Amazon Rekognition
Amazon Rekognition offers pre-trained and customizable computer vision (CV) capabilities to extract information and insights from your images and videos.

Amazon DeepRacer
Amazon DeepRacer - AWS DeepRacer is an autonomous 1/18th scale race car designed to test RL models by racing on a physical track. Using cameras to view the track and a reinforcement model to control throttle and steering, the car shows how a model trained in a simulated environment can be transferred to the real world.






Sampling bias
This is the correct answer because sampling bias occurs when the data used to train the model does not accurately reflect the diversity of the real-world population. If certain ethnic groups are underrepresented or overrepresented in the training data, the model may learn biased patterns, causing it to flag individuals from those groups more frequently. In this scenario, sampling bias leads to discriminatory outcomes and unfairly targets specific groups based on ethnicity.

Incorrect options:

Measurement bias - Measurement bias is not the correct explanation because it involves inaccuracies in data collection, such as faulty equipment or inconsistent measurement processes. This type of bias does not inherently affect the demographic composition of the dataset and, therefore, is not directly responsible for bias based on ethnicity in the model's outputs.

Observer bias - Observer bias is irrelevant in this context because it relates to human errors or subjectivity during data analysis or observation. Since the AI model processes the data autonomously without human intervention, observer bias is not a factor in the biased outcomes of the model.

Confirmation bias - Confirmation bias involves selectively searching for or interpreting information to confirm existing beliefs. This type of bias does not apply to the AI system in this scenario, as there is no indication that the model is designed to reinforce any preconceptions or assumptions related to ethnicity.



Bias: error due to overly simplistic assumptions in the model, leading to underfitting
Variance: error due to the model being too sensitive to small fluctuations in the training data, leading to overfitting
The bias versus variance trade-off in machine learning is about finding a balance between bias (error due to overly simplistic assumptions in the model, leading to underfitting) and variance (error due to the model being too sensitive to small fluctuations in the training data, leading to overfitting). The goal is to achieve a model that generalizes well to new data.







Bidirectional Encoder Representations from Transformers (BERT)

Embedding models are algorithms trained to encapsulate information into dense representations in a multi-dimensional space. Data scientists use embedding models to enable ML models to comprehend and reason with high-dimensional data.

BERT is the correct answer because it is specifically designed to capture the contextual meaning of words by looking at both the words that come before and after them (bidirectional context). Unlike older models that use static embeddings, BERT creates dynamic word embeddings that change depending on the surrounding text, allowing it to understand the different meanings of the same word in various contexts. This makes BERT ideal for tasks that require understanding the nuances and subtleties of language.


Principal Component Analysis (PCA) - PCA is a statistical method used for reducing the dimensions of large datasets to simplify them while retaining most of the variance in the data. While it can be applied to various fields, including image compression and data visualization, PCA does not understand or differentiate the contextual meanings of words in natural language processing. Thus, it is not a suitable choice for understanding word meanings in different phrases.

Word2Vec - Word2Vec is an early embedding model that creates vector representations of words based on their co-occurrence in a given text. However, it uses static embeddings, meaning each word has a single vector representation regardless of the context. This limitation makes Word2Vec less effective at differentiating words with multiple meanings across different phrases since it cannot adjust the embedding based on context, unlike BERT.

Singular Value Decomposition (SVD) - SVD is a matrix decomposition method used in various applications like data compression and noise reduction. Although it can be part of older methods for text analysis, such as Latent Semantic Analysis (LSA), it is not designed to handle the dynamic, context-dependent meanings of words in sentences. Therefore, it is not suitable for differentiating contextual meanings of words across various phrases.








Amazon Q in Connect
Amazon Connect is the contact center service from AWS. Amazon Q helps customer service agents provide better customer service. Amazon Q in Connect uses real-time conversation with the customer along with relevant company content to automatically recommend what to say or what actions an agent should take to better assist customers.

Incorrect options:

Amazon Q Developer - Amazon Q Developer assists developers and IT professionals with all their tasks—from coding, testing, and upgrading applications, to diagnosing errors, performing security scanning and fixes, and optimizing AWS resources.

Amazon Q Business - Amazon Q Business is a fully managed, generative-AI powered assistant that you can configure to answer questions, provide summaries, generate content, and complete tasks based on your enterprise data. It allows end users to receive immediate, permissions-aware responses from enterprise data sources with citations, for use cases such as IT, HR, and benefits help desks.

Amazon Q in QuickSight - With Amazon Q in QuickSight, customers get a generative BI assistant that allows business analysts to use natural language to build BI dashboards in minutes and easily create visualizations and complex calculations.






Agility
Agility - Agility refers to the ability of the cloud to give you easy access to a broad range of technologies so that you can innovate faster and build nearly anything that you can imagine. You can quickly spin up resources as you need them – from infrastructure services, such as compute, storage, and databases, to the Internet of Things, machine learning, data lakes and analytics, and much more.

Elasticity
Elasticity - With cloud computing elasticity, you don’t have to over-provision resources upfront to handle peak levels of business activity in the future. Instead, you provision the number of resources that you need. You can scale these resources up or down instantly to grow and shrink capacity as your business needs change.

Cost savings
Cost savings - The cloud allows you to trade capital expenses (such as data centers and physical servers) for variable expenses, and only pay for IT as you consume it. Plus, the variable expenses are much lower than what you would pay to do it yourself because of the economies of scale.

Ability to deploy globally in minutes
Ability to deploy globally in minutes - With the cloud, you can expand to new geographic regions and deploy globally in minutes. For example, AWS has infrastructure all over the world, so you can deploy your application in multiple physical locations with just a few clicks. Putting applications in closer proximity to end users reduces latency and improves their experience.


IAM Identity Center
With IAM Identity Center, you can create or connect workforce users and centrally manage their access across all their AWS accounts and applications. You need to configure an IAM Identity Center instance for your Amazon Q Business application environment with users and groups added. Amazon Q Business supports both organization and account-level IAM Identity Center instances.

Incorrect options:

AWS Account 
AWS Account - An AWS account is a container for your AWS resources. You create and manage your AWS resources in an AWS account, and the AWS account provides administrative capabilities for access and billing.

AWS IAM service 
AWS IAM service - AWS IAM service is a powerful tool for securely managing access to your AWS resources. One of the primary benefits of using IAM is the ability to grant shared access to your AWS account. Additionally, IAM allows you to assign granular permissions, enabling you to control exactly what actions different users can perform on specific resources.

IAM user 
IAM user - An IAM user is an entity that you create in AWS. The IAM user represents the human user or workload who uses the IAM user to interact with AWS. A user in AWS consists of a name and credentials.


AWS Trusted Advisor
AWS Trusted Advisor is a service that provides guidance to help you provision your resources following AWS best practices. It helps optimize your AWS environment in areas such as cost savings, performance, security, and fault tolerance, making it an essential tool for governance in AI systems.

AWS Config
AWS Config - AWS Config is a service for assessing, auditing, and evaluating the configurations of your AWS resources. It helps with continuous monitoring and compliance but does not provide the broad optimization and guidance offered by AWS Trusted Advisor.

AWS Audit Manager
AWS Audit Manager - AWS Audit Manager helps you continuously audit your AWS usage to assess risk and compliance with regulations and industry standards. It focuses on compliance reporting rather than providing optimization and guidance.
AWS Audit Manager helps automate the collection of evidence to continuously audit your AWS usage. It simplifies the process of assessing risk and compliance with regulations and industry standards, making it an essential tool for governance in AI systems.

AWS CloudTrail - AWS CloudTrail records AWS API calls and delivers log files for auditing purposes. While it is essential for tracking user activity and compliance, it does not offer the optimization and best practice recommendations provided by AWS Trusted Advisor.

AWS Artifact 
AWS Artifact - AWS Artifact provides on-demand access to AWS’ compliance reports and online agreements. It is useful for obtaining compliance documentation but does not provide continuous auditing or automated evidence collection.

AWS Inferentia accelerators are designed by AWS to deliver high performance at the lowest cost in Amazon EC2 for your deep learning (DL) and generative AI inference applications. The first-generation AWS Inferentia accelerator powers Amazon Elastic Compute Cloud (Amazon EC2) Inf1 instances, which deliver up to 2.3x higher throughput and up to 70% lower cost per inference than comparable Amazon EC2 instances.

EC2
AWS Trainium is the machine learning (ML) chip that AWS purpose-built for deep learning (DL) training of 100B+ parameter models. Each Amazon Elastic Compute Cloud (Amazon EC2) Trn1 instance deploys up to 16 Trainium accelerators to deliver a high-performance, low-cost solution for DL training in the cloud.

Amazon Cognito -
 is AWS’s service for user identity management, authentication, and authorization. It provides secure user sign-up/sign-in flows, manages user pools, and integrates with Amazon Lex to handle user sessions and authentication. In this scenario, Cognito would authenticate patients, assign temporary AWS credentials, and securely pass user identity data to Lex, ensuring compliance with healthcare security requirements.






Inference is the correct term for this process. It refers to the stage where a trained machine learning model is deployed to make predictions or generate outputs based on new input data. During inference, the model uses the patterns and relationships it learned during training to provide accurate and meaningful results. In this scenario, the user sends input data to the SageMaker model, which then performs inference to generate the corresponding output or prediction.

Training is the process of teaching a machine learning model to recognize patterns by adjusting its internal parameters based on a labeled dataset. During training, the model learns from data by minimizing errors and improving accuracy. However, the scenario described does not involve modifying the model’s parameters; it only involves using the trained model to make predictions, making "training" an incorrect choice.

Validation is a step used to evaluate and fine-tune the model during the training process by checking its performance on a validation dataset, which is separate from the training dataset. The purpose is to optimize the model's hyperparameters and prevent overfitting. Since the scenario involves using the model to predict outcomes from new input data, rather than evaluating or fine-tuning it, "validation" is not the correct term.

Testing is the final evaluation phase of a model, where its performance is assessed on an unseen test dataset after the training and validation phases are complete. It provides an unbiased estimate of the model’s generalization ability to new data. However, in the given scenario, the focus is on generating predictions from a model already trained, rather than testing its performance, so "testing" is not the correct answer.



To get predictions for an entire dataset - To get predictions for an entire dataset, SageMaker batch transform deployment type is recommended.

For persistent, real-time endpoints that make one prediction at a time - For persistent, real-time endpoints that make one prediction at a time, SageMaker real-time hosting services are recommended.

For workloads that can tolerate cold starts - For workloads that have idle periods between traffic spikes and can tolerate cold starts, SageMaker Serverless Inference is recommended.



Feature extraction involves transforming the data into a new feature space, often using techniques like Principal Component Analysis (PCA) to reduce the number of features. Feature selection, on the other hand, involves selecting a subset of the most relevant features from the original dataset, typically using methods like forward selection, backward elimination, or regularization techniques.

Governance and compliance - This discipline focuses on the policies, procedures, and reporting specific to generative AI solutions.

Legal and privacy - This discipline addresses regulatory, legal, and privacy requirements specific to generative AI solutions.

Resilience - This discipline involves designing generative AI solutions to maintain availability and meet business SLAs.

Risk management - in the Generative AI Security Scoping Matrix involves identifying potential threats to generative AI solutions and recommending mitigations. It encompasses activities like risk assessments and threat modeling, which are essential for understanding and addressing the unique risks associated with generative AI workloads.

Continued Pre-training

In the continued pre-training process, you provide unlabeled data to pre-train a foundation model by familiarizing it with certain types of inputs. You can provide data from specific topics to expose a model to those areas. The Continued Pre-training process will tweak the model parameters to accommodate the input data and improve its domain knowledge.

For example, you can train a model with private data, such as business documents, that are not publicly available for training large language models. Additionally, you can continue to improve the model by retraining the model with more unlabeled data as it becomes available.

Fine-tuning

While fine-tuning a model, you provide labeled data to train a model to improve performance on specific tasks. By providing a training dataset of labeled examples, the model learns to associate what types of outputs should be generated for certain types of inputs. The model parameters are adjusted in the process and the model's performance is improved for the tasks represented by the training dataset.

Zero-shot prompting

Chain-of-thought prompting

Prompt engineering is the practice of carefully designing prompts to efficiently tap into the capabilities of FMs. It involves the use of prompts, which are short pieces of text that guide the model to generate more accurate and relevant responses. With prompt engineering, you can improve the performance of FMs and make them more effective for a variety of applications. Prompt engineering has techniques such as zero-shot and few-shot prompting, which rapidly adapts FMs to new tasks with just a few examples, and chain-of-thought prompting, which breaks down complex reasoning into intermediate steps.

Prompt engineering is not a model customization method. Therefore, both these options are incorrect.

Retrieval Augmented Generation (RAG) - Retrieval Augmented Generation (RAG) allows you to customize a model’s responses when you want the model to consider new knowledge or up-to-date information. When your data changes frequently, like inventory or pricing, it’s not practical to fine-tune and update the model while it’s serving user queries. To equip the FM with up-to-date proprietary information, organizations turn to RAG, a technique that involves fetching data from company data sources and enriching the prompt with that data to deliver more relevant and accurate responses. RAG is not a model customization method.



Hijacking involves manipulating an AI system to serve malicious purposes or to misbehave in unintended ways.

Jailbreaking refers to bypassing the built-in restrictions and safety measures of AI systems to unlock restricted functionalities or generate prohibited content.

Response B is an example of hijacking, where the AI model initially provides a useful response but then diverts to an unethical suggestion (using a cheat tool). Response D is an example of jailbreaking, where the AI is manipulated into providing information about disabling antivirus software despite the initial innocent prompt.





Generative models learn the underlying patterns of data to create new, similar data, while discriminative models learn to distinguish between different classes of data. Generative models, such as GPT-3, can generate new content, whereas discriminative models are used for classification tasks. The former focuses on understanding and replicating the data distribution, while the latter focuses on decision boundaries to classify inputs.

For example, discriminative models look at images - known data like pixel arrangement, line, color, and shape — and then map them to an outcome — the unknown factor. Mathematically, these models work by identifying equations that could numerically map unknown and known factors as x and y variables.

Generative models take this one step further. Instead of predicting a label given some features, they try to predict features given a certain label. Mathematically, generative modeling calculates the probability of x and y occurring together. It learns the distribution of different data features and their relationships. For example, generative models analyze animal images to record variables like different ear shapes, eye shapes, tail features, and skin patterns. They learn features and their relations to understand what different animals look like in general. They can then recreate new animal images that were not in the training set.



Generative AI powered summarization chatbot

Generative AI powered summarization chatbot leverages large language models to generate concise summaries of text. With prompt engineering, the summarization chatbot can be specifically tailored to accurately extract detailed key points, entities, or legal clauses from complex legal documents.

Amazon Comprehend

Amazon Comprehend is an effective choice because it is specifically designed to process large volumes of unstructured text data, such as legal documents, and extract key entities, phrases, and insights. It uses machine learning to accurately identify and extract relevant information, like names, dates, and specific legal clauses, making it well-suited for the law firm’s needs. The service can be integrated with other AWS tools to automate and scale the document review process, thereby enhancing efficiency.

Amazon Textract

Amazon Textract is also a suitable choice because it is designed to extract structured data from scanned documents, such as PDFs or images, which is common in legal settings. Textract can identify key fields, like dates, names, and amounts, and extract them into a structured format. This makes it particularly useful for handling large volumes of physical or scanned documents where the information is not readily accessible as text. Combined with NLP tools like Amazon Comprehend, Textract can provide a comprehensive solution for extracting both structured and unstructured information from legal documents.

Incorrect options:

Convolutional Neural Network (CNN) - This option is incorrect because CNNs are designed for tasks such as image and video recognition, object detection, and similar applications involving grid-like data (such as pixels in an image). While CNNs are excellent at feature extraction and classification in images, they are not inherently designed for document parsing or extraction tasks.

Amazon Personalize - Amazon Personalize is designed for building machine learning models to provide personalized recommendations, such as product or content suggestions. It does not have any built-in capabilities for text analysis or document processing, making it completely irrelevant for the law firm’s goal of extracting key points from legal documents.

WaveNet - This option is incorrect because WaveNet is tailored for audio data generation, specifically for tasks such as speech synthesis and audio signal processing. It does not have the capabilities to analyze legal documents or extract key information, making it an incorrect choice for this task.


stable Diffusion
Stable Diffusion is a generative artificial intelligence (generative AI) model that produces unique photorealistic images from text and image prompts.


Llama - Llama is a series of large language models trained on publicly available data. They are built on the transformer architecture, enabling them to handle input sequences of any length and produce output sequences of varying lengths. A notable feature of Llama models is their capacity to generate coherent and contextually appropriate text.

Jurassic - Jurassic family of models from AI21 Labs supported use cases such as question answering, summarization, draft generation, advanced information extraction, and ideation for tasks requiring intricate reasoning and logic.

Claude - Claude is Anthropic’s frontier, state-of-the-art large language model that offers important features for enterprises like advanced reasoning, vision analysis, code generation, and multilingual processing.



RMSE is a metric used to measure the average magnitude of errors in a regression model's predictions. It is not appropriate for binary classification tasks because it is designed to assess continuous numeric predictions rather than categorical outcomes. Therefore, RMSE does not provide meaningful insights into the correct or incorrect outcomes in a classification context.











