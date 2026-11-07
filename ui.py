# LIBRARIES :)
# importing the needed library functions and
import random
from data_clean import load_data, clean_csvs, one_country_name


# Loading and preparing the climate data
world_data, all_cities = load_data()
Allcities, clean_world_data = clean_csvs(all_cities, world_data)
all_country_names = one_country_name(clean_world_data)

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

# FUNCTION 1
# Displays a horizontal separator
# I really like to actually separate the actual text and put it into a  variable to make the code more readable
def separator():
    separator_line = "-" * WIDTH
    print(separator_line)


# FUNCTION 2
# Displays the application title and introduction
# I really like to actually separate the actual text and put it into a  variable to make the code more readable
def header():
    separator()
    heading_title = "THE EARTH KEPT A RECORD".center(WIDTH)
    print(heading_title)
    sub_heading = "Explore historical climate changes and future predictions".center(WIDTH)
    print(sub_heading)
    separator()


# FUNCTION 3
# Displays the project's main statistics
def stat_cards(years, visualisations, countries):
    print()
    separator()

    card_width = WIDTH // 3 # so the cards are of equal length on the screen

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


# FUNCTION 4
# Displays the available graphs
def visualisation_menu():
    print()
    print("AVAILABLE VISUALISATIONS".center(WIDTH))
    separator()

    print("OPTION          VISUALISATION")
    separator()

    print("1               📈 Temperature Trends")
    print("2               🌡️ Climate Comparison")
    print("3               🌎 Hottest Places Rankings")
    print("4               🗺️ Temperature Heatmap")
    print("Q               Quit")

    separator()


# FUNCTION 5
# returns the user's choice
def user_choice():
    return input("\nEnter your choice: ").strip().lower()


# FUNCTION 6
# Displays a heading for each section what ever section I am going to start and takes it's title as input
def section_heading(title):
    print()
    separator()
    print(title.upper().center(WIDTH))
    separator()


# FUNCTION 7
# Displays the exit message
# I really like to actually separate the actual text and put it into a  variable to make the code more readable
def footer():
    print()
    separator()
    bye_message = "Thank you for exploring The Earth Kept a Record! Byeeeee!!!!!".center(WIDTH)
    print(bye_message)
    exit_message = "Exiting application...".center(WIDTH)
    print(exit_message)
    separator()


# FUNCTION 8
# Briefly explains temperature anomalies
def about_temp_anomaly():
    print("What is temperature anomaly??")
    print(
        "A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature."
    )
    print("🟥 Positive (+) = Warmer than average")
    print("🟦 Negative (−) = Cooler than average")


# FUNCTION 9
# Displays the city/country selection menu
def location_menu():
    print()
    separator()
    print("CHOOSE LOCATION TYPE".center(WIDTH))
    separator()

    print("1. Cities")
    print("2. Countries")
    print("Q. Back to main menu")

    separator()


# FUNCTION 10
# Displays locations in multiple columns
def names_of_selected_choice(locations, title, columns=3):

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


# FUNCTION 11
# Gets the user's choice between cities and countries
def user_category():
    category_choice = input("Enter your choice: ").lower()
    separator()

    if category_choice == "1" or category_choice == "cities":
        names_of_selected_choice(all_cities, "Cities to choose from: ")
        return category_choice

    elif category_choice == "2" or category_choice == "countries":
        names_of_selected_choice(all_country_names, "Countries to choose from:")
        return category_choice

    elif category_choice == "q" or category_choice == "quit":
        return category_choice


# FUNCTION 12
# Allows users to select locations by their own choice or to get surprised by choosing random one
def get_location_selection(locations, limit):
    # the final locations would be returned as a list
    final_location = []

    # if the limit is 0 so only one country/city would be added into the list and the list would be returned then
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

    # if the limit is greater 0 so only the amount of the locations would be as same as the limit
    # and that number of country/city would be added into the list and the list would be returned then
    if limit > 0:
        counter = 1
        print("🎲 Go for RANDOM MAGIC!!!!")
        random_needed = input("🎲 Want to get surprised???\n Y for yes \n N for no\n Enter: ").lower()

        if random_needed == "y":
            final_location = random.sample(locations, limit)

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


# FUNCTION 13
# Displays the available sorting options
def output_sorting_choices():
    print("\nSORTING OPTIONS")
    sort_seperator = "-" * 30
    print(sort_seperator)
    print("1. Highest Warming")
    print("2. Lowest Warming")
    print(sort_seperator)


# FUNCTION 14
# Gets and validates the user's sorting choice
def user_sort_choice():
    while True:
        choice = input("Choose a sorting option: ").strip().lower()

        if choice == "1" or choice == "highest warming":
            return "Highest warming"

        elif choice == "2" or choice == "lowest warming":
            return "Lowest warming"

        else:
            print("Dear user invalid choice. Please choose 1 or 2.")