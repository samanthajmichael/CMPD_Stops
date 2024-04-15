import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

st.title('CMPD Searches Conducted')

@st.cache_data
def load_data(csv):
    df= pd.read_csv(csv)
    return df

stops = load_data('data/Officer_Traffic_Stops.csv')

# Calculate the Search counts for yes and no
search_counts = stops['Was_a_Search_Conducted'].value_counts().reset_index()

# Rename the columns
search_counts.columns = ['Was_a_Search_Conducted', 'count']

# Altair Bar Chart
alt_search = (
    alt.Chart(search_counts)
    .mark_bar()
    .encode(
        x=alt.X('Was_a_Search_Conducted', title='Search Conducted'),
        y=alt.Y('count', title='Number of Searches'),
        color=alt.Color('Was_a_Search_Conducted', title='Search Conducted'),
        tooltip=[
            alt.Tooltip('Was_a_Search_Conducted', title='Search Conducted:'),
            alt.Tooltip('count', title='Count:')]
    )
    .properties(width=400)
)

# Add text labels
alt_search_text = alt_search.mark_text(
    align='center',
    baseline='bottom',
    dx=0,
    dy=-5
).encode(
    text=alt.Text('count:Q')
)

alt_search_combined = alt.layer(alt_search, alt_search_text)
st.altair_chart(alt_search_combined, use_container_width=True)

## Boxplot
age_box = sns.boxplot(stops, x='Was_a_Search_Conducted', y='Driver_Age', hue='Was_a_Search_Conducted')
age_box.set_xlabel('Was a Search Conducted: Y/N')
age_box.set_ylabel('Age of Driver in Years')

st.pyplot(age_box.get_figure())