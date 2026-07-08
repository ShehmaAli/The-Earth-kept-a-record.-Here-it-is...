import streamlit as st
import plotly.express as px
from data_clean import load_data, clean_csvs, one_country_name

world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)


def graph1(type, csv, name):
    if type == "City":
        years = csv["YEAR"]
        temps = csv["metANN"]
        final_title = f"Average annual temperature in {name}"
    if type == "Country":
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in {name}"

    fig = px.line(csv, x=years, y=temps, title= final_title)

    return fig


st.title("Welcome to Graph 1 :party:")

st.markdown("## Choose the following")

choices = ["City", "Country"]

answer = st.radio("Choose: ", choices)

if answer == "City":
    city_choosen = st.selectbox("City", ["Select any option"] + list(Allcities.keys()))
    if city_choosen != "Select any option":
        fig = graph1(answer, all_cities[city_choosen], city_choosen)
        fig.update_layout(
            margin=dict(l=50, r=20, t=40, b=40),
            autosize=True
        )
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

if answer == "Country":

    country_choosen = st.selectbox("Country", ["Select any option"] + one_country_name(clean_world_data))
    if country_choosen != "Select any option":
        fig = graph1(answer, clean_world_data[clean_world_data["Entity"] == country_choosen], country_choosen)
        fig.update_layout(
            margin=dict(l=50, r=20, t=40, b=40),
            autosize=True
        )
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
