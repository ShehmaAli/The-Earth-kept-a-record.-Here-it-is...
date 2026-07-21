# LIBRARIES :)
# importing the required libraries
import streamlit as st
import random
import plotly.express as px

# getting the functions from the file data_clean.py
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, to_one_df, extract_countries

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
cities_in_anomalies = to_anomalies(Allcities)

# setting up the webpage information for this graph
st.set_page_config("Climate Comparison", "🌡️", layout="wide")

st.title("🌡️ Climate Comparison", text_alignment="center")
st.markdown("<p style='color:#c2fcf7;'>Pick multiple cities and see who warmed up fastest. Take a guess!!!</p>",
            unsafe_allow_html=True, text_alignment="center"
            )

# using st.divider to put a divider and make the page clean
st.divider()

# MAIN FUNCTION :)
# this is basically the main function that gives the graph
def graph2(type, csv):
    # getting the parameters for the graph2 function and generating the figure according to it
    if type == "City":
        years = csv["YEAR"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected cities"
        # making the graph using px.line
        fig = px.line(csv, years, temps, title=final_title, color="Location")
    if type == "Country":
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected countries"
        # making the graph using px.line
        fig = px.line(csv, years, temps, title=final_title, color="Entity")

    # returning the figure
    return fig


# using st.columns to make columns both of different sizes
col1, col2 = st.columns([1.5, 1])

with col1:
    # displaying the selection card which selects the category
    with st.container(border=True, height=265):
        st.markdown("## Start by selecting a category ", text_alignment="center")
        st.write(" ")
        with st.container(border=True, height=120):
            choices = ["City", "Country"]
            answer = st.radio("Select among this", choices)

with col2:
    # displaying the card showing the defination of temperature anomaly
    # using html,css for the different colors
    with st.container(border=True, height=265):
        st.markdown("### What is Temperature Anomaly??")
        st.markdown(
            "<p style='color:#c4fffa;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
        )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")

# if the category is City then the user is displayed to whether get 7 unknown random cities or to select upto 7 cities themselves
if answer == "City":
    with col2:
        # displaying to ask about the random option
        with st.container(border=True, height=140):
            st.markdown("### 🎲 Surprise Me!!!", text_alignment="center")
            need_random = st.button("🎲 Random City/Country")

    st.divider()

    # also displaying the multiselect for cities if the random option is not chosen
    if not need_random:
        user_cites = st.multiselect("Cities", list(all_cities.keys()), max_selections=7)

        st.divider()

        # starting to call the graph2 function inorder to generate a graph when there are two or more selections
        if len(user_cites) >= 2:
            selected_df = to_one_df(user_cites, cities_in_anomalies)
            fig = graph2(answer, selected_df)

            # displaying the graph on the webpage using streamlit
            st.plotly_chart(fig, use_container_width=True)

    # if the random option is chosen then:
    else:
        # 7 random cities are chosen and then the graph2 function is called

        random_cities = random.sample(list(all_cities.keys()), 7)
        selected_df_random = to_one_df(random_cities, cities_in_anomalies)
        fig = graph2(answer, selected_df_random)
        # displaying the graph on the webpage using streamlit
        st.plotly_chart(fig, use_container_width=True)

# if the category is Country then the user is displayed to whether get 7 unknown random countries or to select upto 7 countries themselves
if answer == "Country":
    with col2:
        # displaying to ask about the random option
        with st.container(border=True, height=130):
            st.markdown("## 🎲 Surprise Me!!!", text_alignment="center")
            need_random = st.button("🎲 Random City/Country")

    st.divider()

    # also displaying the multiselect for cities if the random option is not chosen
    if not need_random:
        user_countries = st.multiselect("Countries", one_country_name(clean_world_data), max_selections=7)

        st.divider()

        # starting to call the graph2 function inorder to generate a graph when there are two or more selections
        if len(user_countries) >= 2:
            selected_df_countries = extract_countries(user_countries, clean_world_data)
            fig = graph2(answer, selected_df_countries)
            # displaying the graph on the webpage using streamlit
            st.plotly_chart(fig, use_container_width=True)
    else:
        # 7 random countries are chosen and then the graph2 function is called
        random_countries = random.sample(one_country_name(clean_world_data), 7)
        selected_df_random = extract_countries(random_countries, clean_world_data)
        fig = graph2(answer, selected_df_random)

        # displaying the graph on the webpage using streamlit
        st.plotly_chart(fig, use_container_width=True)
