import numpy as np
import pandas as pd


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
All_cities = {"multan": multan,
              "delhi": delhi,
              "london": london,
              "new york": new_york,
              "beijing": beijing,
              "sydney":  sydney,
              "tokyo": tokyo,
              "paris": paris,
              "dubai": dubai,
              "nuuk": nuuk}

for i in All_cities.values():
    i.replace(999.90, np.nan, inplace=True)
    i["metANN"] = i["metANN"].interpolate(method="linear")