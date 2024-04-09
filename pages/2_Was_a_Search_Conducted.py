import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('CMPD Traffic Stops by Age')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')

## Histogram
age_hist = sns.histplot(stops, x='Driver_Age', kde=True, bins=50)
age_hist.set_title('Distribution of Driver Age (bins: 50)')
age_hist.set_xlabel('Driver Age in Years')
age_hist.set_xticks(range(0,100, 5))

st.pyplot(age_hist.get_figure())