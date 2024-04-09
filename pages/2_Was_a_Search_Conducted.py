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

## Boxplot
age_box = sns.boxplot(stops, x='Was_a_Search_Conducted', y='Driver_Age')
age_box.set_title('Boxplot: Was a Search Conducted & Age of Driver')
age_box.set_xlabel('Was a Search Conducted: Y/N')
age_box.set_ylabel('Age of Driver in Years')

st.pyplot(age_hist.get_figure())