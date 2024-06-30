# weather_advice.py

# Function to get clothing recommendations based on weather
def get_clothing_recommendation(weather):
    if weather == 'sunny':
        return "Wear a t-shirt and sunglasses."
    elif weather == 'rainy':
        return "Don't forget your umbrella and a raincoat."
    elif weather == 'cold':
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

# Main function to execute the script
def main():
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
    
    # Get and print the clothing recommendation
    recommendation = get_clothing_recommendation(weather)
    print(recommendation)

# Entry point of the script
if __name__ == "__main__":
    main()

