user_set = set()  # Initialize an empty set to store the values

while True:
    user_input = input("Enter a distinct natural number (1 < n < 11), or 'done' to finish: ")

    if user_input == 'done':
        break  # Exit the loop if the user enters 'done'

    try:
        num = int(user_input)
        if 1 < num < 11 and num not in user_set:
            user_set.add(num)  # Add the valid input to the set
        else:
            print("Invalid input. Please enter a distinct natural number within the specified range.")
    except ValueError:
        print("Invalid input. Please enter a distinct natural number within the specified range.")

print("Set of distinct natural numbers:",user_set)
print("soumya")
