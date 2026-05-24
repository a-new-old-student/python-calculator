print("Welcome to the calculator!")

print(" If you want to get started, type 'go' below/ " \
"\n If you want to exit, type 'exit' below.")

while True:
    user_input_menu = input("--- ")
    if user_input_menu == "go":
            
                print("Great! \n Let's get started. " \
                "\n Below, I'll ask you to write down the numbers you want to perform the operation on, "
                "as well as the operations themselves.")
                
                print("Enter the first number.")
                first_num = int(input("--- "))

                print("Enter the second number.")
                second_num = int(input("--- "))

                print("Enter an action.")
            
                action = input("--- ")

                if action == "plus" or action == "+":
                    total = first_num + second_num
                    print(total)
                    
                elif action == "subtract" or action == "-":
                        total = first_num - second_num
                        print(total)
                            
                elif action == "divide" or action == "/":
                        total = first_num / second_num
                        print(total)
                                    
                elif action == "multiply" or action == "*":
                            total = first_num * second_num
                            print(total)
                            
                        
                else:
                        print("I don't understand.")
                        
                print("Shall we carry on?")


                
                user_input_calcul = input("--- ")
                if user_input_calcul == "yes":
                        print("Greate!")
            
                elif user_input_calcul == "no":
                                exit()
                    
                            


    elif user_input_menu == "exit":
        exit()
    else:
        print("I don't understand.")