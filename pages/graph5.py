import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, heatmap_cities, predict

world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_heatmap_cities = heatmap_cities(Allcities)
cities_in_anomalies = to_anomalies(all_heatmap_cities)

st.set_page_config("Future Temperature Prediction", "🔮", layout="wide")
st.title("🔮 Future Temperature Prediction", text_alignment="center")
st.markdown("<p style='color:#c6b5ff;'>See what the future looks like yourself with the magic of machine learning :) </p>",
            unsafe_allow_html=True, text_alignment="center")

st.divider()

def graph5(type, historic_csv, future_csv, name, prediction_year):
    new_years = future_csv["Year"]
    predicted_values = future_csv["Prediction"]
    historic_values = historic_csv["Temperature anomaly"]
    if type == "City":
        title = f"Predicted temperature anomalies in {name} till {prediction_year}"
        old_years = historic_csv["YEAR"]
    else:
        title = f"Predicted temperature anomalies in {name} till {prediction_year}"
        old_years = historic_csv["Year"]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=old_years,
            y=historic_values,
            mode="lines",
            name="Historical Data",
            line=dict(color="royalblue", width=3)
        )
    )
    fig.add_trace(
        go.Scatter(
            x=new_years,
            y=predicted_values,
            mode="lines",
            name="Prediction",
            line=dict(color="red", dash="dash", width=3)
        )
    )

    fig.update_layout(
        margin=dict(l=50, r=20, t=40, b=40),
        autosize=True,
        title=title,
        xaxis_title="Year",
        yaxis_title="Temperature Anomaly (°C)"
    )
    fig.update_xaxes(tickangle=45)

    return fig

col1, col2 = st.columns([1.5,1])

with col1:
    with st.container(border= True, height=235):
        st.markdown("## Start by selecting a category:", text_alignment="center")
        st.write(" ")

        choices = ["City", "Country"]

        answer = st.radio("Choose: ", choices)

with col2:
    with st.container(border=True, height=235):
        st.markdown("### What is Temperature Anomaly??")
        st.markdown(
            "<p style='color:#c6b5ff;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
            unsafe_allow_html=True, text_alignment="center"
        )
        st.markdown("🟥 Positive (+) = Warmer than average")
        st.markdown("🟦 Negative (−) = Cooler than average")





if answer == "City":
    with col1:
        with st.container(border=True,height=200):
            st.markdown("### Choose your city", text_alignment="center")
            st.write("")
            city_choosen = st.selectbox("City", ["Select any option"] + list(all_heatmap_cities.keys()))

    with col2:
        with st.container(border=True, height=200):
            st.title("⚠️ Disclaimer", text_alignment="center")
            st.markdown(
                "<p style='color:#c6b5ff;'>This is graph is made for Educational purposes only and is not suppose to be replaced with any scientific research</p>",
                unsafe_allow_html=True, text_alignment="center"
            )

    st.divider()

    with st.container(border=True):
        st.markdown("## Till when do you want the prediction???", text_alignment="center")
        end_year = st.slider("Years", 2025, 2060)

    st.divider()

    if city_choosen != "Select any option":
        final_df = predict(answer, cities_in_anomalies[city_choosen], end_year)
        fig = graph5(answer, cities_in_anomalies[city_choosen], final_df, city_choosen, end_year)
        st.plotly_chart(fig, use_container_width=True)


if answer == "Country":
    with col1:
        with st.container(border=True, height=200):
            st.markdown("### Choose your country:", text_alignment="center")
            st.write("")
            country_choosen = st.selectbox("Country", ["Select any option"] + one_country_name(clean_world_data))

    with col2:
        with st.container(border=True, height=200):
            st.title("⚠️ Disclaimer", text_alignment="center")
            st.markdown(
                "<p style='color:#c6b5ff;'>This is graph is made for Educational purposes only and is not suppose to be replaced with any scientific research</p>",
                unsafe_allow_html=True, text_alignment="center"
                )
    with st.container(border=True):
        st.markdown("## Till when do you want the prediction??", text_alignment="center")
        end_year = st.slider("Years", 2025, 2060)
    st.divider()
    if country_choosen != "Select any option":
        final_df = predict(answer, clean_world_data[clean_world_data["Entity"] == country_choosen], end_year)
        fig = graph5(answer, clean_world_data[clean_world_data["Entity"] == country_choosen], final_df, country_choosen,
                     end_year)
        st.plotly_chart(fig, use_container_width=True)

