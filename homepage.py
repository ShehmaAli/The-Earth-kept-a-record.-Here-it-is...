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
    show_header,
    show_data_cards,
    show_visualisation_menu,
    show_section,
    get_choice,
    show_footer,
    temp_anomaly_table,
    show_location_type_menu,
    get_location_selection,
    category,
    show_sorting_choices,
    get_sorting_choice
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


# PROJECT INFORMATION
years = 86
visualisations = 4
countries = world_data["Entity"].nunique()



# MAIN APPLICATION
def main():

    # displaying the homepage
    show_header()
    show_data_cards(years, visualisations, countries)

    # keeping the main menu active
    while True:

        show_visualisation_menu()
        choice = get_choice()

        # GRAPH 1: Temperature Trends
        if choice == "1":
            show_section("📈 Temperature Trends")
            show_location_type_menu()
            category_selection = category()
            separator()
            temp_anomaly_table()
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
                final_list = get_location_selection(country_names, 0)
                fig = graph1("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # GRAPH 2: Climate Comparison
        elif choice == "2":
            show_section("🌡️ Climate Comparison")
            show_location_type_menu()
            category_selection = category()
            separator()
            temp_anomaly_table()
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
                final_list = get_location_selection(country_names, 7)
                fig = graph2("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # GRAPH 3: Hottest Places Rankings
        elif choice == "3":
            show_section("🌎 Hottest Places Rankings")
            show_location_type_menu()
            category_choice = input("Enter your choice: ").lower()
            separator()
            show_sorting_choices()
            temp_change = get_sorting_choice()
            separator()
            temp_anomaly_table()
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
        elif choice == "4":
            show_section("🗺️ Temperature Heatmap")
            show_location_type_menu()
            category_selection = category()
            separator()
            temp_anomaly_table()
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
                final_list = get_location_selection(country_names, 10)
                fig = graph4("Country", final_list)
                fig.show()
                print("Kindly do come again to explore other visualisations")
                break

        # QUIT APPLICATION
        elif choice == "q":
            show_footer()
            break

        else:
            print("\nInvalid choice. Please select 1-4 or Q.")


# running the application
if __name__ == "__main__":
    main()
