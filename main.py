"""
TODO
1: clean CSVs by cities and countries side by side
2: set up graphs designs
3: set up the web application by streamlit
4: make the future graph using regression
5: ship the project

TOTAL countries and cites = 10 countries and 10 cites
"""

import numpy as np
import pandas as pd
import streamlit as st
from graphs.graph1 import graph1

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

# making a list and the then it can be used for multiple things
All_cities = [multan, delhi, london, new_york, beijing, sydney, tokyo, paris, dubai, nuuk]

# another list from which the user can choose the graph for cities from
All_cities_str = ["multan", "delhi", "london", "new york", "beijing", "sydney", "tokyo", "paris", "dubai", "nuuk"]

for i in All_cities:
    i.replace(999.90, np.nan, inplace=True)
    i["metANN"] = i["metANN"].interpolate(method="linear")

"""
GRAPHS AND TYPES:
1: Indiviual City/country line graph seperately
2: all cities/ countries comparison seperately
3: Total warming bar chart seperately
4: Decade heatmap seperately
5: Regression future predictor
"""


# asking user for their desired city to show
while True:
    choice = input("Graph of Country or City: ")
    if choice.lower() == "city":
        user_city = input("Enter desired city: ")
        if user_city.lower() in All_cities_str:
            city_index = All_cities_str.index(user_city.lower())
            graph1(All_cities[city_index], All_cities_str[city_index])
        break
    elif choice.lower() == "country":
        user_country = input("Enter desired country or its code: ")
        if user_country in world_data["Entity"] or user_country in world_data["Code"]:
            print("YAAY")
        break
    else:
        print("wrong enter again")


# setting up web app using streamlit


















