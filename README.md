# 💬 WhatsApp Chat Analyzer with Sentiment Analysis

A Python + Streamlit web app that analyzes WhatsApp chat exports and gives detailed insights into message activity, most active users, common words, emoji usage, and the emotional tone of the conversation using sentiment analysis.

---

## Features

- Upload `.txt` file exported from WhatsApp
- View daily, monthly, and hourly activity trends
- Identify most active users and their message counts
- Generate word clouds and top word lists
- Analyze emoji usage per person
- Run sentiment analysis using the VADER model

---

## 🖼️ Demo Screenshots

### Overview
![Overview](screenshots/overview.png)

### Activity Timeline
![Activity](screenshots/activity.png)

### Emoji and Sentiment
![Sentiment](screenshots/sentiment.png)

---

## 🛠 Tech Stack

- **Backend & Data**: Python, Pandas, Regex, NLTK, VADER
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Frontend**: Streamlit
- **Text Processing**: WordCloud, Emoji, Collections

---


---

## ▶️ How to Run the App Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/tanishapritha/WhatsApp-Chat-Analyzer-with-Sentiment-Analysis
cd WhatsApp-Chat-Analyzer-with-Sentiment-Analysis
```

### Step 2: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 3: Run Streamlit App
```bash
streamlit run app.py
```

