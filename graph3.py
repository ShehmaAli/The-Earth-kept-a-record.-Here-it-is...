# LIBRARIES :)
# importing important libraries needed
import plotly.express as px

# getting the functions from the file data_clean.py
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, \
    heatmap_cities, get_ranks

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_heatmap_cities = heatmap_cities(Allcities)
cities_in_anomalies = to_anomalies(all_heatmap_cities)

# creating the ranking dataframes
city_ranks_df, country_ranks_df = get_ranks(
    cities_in_anomalies,
    clean_world_data,
    one_country_name(clean_world_data)
)


# FUNCTION :)
# creates the warming ranking graph
def graph3(type, order):

    # Select the correct ranking dataframe
    if type == "City":
        csv = city_ranks_df.copy()

    elif type == "Country":
        csv = country_ranks_df.copy()

    else:
        raise ValueError("Invalid location type")

    # Sort according to the selected warming order
    if order == "Highest warming":
        csv = csv.sort_values(
            by="Increase",
            ascending=False
        )

    elif order == "Lowest warming":
        csv = csv.sort_values(
            by="Increase",
            ascending=True
        )

    else:
        raise ValueError("Invalid sorting option")

    # Keep only the top 15 results
    csv = csv.iloc[:15]

    # Set the graph title and location column
    if type == "City":
        title = f"Top 15 cities with the {order}"
        y_column = "Location"

    else:
        title = f"Top 15 countries with the {order}"
        y_column = "Entity"

    # Create the horizontal bar graph
    fig = px.bar(
        csv,
        x="Increase",
        y=y_column,
        orientation="h",
        title=title,
        color="Increase",
        color_continuous_scale="RdYlBu_r"
    )

    fig.update_layout(coloraxis_showscale=False)

    return fig