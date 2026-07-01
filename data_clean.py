import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    # checking for any empty values in each of the CSVs
    # All the selected countries in the world
    world_data = pd.read_csv("Weather station csv/World_data.csv")

    # CSVs of the selected cities
    multan = pd.read_csv("Weather station csv/multan.csv")
    delhi = pd.read_csv("Weather station csv/delhi.csv")
    london = pd.read_csv("Weather station csv/london.csv")
    new_york = pd.read_csv("Weather station csv/new york.csv")
    beijing = pd.read_csv("Weather station csv/beijing.csv")
    sydney = pd.read_csv("Weather station csv/sydney.csv")
    tokyo = pd.read_csv("Weather station csv/tokyo.csv")
    paris = pd.read_csv("Weather station csv/paris.csv")
    dubai = pd.read_csv("Weather station csv/dubai.csv")
    nuuk = pd.read_csv("Weather station csv/nuuk.csv")
    cairo = pd.read_csv("Weather station csv/cairo.csv")
    toronto = pd.read_csv("Weather station csv/toronto.csv")
    moscow = pd.read_csv("Weather station csv/singapore.csv")
    singapore = pd.read_csv("Weather station csv/singapore.csv")
    madrid = pd.read_csv("Weather station csv/madrid.csv")
    seoul = pd.read_csv("Weather station csv/seoul.csv")
    rome = pd.read_csv("Weather station csv/rome.csv")
    berlin = pd.read_csv("Weather station csv/berlin.csv")
    bangkok = pd.read_csv("Weather station csv/bangkok.csv")
    oslo = pd.read_csv("Weather station csv/oslo.csv")

    # another list from which the user can choose the graph for cities from
    all_cities = {
        "Bangkok": bangkok,
        "Beijing": beijing,
        "Berlin": berlin,
        "Cairo": cairo,
        "Delhi": delhi,
        "Dubai": dubai,
        "London": london,
        "Madrid": madrid,
        "Moscow": moscow,
        "Multan": multan,
        "New York": new_york,
        "Nuuk": nuuk,
        "Oslo": oslo,
        "Paris": paris,
        "Rome": rome,
        "Seoul": seoul,
        "Singapore": singapore,
        "Sydney": sydney,
        "Tokyo": tokyo,
        "Toronto": toronto,
    }

    return world_data, all_cities


def clean_csvs(all_cities, world_data):
    for i in all_cities.values():
        i.replace(999.90, np.nan, inplace=True)
        i["metANN"] = i["metANN"].interpolate(method="linear")
    world_data["Code"] = world_data["Code"].fillna("0")
    return all_cities, world_data


def one_country_name(data):
    country = ""
    countries = []
    for single_country in data["Entity"]:
        if single_country != country:
            countries.append(single_country)
            country = single_country

    return countries


def to_anomalies(cities):
    for name, df in cities.items():
        df["Temperature anomaly"] = np.nan
        if df["YEAR"].min() == 1940:
            baseline_period = df[(df["YEAR"] >= 1961) & (df["YEAR"] <= 1990)]
            baseline = baseline_period["metANN"].mean()
            df["Temperature anomaly"] = df["metANN"] - baseline
        else:
            baseline = df["metANN"].mean()
            df["Temperature anomaly"] = df["metANN"] - baseline

    return cities


def to_one_df(selected_cites: list, cities_dataset):
    selected_cities_list = []
    for city in selected_cites:
        one_city_df = cities_dataset[city].copy()
        one_city_df["Location"] = city
        selected_cities_list.append(one_city_df)

    all_selected_cities_df = pd.concat(selected_cities_list, ignore_index=True)

    return all_selected_cities_df

def extract_countries(selected_countries : list, countries_csv):
    selected_countries_list = []
    for country in selected_countries:
        one_country_data = countries_csv[countries_csv["Entity"] == country]
        selected_countries_list.append(one_country_data)

    all_selected_countries_df = pd.concat(selected_countries_list, ignore_index= True)

    return all_selected_countries_df