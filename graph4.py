# LIBRARIES :|
# importing the required libraries
import plotly.express as px
from data_clean import load_data, clean_csvs, one_country_name, to_anomalies, to_one_df, extract_countries, \
    heatmap_cities

# setting up and accessing the required data for this graph
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_heatmap_cities = heatmap_cities(Allcities)
cities_in_anomalies = to_anomalies(all_heatmap_cities)

# MAIN FUNCTION :)
# this is basically the main function that gives the final heatmap
def graph4(type,name_list):
    # Group the data into decades and calculate the
    # average temperature anomaly for each decade.

    if type == "City":
        csv = to_one_df(name_list,cities_in_anomalies)
        # Create a new column containing the decade
        # (e.g. 1985 → 1980, 2004 → 2000)
        csv["Decade"] = (csv["YEAR"] // 10) * 10

        # Calculate the average anomaly for each city
        # within every decade
        final_df = csv.groupby(
            ["Location", "Decade"]
        )["Temperature anomaly"].mean().reset_index()

        # Rearrange the data so that locations become rows
        # and decades become columns for the heatmap
        heatmap_df = final_df.pivot(
            index="Location",
            columns="Decade",
            values="Temperature anomaly"
        )
    else:
        csv = extract_countries(name_list,clean_world_data)
        # Repeat the same process using the country dataset
        csv["Decade"] = (csv["Year"] // 10) * 10
        final_df = csv.groupby(
            ["Entity", "Decade"]
        )["Temperature anomaly"].mean().reset_index()
        heatmap_df = final_df.pivot(
            index="Entity",
            columns="Decade",
            values="Temperature anomaly"
        )

    #  Create the heatmap using the dataframe made above
    fig = px.imshow(heatmap_df, color_continuous_scale="RdBu_r", aspect="auto", text_auto=True)

    # returning the final figure
    return fig