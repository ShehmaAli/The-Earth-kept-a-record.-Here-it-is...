import streamlit as st
import plotly.express as px
from data_clean import load_data, clean_csvs, one_country_name

world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)


st.set_page_config("Temperature Trends", "📈", layout="wide")
st.title("📈 Temperature Trends", text_alignment= "center")
st.markdown("<p style='color:#a8ffde;'>Explore the temperatures changes over 80+ years for any country or city individually. </p>",
            unsafe_allow_html=True, text_alignment="center"

        )

st.divider()


def graph1(type, csv, name):
    if type == "City":
        years = csv["YEAR"]
        temps = csv["metANN"]
        final_title = f"Average annual temperature in {name}"
    if type == "Country":
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in {name}"

    fig = px.line(csv, x=years, y=temps, title= final_title , color_discrete_sequence= ["orangered"])

    return fig

col1, col2 = st.columns([1.5, 1])

with col1:
    with st.container(border= True):
        st.markdown(
            "<h2 style='color:#a6ffe6;'> Start by selecting a category </h2>",
            unsafe_allow_html=True, text_alignment="center"
            )
        with st.container(border= True):
            choices = ["City", "Country"]
            answer = st.radio("Choose:                           ", choices)

with col2:
    with st.container(border= True):
        st.markdown("### What is temperature anomaly??")
        st.markdown("<p style='color:#9afcd7;'> A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
        )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")


st.divider()

if answer == "City":
    city_choosen = st.selectbox("City", ["Select any option"] + list(Allcities.keys()))

    st.divider()


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

    st.divider()

    if country_choosen != "Select any option":
        fig = graph1(answer, clean_world_data[clean_world_data["Entity"] == country_choosen], country_choosen)
        fig.update_layout(
            margin=dict(l=50, r=20, t=40, b=40),
            autosize=True
        )
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
