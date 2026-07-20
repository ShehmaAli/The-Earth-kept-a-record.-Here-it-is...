# LIBRARIES :)
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# using st.cache_data to make data processing faster whenever data is needed again
@st.cache_data
# FUNCTION 1 :)
# this function is basically to load all the necessary datasets for this web application !!!
def load_data():
    # The CSV for all the selected countries in the world
    # reading the CSV and giving it a good variable name
    world_data = pd.read_csv("Weather station csv/world_data.csv")

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
    moscow = pd.read_csv("Weather station csv/moscow.csv")
    singapore = pd.read_csv("Weather station csv/singapore.csv")
    madrid = pd.read_csv("Weather station csv/madrid.csv")
    seoul = pd.read_csv("Weather station csv/seoul.csv")
    rome = pd.read_csv("Weather station csv/rome.csv")
    berlin = pd.read_csv("Weather station csv/berlin.csv")
    bangkok = pd.read_csv("Weather station csv/bangkok.csv")
    oslo = pd.read_csv("Weather station csv/oslo.csv")

    # Making a seperate dictionary for the city csv
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

    # returning the world data csv
    # and the all_cities dictionary
    return world_data, all_cities


# FUNCTION 2 :)
# this function is used to clean the CSVs
# like taking care of the empty(where nothing is entered place) and interpolate them
# so that there is no problem later when making the graph

def clean_csvs(all_cities, world_data):
    # starting a for loop to iterate over each element of the dictionary
    # which is each csv
    for i in all_cities.values():
        # This is going to replace the empty values in each csv in the dictionary
        i.replace(999.90, np.nan, inplace=True)
        # Fill missing temperature values using linear interpolation.
        i["metANN"] = i["metANN"].interpolate(method="linear")

    # this is going to fill the empty values in the world_data with "0"
    world_data["Code"] = world_data["Code"].fillna("0")

    # returning all the all_cities dictionary and the world_data csv
    return all_cities, world_data


# FUNCTION 3 :)
# this function is used to give a list of each country in the world data csv
# this function is made to help when the user selects their desired country
def one_country_name(data):
    country = ""
    # a separate list to store each country once
    countries = []

    # iterating through each element of the Entity column of the csv
    # Create a list containing each country only once.
    for single_country in data["Entity"]:

        # checking with an if statement that if the previous  country is not the same as the new country
        if single_country != country:
            # then the countries list would be appended and this would be added
            countries.append(single_country)

            # the new country will then become the old country
            country = single_country

    # returning the countries list
    return countries


# FUNCTION 4 :)
# This function is used to turn the actual data in the cities csv to  the temperature anomaly
# it's parameter is the all_cities dictionary
def to_anomalies(cities):
    # using a for loop to iterate over each csv in the dictionary
    for name, df in cities.items():

        # initialising the new column in the csv and setting it then to null
        df["Temperature anomaly"] = np.nan

        # seeing with the help of if statements to calculate temperature anomaly
        # seeing the minimum starting year
        # most of the CSVs have the minimum year of 1940
        if df["YEAR"].min() == 1940:
            # if the minimum year is 1940
            # so the baseline period would be from 1961 to 1990
            baseline_period = df[(df["YEAR"] >= 1961) & (df["YEAR"] <= 1990)]

            # then the base temperature for the temperature anomaly is going to be the average of the baseline_period
            baseline = baseline_period["metANN"].mean()

            # the temperature anomaly is going to be the actual temperature subtracted by the baseline
            df["Temperature anomaly"] = df["metANN"] - baseline

        # those who don't have the minimum starting year of 1940
        else:
            # the baseline for the CSVs that don't have the minimum year of 1940
            # would be the average of the actual temperature
            baseline = df["metANN"].mean()

            # the temperature anomaly is going to be the actual temperature subtracted by the baseline
            df["Temperature anomaly"] = df["metANN"] - baseline

    # returning the all_cities dictionary
    return cities


# FUNCTION 5 :)
# this function is to combine the seperate CSV data into a single dataframe inorder to make a graph
# this function would use the selected cities by the user to make a single dataframe
def to_one_df(selected_cites: list, cities_dataset):
    # the list for the selected city dataframes
    selected_cities_list = []

    # In this for loop it would go thought each of the city in the selected_cities
    for city in selected_cites:
        # copying a single city data from it's CSV which is in the selected_cities
        one_city_df = cities_dataset[city].copy()

        # adding the location of that city to this dataframe
        one_city_df["Location"] = city

        # appending the current city dataframe to the selected_city_list
        selected_cities_list.append(one_city_df)

    # turning the selected_cities list into a dataframe by pd.concat
    all_selected_cities_df = pd.concat(selected_cities_list, ignore_index=True)

    # returning the final dataframe of all the selected cities
    return all_selected_cities_df


