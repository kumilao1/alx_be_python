def main():
    # Prompt the user to input a task description
    task = input("Enter the task description: ")

    # Prompt the user to input the task's priority
    priority = input("Enter the task's priority (high, medium, low): ")

    # Prompt the user to input if the task is time-bound
    time_bound = input("Is the task time-bound? (yes or no): ")

    # Create a base reminder message
    reminder_message = f"Reminder: {task} - Priority: {priority.capitalize()}"

    # Process the task based on priority using match-case statement
    match priority:
        case 'high':
            reminder_message += ". This is a high priority task."
        case 'medium':
            reminder_message += ". This is a medium priority task."
        case 'low':
            reminder_message += ". This is a low priority task."
        case _:
            reminder_message += ". This is an unspecified priority task."

    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder_message += " It requires immediate attention today!"

    # Print the customized reminder
    print(reminder_message)

if __name__ == "__main__":
    main()

