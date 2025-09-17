# 🏠 Gurgaon Real Estate Price Prediction & Recommendation

A machine learning project for predicting **real estate prices in Gurgaon (India)** and recommending similar properties to buyers/renters.  

This project combines **web scraping, data cleaning, feature engineering, regression modeling, analytics, and recommendation systems** to deliver accurate price predictions, insights, and property suggestions through a Streamlit interface.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Recommendation System](#recommendation-system)
- [Folder Structure](#folder-structure)
- [Installation & Usage](#installation--usage)
- [Dataset Links](#dataset-links)

---

## 📖 Overview
The Gurgaon housing market is highly dynamic, with property prices influenced by **location, amenities, area, and other features**.  

This project builds:
1. A **price prediction model** using regression algorithms.  
2. A **recommendation system** that suggests similar properties using feature-based similarity measures.  
3. An **analytics module** for market insights.  

---

## ✨ Features
- 📊 **Data Scraping & Cleaning** – Data scraped from 99Acres, cleaned & merged for consistency.  
- 🏗 **Feature Engineering** – Custom transformations like luxury score, furnish details, and possession status.  
- 📈 **Exploratory Data Analysis (EDA)** – Includes univariate, multivariate, and Pandas Profiling reports.  
- 🔎 **Outlier Handling & Missing Value Imputation** – Robust preprocessing pipeline.  
- 🤖 **Machine Learning Models** – Regression models (Linear Regression, Ridge, LASSO, SVR, Random Forest, Gradient Boosting, etc.) with comparison.  
- ⚙️ **Feature Selection** – SHAP, Recursive Feature Elimination, LASSO, and Permutation Importance.  
- 🌐 **Streamlit Web App** – For price prediction, recommendations, and insights.  
- 💡 **Recommender System** – Content-based filtering using location, facilities, and price.  
- 📊 **Analytics Module** – Geo-maps, scatterplots, word clouds, and interactive sector-level insights.  

---

## 📂 Dataset
- Real estate listings data scraped from **99Acres**.  
- Includes **location, square footage, number of rooms, amenities, price, etc.**  
- Location coordinates fetched using a **scraper module**.  
- Cleaned and stored in the `data/` and `datasets/` directories.  

---

## 🛠 Project Workflow

### 1. Data Gathering  
- Project overview in detail  
- Scraped data from 99Acres  
- Collected raw data for flats & houses  

### 2. Data Cleaning  
- Merging flats and houses datasets  
- Basic data cleaning  

### 3. Feature Engineering  
- Engineered columns:  
  - `additionalRoom`  
  - `areaWithType`  
  - `agePossession`  
  - `furnishDetails`  
  - `luxuryScore` (from amenities & features)  

### 4. Exploratory Data Analysis (EDA)  
- Univariate analysis  
- Multivariate analysis  
- Pandas Profiling reports  

### 5. Outlier Detection & Removal  
- Outlier detection and handling  

### 6. Missing Value Imputation  
- Imputation for `area` and `bedroom`  
- General missing value imputation strategies  

### 7. Feature Selection  
- Techniques used:  
  - Correlation analysis  
  - Random Forest Feature Importance  
  - Gradient Boosting Feature Importance  
  - Permutation Importance  
  - LASSO Regression  
  - Recursive Feature Elimination (RFE)  
  - Linear Regression with weights  
  - SHAP (Explainable AI)  

- Models built:  
  - Linear Regression (with OHE, transformations, pipelines)  
  - Support Vector Regression (SVR)  

### 8. Model Selection & Productionalization  
- Price prediction pipeline with different encodings:  
  - Ordinal Encoding  
  - One-Hot Encoding (OHE)  
  - OHE with PCA  
  - Target Encoding  
- Model comparison and selection  
- Streamlit-based web interface for prediction  

### 9. Analytics Module  
- Interactive visualizations:  
  - Geo map (property distribution)  
  - Word cloud (amenities)  
  - Scatterplot (area vs. price)  
  - Pie chart (BHK distribution by sector)  
  - Side-by-side boxplot (bedroom vs. price)  
  - Distplots (flat vs. house prices)  

### 10. Recommender System – Part 1  
- Based on:  
  - Top Facilities  
  - Price Details  
  - Location Advantages  

### 11. Recommender System – Part 2  
- Evaluation of recommendation results  
- Streamlit web interface for recommendations  

### 12. Insights Module  
- Summarized insights about Gurgaon’s housing market.  

---

## 🔗 Recommendation System
- Built using **cosine similarity** on property feature vectors.  
- Helps users discover similar properties by:  
  - Location  
  - Price range  
  - Amenities & features  
- Evaluated for relevance, with results displayed in a Streamlit interface.  

---

## 📁 Folder Structure
```
├── data/ # Raw and processed datasets
├── datasets/ # Source datasets
├── Scraper/ # Scripts to fetch listings and coordinates
├── data_cleaning_code/ # Cleaning, missing value handling, outlier detection
├── EDA/ # Exploratory Data Analysis notebooks
├── Feature_Selection/ # Feature engineering and selection
├── baseline_model.ipynb # Simple baseline regression model
├── model_selection.ipynb # Training and comparing multiple models
├── inference_module.ipynb # Prediction on new/unseen data
├── recommendation_system.ipynb # Property recommendation system
├── Home.py # Streamlit web interface
├── requirements.txt # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation.git
cd Gurgaon_Real-Estate_Price_prediction-and-recommendation
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Prepare the dataset
   a)Place raw data in data/ folder
   b)Run cleaning scripts in data_cleaning_code/
   c)Use feature engineering and selection notebooks to generate the final dataset

4. Train models
👉 [model_selection.ipynb](https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/model_selection.ipynb)

5. Make predictions

👉 [inference_module.ipynb](https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/inference_module.ipynb)

6. Get property recommendations

👉 [recommendation_system.ipynb](https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/recommendation_system.ipynb)

📊 Dataset Links

Datasets are uploaded by me on Kaggle:
📂 [Raw data](https://www.kaggle.com/datasets/namesakenberg/gurgaon-2023-raw-property-listings)
📂 [Cleaned version](https://www.kaggle.com/datasets/namesakenberg/gurgaon-flats-data-2023-from-99acres)
