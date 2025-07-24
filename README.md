🏡 Real Estate Price Prediction and Recommendation System — Gurgaon (99acres.com)
📌 Overview
This project is an end-to-end Real Estate Data Science Application built using data scraped from 99acres.com. It covers the complete ML pipeline — from data collection, preprocessing, and model training to deployment via an interactive Streamlit dashboard.

The core objective is to predict property prices in Gurgaon and provide personalized property recommendations based on user preferences.

🛠 Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn

Scikit-Learn, SHAP, Pickle

Pandas Profiling, Streamlit, Google Colab

Web Scraping: BeautifulSoup, requests

📊 Project Features
✅ Web Scraping (~3500 listings) from 99acres.com using BeautifulSoup

Extracted structured data on price, area, location, furnishing, amenities, etc.

Location focus: Gurgaon (all sectors)

✅ Exploratory Data Analysis (EDA)

Univariate, bivariate, and multivariate analysis

Automated profiling using Pandas Profiling

Outlier treatment, missing value imputation, and encoding of categorical features

✅ Feature Engineering + Selection

Applied 8+ techniques:

LASSO Regression

Recursive Feature Elimination (RFE)

SHAP (SHapley Additive exPlanations)

Correlation Matrix

Random Forest Feature Importance

Mutual Information, Chi-square, etc.

Goal: Identify key drivers of price variation

✅ Machine Learning Model

Random Forest Regressor

Fine-tuned using GridSearchCV and K-Fold Cross Validation

Achieved:

R² Score = 0.902

MAE ≈ 0.53 lakhs

✅ Recommendation Engine

Used cosine similarity on:

Location vectors

Amenities

Price per sqft

Implemented weighted scoring logic for personalized top property suggestions

✅ Streamlit Dashboard

Geo-map of Gurgaon: average area, price, and price/sqft by sector

BHK-wise pie charts

Word cloud of most common amenities

Area vs. Price scatterplots

Bedroom-wise boxplots

Real-time recommendations and model output

📦 Deployment & Packaging
🧠 Model serialized with Pickle

✅ Tested in Google Colab

🚀 Ready for deployment on Streamlit Cloud or custom server



📌 Disclaimer:
The data used in this project was scraped from publicly available listings on 99acres.com in 2023 for educational purposes only.
No personal or sensitive information has been collected or shared.
This project is intended solely for academic and non-commercial use.
