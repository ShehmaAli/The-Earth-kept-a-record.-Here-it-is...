# LIBRARIES :|
# importing required libraries
import streamlit as st
import random
import plotly.express as px
import plotly.graph_objects as go
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, to_one_df, extract_countries, \
    heatmap_cities

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_heatmap_cities = heatmap_cities(Allcities)
cities_in_anomalies = to_anomalies(all_heatmap_cities)

# WEB PAGE using streamlit

# the title and some necesesties this webpage

st.set_page_config("Temperature Heatmap", "🗺️", layout="wide")
st.title("🗺️ Temperature Heatmap", text_alignment="center")
st.markdown("<p style='color:#a2bdfc;'>Watch climate change unfold decade by decade with an interactive heatmap.Maybe your country is the hottest who knows??!</p>",
            unsafe_allow_html=True, text_alignment="center"
            )

st.divider()
def graph4(type, csv):
    if type == "City":
        csv["Decade"] = (csv["YEAR"] // 10) * 10
        final_df = csv.groupby(
            ["Location", "Decade"]
        )["Temperature anomaly"].mean().reset_index()
        heatmap_df = final_df.pivot(
            index="Location",
            columns="Decade",
            values="Temperature anomaly"
        )
    else:
        csv["Decade"] = (csv["Year"] // 10) * 10
        final_df = csv.groupby(
            ["Entity", "Decade"]
        )["Temperature anomaly"].mean().reset_index()
        heatmap_df = final_df.pivot(
            index="Entity",
            columns="Decade",
            values="Temperature anomaly"
        )
    fig = px.imshow(heatmap_df, color_continuous_scale="RdBu_r", aspect="auto", text_auto= True)
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
            "<p style='color:#a2bdfc;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
            )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")


if answer == "City":
    with col2:
        with st.container(border=True, height=140):
            st.markdown("### 🎲 Surprise Me!!!")
            need_random = st.button("🎲 Random City/Country")

    st.divider()

    if not need_random:
        user_cites = st.multiselect("Cities", list(all_heatmap_cities.keys()), max_selections=10)

        st.divider()
        if len(user_cites) >= 2:
            selected_df = to_one_df(user_cites, cities_in_anomalies)
            fig = graph4(answer, selected_df)
            fig.update_layout(
                xaxis_title="Year",
                yaxis_title="Location",
                plot_bgcolor="black",
                paper_bgcolor="black"
            )
            st.plotly_chart(fig, use_container_width=True)
    else:
        random_cities = random.sample(list(all_heatmap_cities.keys()), 10)
        selected_df_random = to_one_df(random_cities, cities_in_anomalies)
        fig = graph4(answer, selected_df_random)
        st.plotly_chart(fig, use_container_width=True)

if answer == "Country":
    with col2:
        with st.container(border=True, height=140):
            st.markdown("### 🎲 Surprise Me!!!")
            need_random = st.button("🎲 Random City/Country")

    st.divider()

    if not need_random:
        user_countries = st.multiselect("Countries", one_country_name(clean_world_data), max_selections=10)
        st.divider()

        if len(user_countries) >= 2:
            selected_df_countries = extract_countries(user_countries, clean_world_data)
            fig = graph4(answer, selected_df_countries)
            st.plotly_chart(fig, use_container_width=True)
    else:
        random_countries = random.sample(one_country_name(clean_world_data), 10)
        selected_df_random = extract_countries(random_countries, clean_world_data)
        fig = graph4(answer, selected_df_random)
        st.plotly_chart(fig, use_container_width=True)
