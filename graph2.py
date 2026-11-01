# LIBRARIES :)
# importing the required libraries
import plotly.express as px

# getting the functions from the file data_clean.py
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, to_one_df, extract_countries

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
cities_in_anomalies = to_anomalies(Allcities)


# MAIN FUNCTION :)
# this is basically the main function that gives the graph

def graph2(type, name_list):
    # getting the parameters for the graph2 function and generating the figure according to it
    if type == "City":
        csv = to_one_df(name_list, cities_in_anomalies)
        years = csv["YEAR"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected cities"
        # making the graph using px.line
        fig = px.line(csv, years, temps, title=final_title, color="Location")
    if type == "Country":
        csv = extract_countries(name_list, clean_world_data)
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in the selected countries"
        # making the graph using px.line
        fig = px.line(csv, years, temps, title=final_title, color="Entity")

    # returning the figure
    return fig
