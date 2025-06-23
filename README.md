# 🛍️ EthioMart NER Analysis

EthioMart aims to centralize e-commerce activity on Telegram in Ethiopia. This project focuses on building a **Named Entity Recognition (NER)** system that can extract entities like **product names**, **prices**, and **locations** from **Amharic text messages** posted by various Telegram vendors.

---

## 📌 Project Objectives

- Ingest Amharic text data from multiple Telegram-based e-commerce channels.
- Preprocess, tokenize, and structure the data for machine learning tasks.
- Label a portion of the data in CoNLL format for supervised learning.
- Fine-tune a multilingual transformer (e.g., XLM-Roberta) for Amharic NER.
- Evaluate and compare multiple models (e.g., mBERT, DistilBERT).
- Interpret predictions using SHAP and LIME.
- Create vendor scorecards based on activity and extracted data.

---

## 📁 Folder Structure

ethioMart-ner-analysis/
├── ingestion/ # Telegram scraping scripts
├── data/ # Collected raw & labeled data
├── models/ # Trained/fine-tuned models
├── notebooks/ # Jupyter notebooks (exploration/training)
├── reports/ # Final report & interim summary
├── README.md
├── requirements.txt
└── main.py

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/Dagi2730/ethioMart-ner-analysis.git
cd ethioMart-ner-analysis
Install dependencies

bash

pip install -r requirements.txt
Set up .env for Telegram API

```
API_ID=your_api_id
API_HASH=your_api_hash
PHONE_NUMBER=+2519xxxxxxx
📊 Tasks Overview
Task	Description
✅ Task 1	Ingest and preprocess Amharic Telegram messages
⏳ Task 2	Label Amharic NER dataset in CoNLL format
⏳ Task 3	Fine-tune and evaluate NER models
⏳ Task 4	Compare XLM-R, DistilBERT, and mBERT models
⏳ Task 5	Use SHAP/LIME to interpret model predictions
⏳ Task 6	Generate Vendor Scorecards for micro-lending

👩‍💻 Tech Stack
Python 3.10+

Telethon – for Telegram scraping

Hugging Face Transformers – for model training

Pandas, SpaCy – for data handling

SHAP, LIME – for model interpretability
