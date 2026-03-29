user_input = input("Enter a number: ")

digit_count = sum(char.isdigit() for char in user_input)

print("You entered", digit_count, "digit(s).")