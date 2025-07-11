import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Property Price Estimator",layout='wide')

# Load the saved files
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.title("🏡 Real Estate Price Predictor")
st.subheader("Please enter the property details below:")

# Input fields with improved grammar
property_type = st.selectbox("Select the property type:", ['flat', 'house'])

sector = st.selectbox("Choose the sector number:", sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox("How many bedrooms does the property have?", sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox("How many bathrooms are available?", sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox("How many balconies are there?", sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox("What is the age of the property?", sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input("Enter the built-up area (in square feet):", min_value=100.0, max_value=10000.0, step=50.0))

servant_room = float(st.selectbox("Does the property have a servant room?", [0.0, 1.0]))

store_room = float(st.selectbox("Does the property have a store room?", [0.0, 1.0]))

furnishing_type = st.selectbox("Select the furnishing type:", sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox("Choose the luxury level of the property:", sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox("What is the preferred floor category?", sorted(df['floor_category'].unique().tolist()))

# Predict button
if st.button('Predict Price'):
    # Form a DataFrame with input
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area,
             servant_room, store_room, furnishing_type, luxury_category, floor_category]]

    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # Prediction
    base_price = np.expm1(pipeline.predict(one_df))[0]  # raw price in rupees
    low = base_price - 0.22
    high = base_price + 0.22

    # Output
    st.success(f"🏠 Estimated property price is between ₹ {round(low, 2)} Cr and ₹ {round(high, 2)} Cr")
