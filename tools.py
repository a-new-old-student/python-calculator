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
    action = input("--- ").strip().lower()

    while action not in ("divide", "/", "plus", "+", "subtract", "-", "multiply", "*", "degree", "**", 
                         "factorial", "!"):
        print("Please enter the correct action.")
        action = input("--- ").strip().lower()
        
    return action

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b
     

