# 🏠 Gurgaon Real Estate Price Prediction & Recommendation

A machine learning project for predicting real estate prices in Gurgaon (India) and recommending similar properties to buyers/renters.  

This project combines **web scraping ,data cleaning, feature engineering, regression modeling, and recommendation systems** to deliver accurate price predictions and useful property suggestions.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Approach](#approach)
- [Recommendation System](#recommendation-system)
- [Folder Structure](#folder-structure)
- [Installation & Usage](#installation--usage)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview
The Gurgaon housing market is highly dynamic, with property prices influenced by **location, amenities, area, and other features**.  

This project builds:
1. A **price prediction model** using regression algorithms.  
2. A **recommendation system** that suggests similar properties using feature-based similarity measures.  

---

## ✨ Features
- 📊 **Data Scraping , Cleaning & Preprocessing** – Handling missing values and outliers from the web scraped data from the 99Acres website.  
- 🏗 **Feature Engineering** – Selecting and transforming property features (location, size, amenities, etc.).  
- 🤖 **Machine Learning Models** – Multiple regression models compared (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, etc.).  
- 🔎 **Property Recommendation System** – Suggests similar properties based on cosine similarity of feature vectors.  
- 📈 **Exploratory Data Analysis (EDA)** – Univariate and multivariate visualizations.  
- 💻 **Inference Module** – Predict house prices for new input data.  

---

## 📂 Dataset
- Real estate listings data for Gurgaon (scraped from 99Acres website).  
- Includes **location, square footage, number of rooms, amenities, price, etc.**  
- Location coordinates fetched using a **scraper module**.  
- Data cleaned, imputed, and stored in the `data/` and `datasets/` directories.  

---

## 🛠 Approach
1. **Data Collection & Cleaning**  
   - Scraping property listings and location coordinates from the 99Acres website
   - Handling missing values & imputations  
   - Detecting and removing outliers  

2. **Feature Engineering**  
   - Encoding categorical variables  
   - Selecting most important features  
   - Normalization and transformations  

3. **Modeling**  
   - Baseline model (Linear Regression)  
   - Advanced models: Decision Trees, Random Forest, Gradient Boosting  
   - Model comparison using RMSE, MAE, R²  

4. **Deployment Readiness**  
   - Saved trained models (`.pkl` files)  
   - Inference module to make predictions  

---

## 🔗 Recommendation System
- Uses **cosine similarity** between property feature vectors.  
- Helps users find properties with similar characteristics (area, location, price range, amenities).  
- Precomputed similarity matrices stored for quick recommendations.  

---

## 📁 Folder Structure
Gurgaon_Real-Estate_Price_prediction-and-recommendation/
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
├── Home.py # Main script or UI
├── requirements.txt # Python dependencies
└── README.md

---


## ⚙️ Installation & Usage

### 1. Clone the repository
```
git clone https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation.git
cd Gurgaon_Real-Estate_Price_prediction-and-recommendation
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Prepare the dataset
Place raw data in data/ folder
Run cleaning scripts in data_cleaning_code/
Use feature selection notebooks to generate final dataset

4. Train models
```
[jupyter notebook model_selection.ipynb](https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/model_selection.ipynb)
```
5. Make predictions
```
[jupyter notebook model_selection.ipynb](https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/inference_module.ipynb)
```
6. Get property recommendations
```
https://github.com/Namesakenberg/Gurgaon_Real-Estate_Price_prediction-and-recommendation/blob/main/recommendation_system.ipynb
 ```

** I have uploaded the data on the  kaagle below are the links for the raw and the cleaned data**
Raw data : https://www.kaggle.com/datasets/namesakenberg/gurgaon-2023-raw-property-listings
Cleaned version : https://www.kaggle.com/datasets/namesakenberg/gurgaon-flats-data-2023-from-99acres

