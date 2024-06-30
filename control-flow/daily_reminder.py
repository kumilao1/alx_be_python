def main():
    # Prompt the user to input a task description
    task = input("Enter your task: ").strip()

    # Prompt the user to input the task's priority
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt the user to input if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority using match-case statement
    reminder_message = f"Reminder: '{task}' is a "
    match priority:
        case 'high':
            reminder_message += "high priority task"
        case 'medium':
            reminder_message += "medium priority task"
        case 'low':
            reminder_message += "low priority task"
        case _:
            reminder_message += "task with unspecified priority"

    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder_message += " that requires immediate attention today!"
    else:
        reminder_message += ". Consider completing it when you have free time."

    # Print the customized reminder
    print(reminder_message)

if __name__ == "__main__":
    main()


