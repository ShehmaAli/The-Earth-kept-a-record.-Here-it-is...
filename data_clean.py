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

    # another list from which the user can choose the graph for cities from
    all_cities = {"Multan": multan,
                  "Delhi": delhi,
                  "London": london,
                  "New york": new_york,
                  "Beijing": beijing,
                  "Sydney": sydney,
                  "Tokyo": tokyo,
                  "Paris": paris,
                  "Dubai": dubai,
                  "Nuuk": nuuk}

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
