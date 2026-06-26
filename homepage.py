"""
TODO
1: clean CSVs by cities and countries side by side
2: set up graphs designs
3: set up the web application by streamlit
4: make the future graph using regression
5: ship the project

TOTAL countries and cites = 10 countries and 10 cites
"""

import streamlit as st

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



