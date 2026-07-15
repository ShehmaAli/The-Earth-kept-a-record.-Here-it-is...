import streamlit as st
import plotly.express as px
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, \
    heatmap_cities, get_ranks

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_heatmap_cities = heatmap_cities(Allcities)
cities_in_anomalies = to_anomalies(all_heatmap_cities)
city_ranks_df, country_ranks_df = get_ranks(cities_in_anomalies, clean_world_data, one_country_name(clean_world_data))

st.set_page_config("Heat Ranking", "🌎", layout="wide")
st.title("🌎 Heat Ranking", text_alignment="center")
st.markdown("<p style='color:#9ae7fc;'>Who is heating up the most?? Who warmed up the most?? See the top 20 countries and cities in seconds!!</p>",
            unsafe_allow_html=True, text_alignment="center"
            )

st.divider()

def graph3(type, csv, order):
    if type == "City":
        if order == "Lowest warming":
            csv = csv.sort_values(
                by="Increase",
                ascending = False
            )
        if order == "Highest warming":
            csv = csv.sort_values(
                by="Increase",
                ascending=True
            )
    else:
        if order == "Highest warming":
            csv = csv.sort_values(
                by="Increase",
                ascending=True
            )
        if order == "Lowest warming":
            csv = csv.sort_values(
                by="Increase",
                ascending=False
            )

    csv = csv.iloc[:15]
    if type == "City":
        if order == "Highest warming":
            title = "Top 15 cities with the Highest warming"
        else:
            title = "Top 15 cities with the Lowest warming"
        fig = px.bar(csv, x="Increase", y="Location", orientation="h", title=title, color="Increase",
                         color_continuous_scale="RdYlBu_r")
        fig.update_layout(coloraxis_showscale=False)


    if type == "Country":
        if order == "Highest warming":
            title = "Top 15 countries with the Highest warming"
        else:
            title = "Top 15 countries with the Lowest warming"

        fig = px.bar(csv, x="Increase", y="Entity", orientation="h", title=title, color="Increase",
                    color_continuous_scale="RdYlBu_r")
        fig.update_layout(coloraxis_showscale=False)



    return fig


col1, col2 = st.columns([1.5,1])

with col1:
    with st.container(border=True, height=365):
        st.markdown("### Start by selecting a category:", text_alignment="center")
        st.write(" ")

        type_choices = ["City", "Country"]
        warming_choices = ["Unsorted", "Highest warming", "Lowest warming"]

        with st.container(border= True, height=120):
            category = st.radio("Choose: ", type_choices)

        with st.container(border=True, height=125):
            temp_change = st.radio("Sort by ⬇️", warming_choices)

with col2:
    with st.container(border= True, height=265):
        st.markdown("### What is Temperature Anomaly??")
        st.markdown(
            "<p style='color:#c4f2ff;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
        )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")


st.divider()

if category == "City":
    fig = graph3(category, city_ranks_df, temp_change)
    st.plotly_chart(fig)
    st.divider()
if category == "Country":
    fig = graph3(category, country_ranks_df, temp_change)
    st.plotly_chart(fig)
    st.divider()