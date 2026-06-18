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
import plotly.express as px
import plotly.graph_objects as go

# checking for any empty values in each of the CSVs
# All the selected countries in the world
world_data = pd.read_csv("Weather station csv/world_data.csv")

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

"""
GRAPHS AND TYPES:
1: Indiviual City/ country line graph
2: all cities/ countries comparison
3: Total warming bar chart
4: Decade heatmap 
5: Regression future predictor
"""


# graph 1
def graph1city(city_csv, city_name):
    fig = px.line(
        city_csv,
        x = "YEAR",
        y = "metANN",
        title = f"Temperature in {city_name} from 1940s to 2026"
    )
    fig.update_traces(connectgaps = True)
    fig.show()

def graph2city(city_csv, city_name):
    pass



# asking user for their desired city to show
while True:
    user_city = input("Enter desired city: ")
    if user_city.lower() in All_cities_str:
        city_index = All_cities_str.index(user_city.lower())
        graph1city(All_cities[city_index], All_cities_str[city_index])
        break


