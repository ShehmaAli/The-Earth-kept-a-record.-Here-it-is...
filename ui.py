# LIBRARIES :)
# Importing
import random
from data_clean import load_data, clean_csvs, one_country_name


# Loading and preparing the climate data
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
country_names = one_country_name(clean_world_data)

# Cities available for selection
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
    "tokyo"
]

WIDTH = 100


# Displays a horizontal separator
def separator():
    print("-" * WIDTH)


# Displays the application title and introduction
def show_header():
    separator()
    print("THE EARTH KEPT A RECORD".center(WIDTH))
    print("Explore historical climate changes and future predictions".center(WIDTH))
    separator()


# Displays the project's main statistics
def show_data_cards(years, visualisations, countries):
    print()
    separator()

    card_width = WIDTH // 3

    print(
        f"{'YEARS OF DATA'.center(card_width)}"
        f"{'VISUALISATIONS'.center(card_width)}"
        f"{'COUNTRIES'.center(card_width)}"
    )

    print(
        f"{str(years).center(card_width)}"
        f"{str(visualisations).center(card_width)}"
        f"{str(countries).center(card_width)}"
    )

    separator()


# Displays the available graphs
def show_visualisation_menu():
    print()
    print("AVAILABLE VISUALISATIONS".center(WIDTH))
    separator()

    print(f"{'OPTION':<15}{'VISUALISATION'}")
    separator()

    print(f"{'1':<15}📈 Temperature Trends")
    print(f"{'2':<15}🌡️ Climate Comparison")
    print(f"{'3':<15}🌎 Hottest Places Rankings")
    print(f"{'4':<15}🗺️ Temperature Heatmap")
    print(f"{'Q':<15}Quit")

    separator()


# Gets the user's menu choice
def get_choice():
    return input("\nEnter your choice: ").strip().lower()


# Displays a heading for each section
def show_section(title):
    print()
    separator()
    print(title.upper().center(WIDTH))
    separator()


# Displays the exit message
def show_footer():
    print()
    separator()
    print("Thank you for exploring The Earth Kept a Record! Byeeeee!!!!!".center(WIDTH))
    print("Exiting application...".center(WIDTH))
    separator()


# Briefly explains temperature anomalies
def temp_anomaly_table():
    print("What is temperature anomaly??")
    print(
        "A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature."
    )
    print("🟥 Positive (+) = Warmer than average")
    print("🟦 Negative (−) = Cooler than average")


# Displays the city/country selection menu
def show_location_type_menu():
    print()
    separator()
    print("CHOOSE LOCATION TYPE".center(WIDTH))
    separator()

    print("1. Cities")
    print("2. Countries")
    print("Q. Back to main menu")

    separator()


# Displays locations in multiple columns
def show_location_table(locations, title, columns=3):

    print()
    separator()
    print(title.upper().center(WIDTH))
    separator()

    # Calculate the width available for each column
    column_width = WIDTH // columns

    # Calculate the number of rows required
    total_rows = (len(locations) + columns - 1) // columns

    for row in range(total_rows):

        line = ""

        for column in range(columns):

            index = row * columns + column

            if index < len(locations):
                location = locations[index]
                cell = f"{index + 1}. {location}"
            else:
                cell = ""

            line += cell.ljust(column_width)

        print(line)

    separator()

    separator()


# Gets the user's choice between cities and countries
def category():
    category_choice = input("Enter your choice: ").lower()
    separator()

    if category_choice == "1" or category_choice == "cities":
        show_location_table(all_cities, "Cities to choose from: ")
        return category_choice

    elif category_choice == "2" or category_choice == "countries":
        show_location_table(country_names, "Countries to choose from:")
        return category_choice

    elif category_choice == "q" or category_choice == "quit":
        return category_choice


# Allows users to select locations manually or randomly
def get_location_selection(locations, limit):
    final_location = []

    if limit == 0:
        while True:
            choice = input("\nEnter the location of your choice: ").strip()

            if choice.isdigit() and 1 <= int(choice) <= len(locations):
                choice = locations[int(choice) - 1]
            else:
                choice = next(
                    (location for location in locations
                     if location.lower() == choice.lower()), None
                )

            if choice is None:
                print("Invalid selection. Please enter a valid name or number.")
            else:
                final_location.append(choice)
                break

    if limit > 0:
        counter = 1
        print("🎲 Go for RANDOM MAGIC!!!!")
        random_needed = input("🎲 Want to get surprised???\n Y for yes \n N for no\n Enter: ").lower()

        if random_needed == "y":
            final_location = random.sample(locations, limit)
            # remember to change it into dataframe later

        if random_needed == "n":
            while True:
                print("Enter E to stop: and kindly write the correct spellings")
                choice = input("\nEnter the location of your choice:").strip()

                if choice.lower() == "e" or counter > limit:
                    print("Thank you that would be all")
                    print("Graph would be given shortly")
                    separator()
                    break

                if choice.isdigit() and 1 <= int(choice) <= len(locations):
                    choice = locations[int(choice) - 1]
                else:
                    choice = next(
                        (location for location in locations
                         if location.lower() == choice.lower()), None
                    )

                if choice is None:
                    print("Invalid selection. Please enter a valid name or number.")
                    continue

                if choice in final_location:
                    print("Oops already in this selected!")
                else:
                    counter += 1
                    final_location.append(choice)

    return final_location


# Displays the available sorting options
def show_sorting_choices():
    print("\nSORTING OPTIONS")
    print("------------------------------")
    print("1. Highest Warming")
    print("2. Lowest Warming")
    print("------------------------------")


# Gets and validates the user's sorting choice
def get_sorting_choice():
    while True:
        choice = input("Choose a sorting option: ").strip().lower()

        if choice in ["1", "highest warming"]:
            return "Highest warming"

        elif choice in ["2", "lowest warming"]:
            return "Lowest warming"

        else:
            print("Invalid choice. Please choose 1 or 2.")