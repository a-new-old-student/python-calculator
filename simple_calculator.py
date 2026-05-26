print("Welcome to the calculator!" \
"\n If you want to get started, type 'go' below." \
"\n If you want to exit, type 'exit' below.")

while True:
        print("|menu|")
        user_input_menu = input("--- ")
    
        if user_input_menu == "go":
                print("Great! \n Let's get started. " \
                "\n Below, I'll ask you to write down the numbers you want to perform the operation on, "
                "as well as the operations themselves.")
        
                while True:
                        while True:
                                try:        
                                        print("Enter the first number.")
                                        first_num = int(input("--- "))
                                        break                        
                                except ValueError:
                                        print("This is not a number! Please use digits.")
                        while True:
                                try:
                                        print("Enter the second number.")
                                        second_num = int(input("--- "))
                                        break
                                except ValueError:
                                        print("This is not a number! Please use digits.")


                        print("Enter an action.")
                        action = input("--- ")

                        
                        while action not in ("divide", "/", "plus", "+", "subtract", "-", "multiply", "*", "degree", "**"):
                                print("Please enter the correct action.")
                                action = input("--- ")


                        
                                
                        while second_num == 0 and action in ("/", "divide"):
                                while True:
                                        try:
                                                print("You cannot divide be zero." \
                                                "\nEnter the second number.")
                                                second_num = int(input("--- "))
                                                break
                                        except ValueError:
                                                print("This is not a number! Please use digits.")
                                
                               


                        if action == "divide" or action == "/":
                                print(f"Answer: {first_num / second_num}")
                
                        elif action == "plus" or action == "+":
                                print(f"Answer: {first_num + second_num}")
                
                        elif action == "subtract" or action == "-":
                                print(f"Answer: {first_num - second_num}")
                
                        elif action == "multiply" or action == "*":
                                print(f"Answer: {first_num * second_num}")
                        elif action == "degree" or action == "**":
                                print(f"Answer: {first_num ** second_num}")

                        print("Shall we carry on?")
                        user_input_calcul = input("--- ")
            
                        while user_input_calcul not in ("yes", "no"):
                                print("I don't understand." \
                                "\nShall we carry on?")
                                user_input_calcul = input("--- ")
            
                        if user_input_calcul == "yes":
                                continue
                        elif user_input_calcul == "no":
                                break

        elif user_input_menu == "exit":
                break
        else:
                print("I don't understand.")