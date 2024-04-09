import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

st.title('CMPD Traffic Stops by Department')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')
stops['Month_of_Stop'] = stops['Month_of_Stop'].astype('datetime64[ns]')
stops['Month_of_Stop'] = pd.to_datetime(stops['Month_of_Stop'], format='%y%m%d')

# Facet plot for division stops
## create the dataframe that groups by month and division
stops_count = stops.groupby(['Month_of_Stop', 'CMPD_Division']).size().reset_index(name='Count')
stops_count['Month_of_Stop'] = stops_count['Month_of_Stop'].dt.strftime('%m-%Y')

# Convert 'Month_of_Stop' to datetime
stops_count['Month_of_Stop'] = pd.to_datetime(stops_count['Month_of_Stop'])

# Sort the DataFrame by 'Month_of_Stop' in ascending order
stops_count = stops_count.sort_values(by='Month_of_Stop', ascending=True)

base = alt.Chart(stops_count).mark_line().encode(
    x=alt.X('Month_of_Stop:T', axis=alt.Axis(format='%b-%Y', title='Date of Stop', labelAngle=-90)),
    y=alt.Y('Count:Q', axis=alt.Axis(title='Number of Stops')),
    color='CMPD_Division'
).properties(
    width=200,
    height=200
).facet(
    column=alt.Column('CMPD_Division:N', header=alt.Header(labelAngle=-90), columns=5)
).resolve_scale(y='independent')

st.altair_chart(base, use_container_width=True)
