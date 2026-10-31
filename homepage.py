"""
GRAPHS AND TYPES:
1: Indiviual City/country line graph seperately
2: all cities/ countries comparison seperately
3: Total warming bar chart seperately
4: Decade heatmap seperately
5: Regression future predictor
"""


def menu():
    print("\n" + "=" * 42)
    print("The EARTH KEPT A RECORD")

    # to make the commandline more readable
    print("=" * 42)
    print("Explore the historic climate data \n DATA is obtained from the NASA spacecenter \n")

    print("1. Temperature Trends")
    print("2. Climate Comparison (between many different countries or cities)")
    print("3. Hottest Places(countries or cities seperately) Rankings")
    print("4. Temperature Heatmap")
    print("5. Future Temperature Prediction")
    print("6. Exit")


def main():
    while True:
        menu()
        user_choice = input("Kindly choose an option between 1-6 inclusive ")


        if user_choice == "1":
            print("Temperature Trends")
        elif user_choice == "2":
            print("Climate Comparison (between many different countries or cities)")
        elif user_choice == "3":
            print("Hottest Places(countries or cities seperately) Rankings")
            break
        elif user_choice == "4":
            print("Temperature Heatmap")
            break
        elif user_choice == "5":
            print("Future Temperature Prediction")
            break
        elif user_choice == "6":
            print("Thank you for getting to known our planet more better 🎉")
            break
        else:
            print("Kindly choose the correct choice.")
            print("Remember to eneter a number between 1-6 inclusive")

if __name__ == "__main__":
    main()


"""
    
from rich.console import Console
from rich.markdown import Markdown

console = Console()
    TEMP ANOMALLY

console.print(Markdown("### What is temperature anomaly??"))
console.print(Markdown(
        "<p style='color:#9afcd7;'>A temperature anomaly shows how much warmer or cooler a place is compared to its usual long-term average temperature.</p>",
        unsafe_allow_html=True, text_alignment="center"
        ))
console.print(Markdown("🟥 Positive (+) = Warmer than average"))
console.print(Markdown("🟦 Negative (−) = Cooler than average"))
    """
