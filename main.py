"""
TODO
1: clean CSVs by cities and countries side by side
2: set up graphs designs
3: set up the web application by streamlit
4: make the future graph using regression
5: ship the project

TOTAL countries and cites = 10 countries and 10 cites
"""

import numpy as np
import pandas as pd
import streamlit as st


# checking for any empty values in each of the CSVs
# All the selected countries in the world
world_data = pd.read_csv("Weather station csv/World_data.csv")

# CSVs of the selected cities
multan = pd.read_csv("Weather station csv/multan.csv")
delhi = pd.read_csv("Weather station csv/delhi.csv")
london = pd.read_csv("Weather station csv/london.csv")
new_york = pd.read_csv("Weather station csv/new york.csv")
beijing = pd.read_csv("Weather station csv/beijing.csv")
sydney = pd.read_csv("Weather station csv/sydney.csv")
tokyo = pd.read_csv("Weather station csv/tokyo.csv")
paris = pd.read_csv("Weather station csv/paris.csv")
dubai = pd.read_csv("Weather station csv/dubai.csv")
nuuk = pd.read_csv("Weather station csv/nuuk.csv")

# making a list and the then it can be used for multiple things
All_cities = [multan, delhi, london, new_york, beijing, sydney, tokyo, paris, dubai, nuuk]

# another list from which the user can choose the graph for cities from
All_cities_str = ["multan", "delhi", "london", "new york", "beijing", "sydney", "tokyo", "paris", "dubai", "nuuk"]

for i in All_cities:
    i.replace(999.90, np.nan, inplace=True)
    i["metANN"] = i["metANN"].interpolate(method="linear")

# setting up web app using streamlit
st.title("&#127758; Earth Kept a :red[Record]. Here it is!!")
st.markdown("### 80 years of climate change shown easily", text_alignment="center")

st.markdown("# User's choose from the following: ", text_alignment="center")

st.set_page_config("Earth Kept a Record. Here it is!!", layout="centered")

left_column, right_column = st.columns(2, gap= "medium", vertical_alignment="top")

with left_column:
    st.page_link("pages/graph1.py", label="Graph 1")
    st.page_link("pages/graph3.py", label="Graph 3")
    st.page_link("pages/graph5.py", label="Graph 5")

with right_column:
    st.page_link("pages/graph2.py", label="Graph 2")
    st.page_link("pages/graph4.py", label="Graph 4")


# GRAPHS AND TYPES:
# 1: Indiviual City/country line graph seperately
# 2: all cities/ countries comparison seperately
# 3: Total warming bar chart seperately
# 4: Decade heatmap seperately
# 5: Regression future predictor


