import streamlit as st
import pandas as pd

st.title('CMPD Traffic Stops')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')

st.dataframe(stops, width=800, height=400)