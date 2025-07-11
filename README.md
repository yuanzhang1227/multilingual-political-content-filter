# Multilingual Political Content Filter

## Table of Contents
- [Model Summary](#model-summary)
- [How to Use](#how-to-use)
- [Interactive Demo](#interactive-demo)
- [Training](#training)
- [Evaluation](#evaluation)
- [Limitation](#limitation)

---

## Model Summary

This repository provides political content classifiers for Portuguese (Brazil), Spanish (Spain), and English (US) social media posts. The training data for these classifiers come from social media posts by major media outlets during the following elections:
- **Brazilian Presidential Election (2022)**
- **Spanish General Election (2023)**
- **U.S. Presidential Election (2024)**

### Approach
We employ a hybrid annotation approach:
1. **Human annotators** generate small-scale, gold-standard datasets.
2. **Large Language Models (LLMs)** act as annotators to create large-scale, high-quality labeled datasets.
3. The labeled data is used to fine-tune traditional classifiers based on multilingual sentence transformers.

**Annotation Task:**  
*Is the text related to the politics of the given country?*  
(`yes` / `no` / `unclear`)

---

## How to Use

### Download Models
- **Portuguese (Brazil):** [`pt_model.joblib`](./pt_model.joblib)
- **Spanish (Spain):** [`es_model.joblib`](./es_model.joblib)
- **English (US):** [`en_model.joblib`](./en_model.joblib)

### Example Usage
```python
import joblib
from sentence_transformers import SentenceTransformer

# Load encoder and classifier
encoder = SentenceTransformer("intfloat/multilingual-e5-large")
clf = joblib.load("pt_model.joblib")

# Predict
text = "Seu texto de exemplo aqui"
embedding = encoder.encode([text])  
prediction = clf.predict(embedding)

print(prediction[0])  # Output: 'yes', 'no', or 'unclear'
```

## Interactive Demo

You can try out the model with various sentences using the interactive demo:  
[https://huggingface.co/spaces/Yuan1227/multilingual-political-content-filter](https://huggingface.co/spaces/Yuan1227/multilingual-political-content-filter)

The model card is available here:  
[https://huggingface.co/Yuan1227/multilingual-political-content-filter](https://huggingface.co/Yuan1227/multilingual-political-content-filter)

## Training

Experiments:
LLM annotators: GPT-4, GPT-4 Turbo, GPT-4o, Gemini, Claude, DeepSeek, Mistral
Sentence Transformers for supervised learning (multilingual): MiniLM, Mpnet, E5
Finally we use the data annoated by GPT-4 model as the training data and E5 model as encoder as it achieves the highest consistency and accuracy (see the evaluation below).

## Evaluation

The classifiers trained on different LLM annotated datasets using different sentence transformer embeddings are evaluated with both cross validation and human coder generated gold-standard datasets. The best accuracy score 

Brazil

| Model   | GPT-4 CV | GPT-4 Gold | GPT-4 Turbo CV | GPT-4 Turbo Gold | GPT-4o CV | GPT-4o Gold | Gemini CV | Gemini Gold | Claude CV | Claude Gold | DeepSeek CV | DeepSeek Gold | Mistral CV | Mistral Gold |
|---------|----------|------------|----------------|------------------|-----------|-------------|-----------|-------------|-----------|-------------|-------------|---------------|------------|--------------|
| MiniLM  | 87.80    | 84.94      | 87.60          | 84.56            | 89.02     | 81.08       | 87.13     | 86.10       | 87.67     | 83.40       | 87.60       | 84.56         | 86.51      | 86.10        |
| Mpnet   | 90.08    | 85.33      | 89.56          | 84.56            | 90.73     | 81.85       | 88.98     | 84.56       | 89.80     | 84.56       | 89.56       | 84.56         | 88.80      | 86.10        |
| E5      | **92.29**| **89.96**  | **92.60**      | **86.87**        | **93.22** | **83.01**   | **91.54** | **89.96**   | **91.90** | **86.49**   | **92.60**   | **86.87**     | **91.02**  | **88.80**    |

Spain

| Model   | GPT-4 CV | GPT-4 Gold | GPT-4 Turbo CV | GPT-4 Turbo Gold | GPT-4o CV | GPT-4o Gold | Gemini CV | Gemini Gold | Claude CV | Claude Gold | DeepSeek CV | DeepSeek Gold | Mistral CV | Mistral Gold |
|---------|----------|------------|----------------|------------------|-----------|-------------|-----------|-------------|-----------|-------------|-------------|---------------|------------|--------------|
| MiniLM  | 88.91    | 86.26      | 89.75          | 86.26            | 88.92     | 86.26       | 87.51     | 86.58       | 89.27     | 85.62       | 89.98       | 86.90         | 83.73      | 83.07        |
| Mpnet   | 91.15    | 88.50      | 91.20          | 87.86            | 91.04     | 88.18       | 89.60     | 85.94       | 90.80     | 88.50       | 91.77       | 88.82         | 86.76      | 85.94        |
| E5      | **93.83**| **90.10**  | **94.00**      | **88.82**        | **92.94** | **89.46**   | **92.46** | **88.18**   | **93.31** | **89.46**   | **94.11**   | **90.10**     | **89.18**  | **86.90**    |

The United States

| Model   | GPT-4 CV | GPT-4 Gold | GPT-4 Turbo CV | GPT-4 Turbo Gold | GPT-4o CV | GPT-4o Gold | Gemini CV | Gemini Gold | Claude CV | Claude Gold | DeepSeek CV | DeepSeek Gold | Mistral CV | Mistral Gold |
|---------|----------|------------|----------------|------------------|-----------|-------------|-----------|-------------|-----------|-------------|-------------|---------------|------------|--------------|
| MiniLM  | 91.06    | 89.29      | 90.22          | 89.64            | 90.70     | 87.14       | 89.40     | 88.57       | 90.60     | 90.00       | 90.22       | 89.64         | --         | --           |
| Mpnet   | 92.12    | 90.36      | 91.56          | 88.93            | 90.96     | 88.21       | 90.60     | 88.57       | 91.32     | 89.29       | 91.56       | 88.93         | --         | --           |
| E5      | **94.54**| **89.64**  | **93.89**      | **90.00**        | **92.24** | **88.57**   | **92.46** | **90.36**   | **93.29** | **90.36**   | **93.97**   | **90.00**     | --         | --           |

## Limitation

As the training data are drawn from elections in specific countries and years, these models should be applied with caution to other countries that use the same language or to time periods that are far removed from those elections.
