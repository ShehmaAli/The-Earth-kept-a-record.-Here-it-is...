"""
GRAPHS AND TYPES:
1: Indiviual City/country line graph seperately
2: all cities/ countries comparison seperately
3: Total warming bar chart seperately
4: Decade heatmap seperately
5: Regression future predictor
"""

# LIBRARY :)
# imported streamlit to make up the homepage
import streamlit as st

# setting up the main web homepage using streamlit
st.set_page_config("Earth Kept a Record. Here it is!!", "🌎", layout="wide")

# the title and description of the page
st.title("&#127758; Earth Kept a :red[Record]. Here it is!!", text_alignment="center")
st.markdown("### 80 years of climate change shown easily", text_alignment="center")

# using st.divider to put a divider and make the page clean
st.divider()

# the quick summary about the data of the web application
st.markdown("## Let's see the Earth's record: ", text_alignment="center")

# using st.columns to make the data split into 3 equal columns
column1, column2, column3 = st.columns(3, gap="medium", vertical_alignment="top")

# using st.metric to display mini information cards being visually good
with column1:
    st.metric("Years of data", ":blue[80+]")
with column2:
    st.metric("Visualisations", ":red[5]")
with column3:
    st.metric("Countries", " :green[200+]")

# using st.divider to put a divider and make the page clean
st.divider()

# Create navigation cards for each visualisation.
with column1:
    with st.container(border=True, vertical_alignment="bottom", height=250):
        # using some html, css for the color
        st.markdown(
            "<h2 style='color:#45ffb8;'>📈 Temperature Trends</h2>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='color:#a8ffde;'>See the temperatures changes over 80+ years for any country or city. </p>",
            unsafe_allow_html=True

            )
        st.write("")
        st.page_link("pages/graph1.py", label="Explore Now")
with column2:
    with st.container(border=True, vertical_alignment="bottom", height=250):
        # using some html, css for the color
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
    with st.container(border=True, vertical_alignment="bottom", height=250):
        # using some html, css for the color
        st.markdown(
            "<h2 style='color:#45d7ff;'>🌎 Heat Ranking</h2>",
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(
            "<p style='color:#9ae7fc;'>Who is heating up the most?? Who warmed up the most?? See the top 20 countries and cities in seconds!!</p>",
            unsafe_allow_html=True

            )
        st.write("")
        st.page_link("pages/graph3.py", label="View Ranking!!")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True, vertical_alignment="center", height=250):
        # using some html, css for the color
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
    with st.container(border=True, vertical_alignment="center", height=250):
        # using some html, css for the color
        st.markdown(
            "<h2 style='color:#7045ff;'>🔮 Future Temperature Prediction</h2>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='color:#c6b5ff;'>See what the future looks like yourself with the magic of machine learning :) </p>",
            unsafe_allow_html=True)
        st.write("")
        st.page_link("pages/graph5.py", label="Let's see the future!!!")

# using st.divider to put a divider and make the page clean
st.divider()

# displaying the about section
st.markdown("## About:")
st.markdown("The Earth Kept a Record transforms over 80 years of real climate data "
            "into an interactive experience. Explore temperature trends, compare cities and countries, "
            "uncover climate patterns, and discover what Earth's data has to "
            "say, all through beautiful, easy-to-use visualizations.")
st.write("")

# using some html, css for the color
st.markdown("<p style='color:#d1ffee;'>Every graph is the reflections of our actions. </p>",
            unsafe_allow_html=True)

# using st.divider to put a divider and make the page clean
st.divider()

# providing the link to this project's github repository
st.markdown("## Curious to explore more 🤔???", text_alignment="center")
st.markdown("### 📂 Let's go to explore the GitHub Repository", text_alignment="center")
st.page_link("https://github.com/ShehmaAli/The-Earth-kept-a-record.-Here-it-is...", label="Let's go!!", width="stretch")
