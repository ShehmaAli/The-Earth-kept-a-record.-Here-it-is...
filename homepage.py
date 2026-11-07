"""
GRAPHS AND TYPES:
1: Individual city/country line graph separately
2: All cities/countries comparison separately
3: Total warming bar chart separately
4: Decade heatmap separately
"""

# importing the required functions and graph modules
from ui import (
    separator,
    header,
    stat_cards,
    visualisation_menu,
    section_heading,
    user_choice,
    footer,
    about_temp_anomaly,
    location_menu,
    get_location_selection,
    user_category,
    output_sorting_choices,
    user_sort_choice
)

# importing functions from other files
from data_clean import load_data, clean_csvs, one_country_name
from graph1 import graph1
from graph2 import graph2
from graph3 import graph3
from graph4 import graph4


# loading and preparing the climate datasets
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
country_names = one_country_name(clean_world_data)

# available cities for selection
all_cities = [
    "bangkok",
    "beijing",
    "berlin",
    "cairo",
    "delhi",
    "london",
    "madrid",
    "moscow",
    "multan",
    "new york",
    "nuuk",
    "oslo",
    "paris",
    "rome",
    "seoul",
    "sydney",
    "tokyo",
]

# Main Function actually the main function that would run the whole program
def main():

    # displaying the homepage
    header()
    stat_cards(86, 4, world_data["Entity"].nunique())

    # keeping the main menu active
    while True:

        visualisation_menu()
        choice = user_choice()

        # GRAPH 1: Temperature Trends
        # this graph would show the temperature trend of the single city/country
        if choice == "1":
            section_heading("📈 Temperature Trends")
            location_menu()
            category_selection = user_category()
            separator()
            about_temp_anomaly()
            separator()

            if category_selection == "q":
                pass

            if category_selection == "1" or category_selection == "cities":
                final_list = get_location_selection(all_cities, 0)
                fig = graph1("City", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

            if category_selection == "2" or category_selection == "countries":
                final_list = get_location_selection(all_country_names, 0)
                fig = graph1("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # GRAPH 2: Climate Comparison
        # this graph would be open up in the browser
        # and this graph would compare multiple cities/countries
        elif choice == "2":
            section_heading("🌡️ Climate Comparison")
            location_menu()
            category_selection = user_category()
            separator()
            about_temp_anomaly()
            separator()

            if category_selection == "q":
                pass

            if category_selection == "1" or category_selection == "cities":
                final_list = get_location_selection(all_cities, 7)
                fig = graph2("City", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

            if category_selection == "2" or category_selection == "countries":
                final_list = get_location_selection(all_country_names, 7)
                fig = graph2("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # GRAPH 3: Hottest Places Rankings
        # this graph would open in the browser and show the user
        # either ranking by highest warming
        # either ranking by lowest warming
        elif choice == "3":
            section_heading("🌎 Hottest Places Rankings")
            location_menu()
            category_choice = input("Enter your choice: ").lower()
            separator()
            output_sorting_choices()
            temp_change = user_sort_choice()
            separator()
            about_temp_anomaly()
            separator()

            if category_choice == "1" or category_choice == "cities":
                fig = graph3("City", temp_change)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

            elif category_choice == "2" or category_choice == "countries":
                fig = graph3("Country", temp_change)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

            elif category_choice == "q" or category_choice == "quit":
                pass

        # GRAPH 4: Temperature Heatmap
        # this graph is supposed to open a heatmap in the browser
        elif choice == "4":
            section_heading("🗺️ Temperature Heatmap")
            location_menu()
            category_selection = user_category()
            separator()
            about_temp_anomaly()
            separator()

            if category_selection == "q":
                pass

            if category_selection == "1" or category_selection == "cities":
                final_list = get_location_selection(all_cities, 10)
                fig = graph4("City", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

            if category_selection == "2" or category_selection == "countries":
                final_list = get_location_selection(all_country_names, 10)
                fig = graph4("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # QUIT APPLICATION
        elif choice == "q":
            footer()
            break

        else:
            print("\nDear user kindly select within 1-4 or Q to quit the program.")


# running the application
if __name__ == "__main__":
    main()
