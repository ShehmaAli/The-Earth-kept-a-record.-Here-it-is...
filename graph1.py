# LIBRARIES :)
# importing required libraries
import plotly.express as px

# getting the functions from the file data_clean.py
from data_clean import load_data, clean_csvs,to_one_df, extract_countries

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)

# MAIN FUNCTION :)
# this is basically the main function that gives the graph
def graph1(type,name_list):

    # getting the parameters for the graph according to the category
    if type == "City":
        csv = to_one_df(name_list,Allcities)
        years = csv["YEAR"]
        temps = csv["metANN"]
        final_title = f"Average annual temperature in your selected City"
    if type == "Country":
        csv = extract_countries(name_list, clean_world_data)
        years = csv["Year"]
        temps = csv["Temperature anomaly"]
        final_title = f"Temperature anomalies in your selected Country"

    # making a graph with the use of px.line
    fig = px.line(csv, x=years, y=temps, title=final_title, color_discrete_sequence=["orangered"])

    # returning the made figure
    return fig
