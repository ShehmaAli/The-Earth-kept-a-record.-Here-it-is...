import streamlit as st
import random
import plotly.express as px
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, to_one_df, extract_countries

world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
cities_in_anomalies = to_anomalies(Allcities)

st.set_page_config("Climate Comparison", "🌡️", layout="wide")


st.title("🌡️ Climate Comparison", text_alignment="center")
st.markdown("<p style='color:#c2fcf7;'>Pick multiple cities and see who warmed up fastest. Take a guess!!!</p>",
            unsafe_allow_html=True, text_alignment="center"

        )

st.divider()

def graph2(type, csv):
    if type == "City":
        years = csv["YEAR"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected cities"
        fig = px.line(csv, years, temps, title=final_title, color="Location")
    if type == "Country":
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected countries"
        fig = px.line(csv, years, temps, title=final_title, color="Entity")


    return fig


col1, col2 = st.columns([1.5, 1])

with col1:
    with st.container(border=True, height=265):
        st.markdown("## Start by selecting a category ", text_alignment="center")
        st.write(" ")

        with st.container(border=True, height=120):
            choices = ["City", "Country"]
            answer = st.radio("Select among this", choices)

with col2:
    with st.container(border= True, height= 265):
        st.markdown("### What is Temperature Anomaly??")
        st.markdown(
            "<p style='color:#c4fffa;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
            )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")

if answer == "City":
    with col2:
        with st.container(border= True, height= 140):
            st.markdown("### 🎲 Surprise Me!!!", text_alignment="center")
            need_random = st.button("🎲 Random City/Country")

    st.divider()
    if not need_random:
        user_cites = st.multiselect("Cities", list(all_cities.keys()), max_selections=7)

        st.divider()

        if len(user_cites) >= 2:
            selected_df = to_one_df(user_cites, cities_in_anomalies)
            fig = graph2(answer, selected_df)
            st.plotly_chart(fig, use_container_width=True)
    else:
        random_cities = random.sample(list(all_cities.keys()), 7)
        selected_df_random = to_one_df(random_cities, cities_in_anomalies)
        fig = graph2(answer, selected_df_random)
        st.plotly_chart(fig, use_container_width=True)

if answer == "Country":
    with col2:
        with st.container(border=True, height= 130):
            st.markdown("## 🎲 Surprise Me!!!", text_alignment="center")
            need_random = st.button("🎲 Random City/Country")

    st.divider()

    if not need_random:
        user_countries = st.multiselect("Countries", one_country_name(clean_world_data), max_selections=7)

        st.divider()

        if len(user_countries) >= 2:
            selected_df_countries = extract_countries(user_countries, clean_world_data)
            fig = graph2(answer, selected_df_countries)
            st.plotly_chart(fig, use_container_width=True)
    else:
        random_countries = random.sample(one_country_name(clean_world_data), 7)
        selected_df_random = extract_countries(random_countries, clean_world_data)
        fig = graph2(answer, selected_df_random)
        st.plotly_chart(fig, use_container_width= True)
