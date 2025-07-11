import streamlit as st

# Set page config
st.set_page_config(
    page_title="Gurgaon Real Estate App",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Homepage Title and Intro
st.title("🏠 Gurgaon Real Estate Price Prediction & Insights")
st.markdown("---")

# Main Description
st.markdown("""
Welcome to the **Gurgaon Real Estate Price Prediction and Analysis App** – a comprehensive tool designed to explore, analyze, and predict property prices across Gurgaon using **machine learning** and **data-driven insights**.

This app is built to assist:
- 🏡 **Buyers**
- 📈 **Investors**
- 📊 **Analysts**
- 🧠 **Real estate enthusiasts**

in making informed decisions through:

- 📊 **Real estate trend analysis**
- 💡 **Key feature-driven pricing insights**
- 💰 **Accurate property price prediction**
- 🧭 **Personalized property recommendations**
""")

# Navigation instructions
st.markdown("### 🔍 Use the **sidebar** to navigate between the modules:")
st.markdown("""
- 🔹 **Price Prediction Module**  
  Enter property features to get price predictions from machine learning models trained on real data.
  
- 🔹 **Analytics Module**  
  Explore Gurgaon property trends with interactive geo-maps, word clouds, scatter plots, and more.
  
- 🔹 **Recommendation Module**  
  Get suggestions tailored to your preferences using amenities, price, and location advantages.

""")

st.markdown("---")
st.success("Start by selecting a module from the sidebar to begin your real estate journey in Gurgaon!")
