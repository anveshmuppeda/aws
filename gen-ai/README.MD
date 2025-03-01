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
