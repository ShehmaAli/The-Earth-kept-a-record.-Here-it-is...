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
st.set_page_config("Earth Kept a Record. Here it is!!", "🌎", layout="wide")
st.title("&#127758; Earth Kept a :red[Record]. Here it is!!", text_alignment="center")
st.markdown("### 80 years of climate change shown easily", text_alignment="center")

st.divider()

st.markdown("## Let's see the Earth's record: ", text_alignment="center")

column1, column2, column3 = st.columns(3, gap="medium", vertical_alignment="top")

with column1:
    st.metric("Years of data", ":blue[80+]")
with column2:
    st.metric("Visualisations", ":red[5]")
with column3:
    st.metric("Countries", " :green[200+]")

st.divider()

with column1:
    with st.container(border=True, vertical_alignment= "bottom"):
        st.markdown(
            "<h2 style='color:#45ffb8;'>📈 Temperature Trends</h2>",
            unsafe_allow_html=True
        )
        st.markdown("<p style='color:#a8ffde;'>See the temperatures changes over 80+ years for any country or city. </p>",
            unsafe_allow_html=True

        )
        st.write("")
        st.page_link("pages/graph1.py", label="Explore Now")
with column2:
    with st.container(border=True, vertical_alignment= "bottom"):
        st.markdown(
            "<h2 style='color:#45ffec;'>🌡️ Climate Comparison</h2>",
            unsafe_allow_html=True
        )
        st.markdown("<p style='color:#aafaf2;'>Pick multiple cities and see who warmed up fastest. Take a guess!!!</p>",
            unsafe_allow_html=True

        )
        st.write("")
        st.page_link("pages/graph2.py", label="Start Comparing!!!")
with column3:
    with st.container(border=True, vertical_alignment= "bottom"):
        st.markdown(
            "<h2 style='color:#45d7ff;'>🌎 Heat Ranking</h2>",
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown("<p style='color:#9ae7fc;'>Who is heating up the most?? Who warmed up the most?? See the top 20 countries and cities in seconds!!</p>",
            unsafe_allow_html=True

        )
        st.write("")
        st.page_link("pages/graph3.py", label="View Ranking!!")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True, vertical_alignment= "bottom"):
        st.markdown(
             "<h2 style='color:#457dff;'>🗺️ Temperature Heatmap</h2>",
                     unsafe_allow_html=True)
        st.write("")
        st.markdown(
            "<p style='color:#86aafc;'>Watch climate change unfold decade by decade with an interactive heatmap.Maybe your country is the hottest who knows??!</p>",
            unsafe_allow_html=True)
        st.write("")
        st.page_link("pages/graph4.py", label="Open heatmap")
with col2:
    with st.container(border=True, vertical_alignment= "bottom"):
        st.markdown(
             "<h2 style='color:#7045ff;'>🔮 Future Temperature Prediction</h2>",
                     unsafe_allow_html=True)
        st.markdown(
            "<p style='color:#c6b5ff;'>See what the future looks like yourself with the magic of machine learning :) </p>",
            unsafe_allow_html=True)
        st.write("")
        st.page_link("pages/graph5.py", label="Let's see the future!!!")

st.divider()

st.markdown("## About:")
st.markdown("The Earth Kept a Record transforms over 80 years of real climate data "
            "into an interactive experience. Explore temperature trends, compare cities and countries, "
            "uncover climate patterns, and discover what Earth's data has to "
            "say, all through beautiful, easy-to-use visualizations.")
st.write("")
st.markdown("<p style='color:#d1ffee;'>Every graph is the reflections of our actions. </p>",
            unsafe_allow_html=True)

st.divider()

st.markdown("## Curious to explore more 🤔???")
st.write("")
st.page_link("pages/moreinfo.py", label="Let's go!!")


# GRAPHS AND TYPES:
# 1: Indiviual City/country line graph seperately
# 2: all cities/ countries comparison seperately
# 3: Total warming bar chart seperately
# 4: Decade heatmap seperately
# 5: Regression future predictor
