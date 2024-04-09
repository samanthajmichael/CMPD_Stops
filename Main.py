import streamlit as st
import pandas as pd

st.title('CMPD Traffic Stops')
st.write('Investigating traffic stops conducted by CMPD from 2016-2017 in Charlotte, NC')
@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')

st.dataframe(stops, use_container_width=True)