def get_num(prompt):
    while True:
        try:
            print(prompt)
            user_num = int(input("--- "))
            break

        except ValueError:
            print("That's not a number.")

    return user_num

def get_action():
    print("Enter an action.")
    action = input("--- ")

    while action not in ("divide", "/", "plus", "+", "subtract", "-", "multiply", "*", "degree", "**"):
        print("Please enter the correct action.")
        action = input("--- ")
        
    return action

