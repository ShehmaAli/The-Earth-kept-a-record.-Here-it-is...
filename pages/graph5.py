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


st.title("Welcome to Graph 5 :party:")

st.markdown("## Choose the following")

choices = ["Select one of the following", "City", "Country"]

answer = st.radio("Choose: ", choices)

end_year = st.slider("Till when do you want the prediction", 2026, 2150)

def graph5(type, csv, name, prediction_year):
    years = csv["Year"]
    predicted_values = csv["Prediction"]
    if type == "City":
        title = f"Predicted temperature anomalies in {name} till {prediction_year}"
    else:
        title = f"Predicted temperature anomalies in {name} till {prediction_year}"
    fig = px.line(csv, x=years, y=predicted_values, title=title)

    return fig

if answer == "City":
    city_choosen = st.selectbox("City", ["Select any option"] + list(Allcities.keys()))
    final_df = predict(answer, cities_in_anomalies[city_choosen],end_year)
    fig = graph5(answer, final_df, city_choosen,end_year)
    fig.update_layout(
        margin=dict(l=50, r=20, t=40, b=40),
        autosize=True
    )
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)

if answer == "Country":
    country_choosen = st.selectbox("Country", ["Select any option"] + one_country_name(clean_world_data))
    final_df = predict(answer, clean_world_data[clean_world_data["Entity"] == country_choosen], end_year)
    fig = graph5(answer, final_df, country_choosen, end_year)
    fig.update_layout(
        margin=dict(l=50, r=20, t=40, b=40),
        autosize=True
    )
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)
