from datetime import datetime, timedelta

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.now()
    # Format and print the current date and time in a readable format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days_to_add):
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in a readable format
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(days_to_add)

