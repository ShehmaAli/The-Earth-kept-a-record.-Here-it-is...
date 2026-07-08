# LIBRARIES :)
import numpy as np
import pandas as pd
import streamlit as st


# using st.cache_data to make data processing faster whenever data is needed again
@st.cache_data
# FUNCTION 1
# this function is basically to load all the necessary datasets for this web application !!!
def load_data():
    # checking for any empty values in each of the CSVs
    # All the selected countries in the world
    world_data = pd.read_csv("Weather station csv/World_data.csv")

    # reading all the city CSVs and giving them each a good variable name
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

    # Putting the city CSVs which have been read and entering into a dictionary
    # for easier data handling later
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


# FUNCTION 2
# this function is used to clean the CSVs
# like taking care of the empty(where nothing is entered place) and interpolate them
# so that there is no problem later when making the graph
def clean_csvs(all_cities, world_data):
    for i in all_cities.values():
        i.replace(999.90, np.nan, inplace=True)
        i["metANN"] = i["metANN"].interpolate(method="linear")
    world_data["Code"] = world_data["Code"].fillna("0")
    return all_cities, world_data


# FUNCTION 3
# this function is used to give a list of each country in the world data csv
# this function is made to help when the user selects their desired country
def one_country_name(data):
    country = ""

    # a separate list to store each country once
    countries = []
    for single_country in data["Entity"]:
        if single_country != country:
            countries.append(single_country)
            country = single_country

    return countries


# FUNCTION 3:|
#
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


def extract_countries(selected_countries: list, countries_csv):
    selected_countries_list = []
    for country in selected_countries:
        one_country_data = countries_csv[countries_csv["Entity"] == country]
        selected_countries_list.append(one_country_data)

    all_selected_countries_df = pd.concat(selected_countries_list, ignore_index=True)

    return all_selected_countries_df


def heatmap_cities(cities_dataset):
    heatmap_cities = {}

    for city, df in cities_dataset.items():
        if df["YEAR"].min() <= 1940:
            heatmap_cities[city] = df

    return heatmap_cities

def get_ranks(cities_csv, country_csv, all_country_list):
    country_ranks = []
    city_ranks = []
    for city, df in cities_csv.items():
        first = df["Temperature anomaly"].iloc[0]
        last = df["Temperature anomaly"].iloc[-1]
        increase = last - first
        city_ranks.append({
            "Location": city,
            "Increase": increase
        })
    city_ranking_df = pd.DataFrame(city_ranks)

    for country in all_country_list:
        country_df = country_csv[
            country_csv["Entity"] == country
            ]
        first = country_df["Temperature anomaly"].iloc[0]

        last = country_df["Temperature anomaly"].iloc[-1]

        increase = last - first

        country_ranks.append({
            "Entity": country,
            "Increase": increase
        })
        country_ranking_df = pd.DataFrame(country_ranks)

    return city_ranking_df,country_ranking_df

