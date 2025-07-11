import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns

#analytics module :
#1) geo map
#2) amenities word cloud
#3) scatterplot
#4) piechart
#5) boxplot
#6) distplot oof price and property

# Load data
new_df = pd.read_csv('datasets/data_viz1.csv')

# Clean sector name (optional: title case)
new_df['sector'] = new_df['sector'].astype(str).str.strip().str.title()

# Group by sector
group_df = new_df.groupby('sector', as_index=False).mean(numeric_only=True)[
    ['sector', 'price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
]

# Streamlit page layout
st.set_page_config(page_title="Gurgaon Property Analytics", layout="wide")
st.title("📍 Gurgaon Sector-wise Property Analytics")



# Plot map
fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.sequential.Viridis,
    zoom=10,
    mapbox_style="open-street-map",
    hover_name="sector",
    hover_data={
        "price": True,
        "price_per_sqft": True,
        "built_up_area": True,
        "latitude": False,
        "longitude": False
    }
)

fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0},
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# plot the wordcloud
st.title("🏠 Property Amenities Word Cloud")
st.markdown(
    """
    This word cloud visualizes the most frequently mentioned amenities across all properties.
    Larger words indicate higher frequency.
    """
)

# Load amenities text from pickle
wordcloud_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

# Sidebar: Optional word filters
with st.sidebar:
    st.header("⚙️ Word Cloud Settings")
    remove_common_words = st.checkbox("Remove common junk words", value=True)

# Define stopwords
custom_stopwords = set(STOPWORDS)
if remove_common_words:
    custom_stopwords.update(['shui', 'nan', 'null', 'none', 'etc', 'vaastu'])

# Generate the WordCloud
wordcloud = WordCloud(
    width=400,
    height=180,
    background_color='white',
    colormap='viridis',
    stopwords=custom_stopwords,
    max_words=150
).generate(wordcloud_text)

# Use columns to center and reduce width
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

st.title("📈 Area vs price")
df = pd.read_csv('datasets/gurgaon_properties_post_feature_selection_v2.csv')
with st.sidebar:
    st.header("select property type")
    property_selected= st.selectbox('Select property type',['flat','house'])
fig1= px.scatter(df[df['property_type']==property_selected] ,x='built_up_area',y='price',color='bedRoom')
st.plotly_chart(fig1,use_container_width=True)


# bar graph showing the bhk for selected sector
st.title("📊 BHK Distribution by Sector")
sector_options = df['sector'].unique().tolist()
sector_options.insert(0,'overall')
sector_selected = st.selectbox('Sector',sector_options)
if sector_selected == 'overall':
    piechart = px.pie(df, names='bedRoom', title='Overall BHK Distribution')
else:
    piechart = px.pie(df[df['sector']==sector_selected],names='bedRoom')
st.plotly_chart(piechart)


# side by side boxplot to compare the prices of properties
st.title("Comparing prices of properties")
temp_df = df[df['bedRoom']<=4]
boxplot = px.box(temp_df , x = 'bedRoom',y='price')
st.plotly_chart(boxplot)


st.title("📈 KDE Plot of Property Prices")

# Create centered columns: left, center, right
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    fig, ax = plt.subplots(figsize=(5, 2))  # Smaller width & height
    sns.kdeplot(df[df['property_type'] == 'house']['price'], label='House', ax=ax)
    sns.kdeplot(df[df['property_type'] == 'flat']['price'], label='Flat', ax=ax)

    ax.set_title('Price Distribution by Property Type')
    ax.set_xlabel('Price')
    ax.set_ylabel('Density')
    ax.legend()

    st.pyplot(fig)
