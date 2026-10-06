import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
)
st.write("How do passenger class, sex, and age group affect survival on the Titanic?")
# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)


st.write(
'''
# Titanic Visualization 2
'''
)
st.write("How does family size affect fare across different passenger classes?")
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)
st.write("The most common last names in the Titanic dataset are:")
st.write(last_names().head(10))

