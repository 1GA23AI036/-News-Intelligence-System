# 📰 News Intelligence System

A Python-based **News Intelligence and Information Extraction System** that processes news articles and converts raw article data into useful analytical insights.

## 🚀 Features

- 📄 News article preprocessing and cleaning
- 🏷️ Named Entity Recognition (NER) using spaCy
- 🔑 Keyword extraction and frequency analysis
- 🧠 Topic analysis using TF-IDF
- 😊 Sentiment analysis
- 🗂️ News categorization
- 📊 Statistical analysis and visualizations
- 📑 Report generation
- 📈 Interactive Streamlit dashboard
- 💾 Export of processed results to CSV

## 🛠️ Technologies

- **Python**
- **Pandas**
- **spaCy**
- **Scikit-learn**
- **TextBlob**
- **Matplotlib**
- **Streamlit**

## 📁 Project Structure

```text
News-Intelligence-System/
│
├── app.py
├── README.md
├── data/
│   └── Kosovo-News-Articles.csv
│
├── output/
│
└── src/
    ├── __init__.py
    ├── preprocessing.py
    ├── entities.py
    ├── topics.py
    ├── sentiment.py
    ├── analysis.py
    ├── keywords.py
    ├── categorization.py
    ├── reports.py
    └── visualization.py
```

## ⚙️ Installation

### 1. Open the project folder

```powershell
cd "C:\Users\HP\Downloads\archive"
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

For PowerShell:

```powershell
& ".\.venv\Scripts\Activate.ps1"
```

If PowerShell blocks activation, you can run the project using the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Install the required packages

```powershell
python -m pip install pandas spacy scikit-learn textblob matplotlib streamlit
```

### 5. Install the spaCy English model

```powershell
python -m spacy download en_core_web_sm
```

## ▶️ Run the Application

Start the Streamlit dashboard with:

```powershell
python -m streamlit run app.py
```

Then open the address shown in the terminal, normally:

```text
http://localhost:8501
```

## 📊 System Workflow

```text
News Dataset
     ↓
Data Loading
     ↓
Preprocessing & Cleaning
     ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Entities       Keywords       Sentiment
 ↓               ↓               ↓
 └───────────────┴───────────────┘
                 ↓
           Topic Analysis
                 ↓
          News Categorization
                 ↓
       Analysis & Visualization
                 ↓
          Reports / CSV Output
                 ↓
        Streamlit Dashboard
```

## 📌 Dataset

The system is designed to work with a news article CSV dataset. The included dataset is:

```text
data/Kosovo-News-Articles.csv
```

The preprocessing module automatically looks for suitable article/text columns depending on the dataset structure.

## 📂 Output

Generated analysis files and visualizations can be stored in:

```text
output/
```

Typical outputs may include:

- Cleaned article data
- Entity results
- Keyword frequencies
- Topic results
- Sentiment results
- Analysis summaries
- Charts and visualizations
- Generated reports

## 🧠 NLP Components

### Named Entity Recognition

The system uses spaCy to identify entities such as:

- People
- Organizations
- Locations
- Dates
- Countries
- Events

### Keyword Analysis

Frequently occurring and important terms are extracted from the news articles to identify major subjects.

### Topic Analysis

TF-IDF and related NLP techniques are used to identify important terms and discover themes across articles.

### Sentiment Analysis

Articles are analyzed to estimate their sentiment and help identify positive, negative, or neutral content.

### News Categorization

Articles can be grouped into meaningful categories based on their content.

## 📈 Streamlit Dashboard

The Streamlit application provides an interactive interface for exploring the processed news dataset and viewing analytical results.

## 🔧 Troubleshooting

### `ModuleNotFoundError`

If you see an error such as:

```text
ModuleNotFoundError: No module named 'sklearn'
```

install the missing package:

```powershell
python -m pip install scikit-learn
```

For TextBlob:

```powershell
python -m pip install textblob
```

For spaCy:

```powershell
python -m pip install spacy
```

### `No module named 'en_core_web_sm'`

Run:

```powershell
python -m spacy download en_core_web_sm
```

### `No columns to parse from file`

Make sure the CSV dataset is not empty and is located at:

```text
data/Kosovo-News-Articles.csv
```

Also check that the CSV contains a header row and article data.

## 🎯 Project Goal

The goal of this project is to demonstrate how **Natural Language Processing, machine learning, and data visualization** can be combined to build a practical news intelligence platform.

The system transforms unstructured news articles into structured information that can be analyzed and visualized.

## 📜 License

This project is intended for educational and research purposes.

---

**News Intelligence System — NLP-powered news analysis with Python and Streamlit.**