# FUNCTION 6 :)
# This function is the same as the function 5 but the only difference in this function is that it is for countries
# and there is only one csv to extract the data from
# This function is basically to extract the data from the world_data CSV according to the countries the user selects
# and then returns a single dataframe
def extract_countries(selected_countries: list, countries_csv):
    # this is the list that is later going to be converted into a single dataframe
    selected_countries_list = []

    # going through each country selected by the user
    for country in selected_countries:
        # the one country data is going to be
        # where the Entity in the countries_csv is the same as one of the selected country by the users
        # the data would be extracted
        one_country_data = countries_csv[countries_csv["Entity"] == country]

        # appending the current city dataframe to the selected_country_list
        selected_countries_list.append(one_country_data)

    # turning the selected_countries_list into a dataframe by pd.concat
    all_selected_countries_df = pd.concat(selected_countries_list, ignore_index=True)

    # returning the final dataframe of all the selected countries
    return all_selected_countries_df


# FUNCTION 7 :)
def heatmap_cities(cities_dataset):
    heatmap_cities = {}

    for city, df in cities_dataset.items():
        if df["YEAR"].min() <= 1940:
            heatmap_cities[city] = df

    return heatmap_cities


# FUNCTION 8 :)
# this function is used to get ranking for each category the cities and the countries
# the ranking is decided by the increase in temperature anomaly thought out from 1940 to 2025
def get_ranks(cities_csv, country_csv, all_country_list):
    country_ranks = []
    city_ranks = []

    # FOR CITIES
    # for every city the loop will take the first temperature anomaly which is in 1940 and the last temperature anomaly which is in 2025
    for city, df in cities_csv.items():
        # the first anomaly in 1940
        first = df["Temperature anomaly"].iloc[0]
        # the last anomaly in 2025
        last = df["Temperature anomaly"].iloc[-1]

        # the total increase in temperature anomaly overall
        increase = last - first

        # then appending the city_ranks list which is later going to be turned into a dataframe
        city_ranks.append({
            "Location": city,
            "Increase": increase
        })

    # turning the list into a dataframe by the use of pd.DataFrame
    city_ranking_df = pd.DataFrame(city_ranks)

    # FOR COUNTRIES
    # going through every  country one by one
    for country in all_country_list:
        # abtaining one country's data
        country_df = country_csv[
            country_csv["Entity"] == country
            ]

        # getting the temperature anomaly in 1940
        first = country_df["Temperature anomaly"].iloc[0]

        # getting the temperature anomaly in 2025
        last = country_df["Temperature anomaly"].iloc[-1]

        # calculating the total increase in temperature anomaly
        increase = last - first

        # adding the country and it's increase of temperature anomaly in the country_ranks
        country_ranks.append({
            "Entity": country,
            "Increase": increase
        })

        # turning the list to a dataframe using the pd.DataFrame
        country_ranking_df = pd.DataFrame(country_ranks)

    # returning both of the dataframes
    return city_ranking_df, country_ranking_df


# FUNCTION 9 :)
# this function does the linear regression and it uses ploynomial features to predict the temperature anomaly in the future
def predict(type, csv, prediction_year):
    # Create polynomial features of degree 2.
    # This allows the model to basically learn curves instead of just a straight line.
    poly = PolynomialFeatures(degree=2)

    # The city CSV uses the column "YEAR" while the country CSV uses "Year".
    # Select the correct column and convert it into polynomial features.
    if type == "City":
        X = poly.fit_transform(csv[["YEAR"]])
    else:
        X = poly.fit_transform(csv[["Year"]])

    # Create the Polynomial Regression model.
    # We use LinearRegression because the polynomial transformation
    # has already converted the data into a curved form.
    model = LinearRegression()

    # Train the model using the historical temperature anomaly data.
    # X contains the years and csv["Temperature anomaly"] contains the values to learn.
    model.fit(X, csv["Temperature anomaly"])

    # Generate all future years from 2025 up to the year selected by the user.
    # reshape(-1,1) converts the list into the format expected by Scikit-Learn.
    future_year = np.arange(2025, prediction_year + 1).reshape(-1, 1)

    # Convert the future years into polynomial features
    # so they have the same format as the training data.
    future_predict = poly.transform(future_year)

    # Predict the temperature anomaly for each future year.
    prediction = model.predict(future_predict)

    # Store the predicted years and their corresponding predictions as a DataFrame predicted_df for easier plotting
    predicted_df = pd.DataFrame({
        "Year": future_year.flatten(),
        "Prediction": prediction
    })

    # returning the predicted_df
    return predicted_df
