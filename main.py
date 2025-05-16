import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.error import URLError

# Set page config and title
st.set_page_config(
    page_title="Cancer Frequency Analysis",
    page_icon="📊",
    layout="wide"
)

# Add title and description
st.title("🌍 Global Cancer Frequency Analysis")
st.markdown("""
This dashboard visualizes cancer rates across different countries, helping to understand
the global distribution of cancer frequencies.
""")

# Define continent mapping
continent_mapping = {
    'Australia': 'Oceania',
    'New Zealand': 'Oceania',
    'Ireland': 'Europe',
    'Hungary': 'Europe',
    'United States': 'North America',
    'Belgium': 'Europe',
    'France': 'Europe',
    'Denmark': 'Europe',
    'Norway': 'Europe',
    'Netherlands': 'Europe',
    'Canada': 'North America',
    'France(New Caledonia)': 'Oceania',
    'United Kingdom': 'Europe',
    'South Korea': 'Asia',
    'Germany': 'Europe',
    'Switzerland': 'Europe',
    'Luxembourg': 'Europe',
    'Serbia': 'Europe',
    'Slovenia': 'Europe',
    'Latvia': 'Europe',
    'Slovakia': 'Europe',
    'Czech Republic': 'Europe',
    'Sweden': 'Europe',
    'Italy': 'Europe',
    'Croatia': 'Europe',
    'Lithuania': 'Europe',
    'Estonia': 'Europe',
    'Greece': 'Europe',
    'Spain': 'Europe',
    'Finland': 'Europe',
    'Uruguay': 'South America',
    'Belarus': 'Europe',
    'Portugal': 'Europe',
    'Iceland': 'Europe',
    'France(Guadeloupe)': 'North America',
    'United States(Puerto Rico)': 'North America',
    'Moldova': 'Europe',
    'Poland': 'Europe',
    'Cyprus': 'Europe',
    'France(Martinique)': 'North America',
    'Malta': 'Europe',
    'Singapore': 'Asia',
    'Japan': 'Asia',
    'Austria': 'Europe',
    'Barbados': 'North America',
    'France(French Guiana)': 'South America',
    'Bulgaria': 'Europe',
    'Lebanon': 'Asia',
    'France(French Polynesia)': 'Oceania'
}

try:
    # Load and display data
    df = pd.read_csv("Cancer frequency.csv")
    
    # Add continent information
    df['Continent'] = df['Country'].map(continent_mapping)
    
    # Add a container for the chart
    with st.container():
        st.subheader("Cancer Rates by Country")
        
        # Create a Plotly bar chart
        fig = px.bar(
            df,
            x='Country',
            y='Cancer rate',
            color='Continent',
            title='Cancer Rates by Country and Continent',
            labels={'Cancer rate': 'Cancer Rate (per 100,000)', 'Country': 'Country'},
            height=600
        )
        
        # Customize the layout
        fig.update_layout(
            xaxis_tickangle=-45,
            showlegend=True,
            legend_title_text='Continent',
            plot_bgcolor='white',
            margin=dict(b=100)  # Add bottom margin for rotated labels
        )
        
        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
        
        # Add data source citation
        st.caption("Data source: Cancer frequency dataset")
        
except URLError as e:
    st.error(f"⚠️ This demo requires internet access. Connection error: {e.reason}")