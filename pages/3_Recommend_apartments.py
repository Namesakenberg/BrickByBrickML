import streamlit as st
import pandas as pd
import pickle

# Set the page title and layout
st.set_page_config(page_title="Apartment Recommender", layout="wide")

st.title("🏡 Apartment Recommender System")

# Load data
location_df = pickle.load(open('datasets/location_distances.pkl', 'rb'))            # load the dataframe
cosine_sim1 = pickle.load(open('cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('cosine_sim3.pkl','rb'))

# Function to recommend similar properties
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5*cosine_sim1 + 0.8*cosine_sim2 + 1*cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': [round(score, 3) for score in top_scores]
    })

    return recommendations_df

# ────────────────────────────────────────────────
# 🔁 SECTION 1: Recommender (More Realistic & Accurate)
st.markdown("## 🔁 Recommend Similar Properties Based on a Society")

selected_society = st.selectbox("🏙️ Select a society", sorted(location_df.index.to_list()))       # select a society independently from dropdown

if st.button("🎯 Recommend Similar Properties"):
    recommendations = recommend_properties_with_scores(selected_society)
    with st.expander("🔍 View Recommendations"):
        st.dataframe(recommendations, use_container_width=True)

# ───────────────────────────────────────────────
# 📍 SECTION 2: Landmark-based Nearby Properties (Less accurate)
st.markdown("---")
st.markdown("## 📍 Find Properties Near a Landmark")

with st.container():
    selected_location = st.selectbox("Select a reference location", location_df.columns.tolist())
    radius = st.slider("Select radius (in km)", min_value=1, max_value=50)

    if st.button("🔎 Search Nearby Properties"):
        st.markdown(f"### 🏘️ Properties within **{radius} km** of **{selected_location}**")
        results = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

        if results.empty:
            st.warning("No properties found within the selected radius.")
        else:
            result_df = pd.DataFrame({
                "Property Name": results.index,
                "Distance (km)": (results.values / 1000).round(2)
            }).reset_index(drop=True)

            st.session_state["result_df"] = result_df
            st.session_state["search_clicked"] = True

# ────────────────────────────────────────────────
# 💡 Side-by-Side Layout for Radio + Recommendation
if st.session_state.get("search_clicked") and st.session_state.get("result_df") is not None:
    result_df = st.session_state["result_df"]

    st.success(f"✅ Found {len(result_df)} nearby properties.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏘️ Nearby Societies")
        selected_society = st.radio(
            label="Select a nearby society:",
            options=result_df['Property Name'].tolist(),
            captions=[f"{dist} km" for dist in result_df["Distance (km)"]],
            index=0
        )

    with col2:
        if selected_society:
            st.subheader("🎯 Recommended Alternatives")
            recommendations = recommend_properties_with_scores(selected_society)
            st.dataframe(recommendations, use_container_width=True)
