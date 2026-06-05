from tools import get_num
from tools import get_action
from instruction import user_instruction


print(
    "Welcome to the calculator!"
    "\n\nThere are four options available in the menu:"
    "\nTo start using the calculator, type 'go'."
    "\nTo view calculation history, type 'history'."
    "\nTo view detailed instructions, type 'instruction'."
    "\nTo exit the program, type 'exit'."
)
      
calculator_history = []

while True:
        print("|menu|")
        user_input_menu = input("--- ").strip().lower()

        if user_input_menu == "history":
                print("\n--- Calculator History ---")
                for record in calculator_history:
                        print(record)
                print("--------------------------\n")
                
        elif user_input_menu == "instruction":
                print(user_instruction)
    
        elif user_input_menu == "go":
                while True:
                        print("Great! \n Let's get started. " \
                        "\n Below, I'll ask you to write down the numbers you want to perform the operation on, "
                        "as well as the operations themselves.")
                
                        first_num = get_num("Enter the first number.")
                        user_action = get_action()

                        if user_action in ("factorial", "!"):
                                number = 1
                                for i in range(1, first_num + 1):
                                        number *= i
                                answer_history = (f"{first_num}! = {number}")
                                print(answer_history)
                                calculator_history.append(answer_history)
                        else:
                        
                                second_num = get_num("Enter the second number.")                        
                                                
                                while second_num == 0 and user_action in ("/", "divide"):                                                                        
                                        print("You cannot divide by zero.")
                                        second_num = get_num("Enter the second number.")
                                        
                                                
                                                
                                if user_action in ("divide", "/"):
                                        answer = first_num / second_num
                                        answer_history = (f"{first_num} / {second_num} = {answer}")
                                        print(answer_history)
                                        calculator_history.append(answer_history)
                                
                                elif user_action in ("plus", "+"):
                                        answer = first_num + second_num
                                        answer_history = (f"{first_num} + {second_num} = {answer}")
                                        print(answer_history)
                                        calculator_history.append(answer_history)

                                
                                elif user_action in ("subtract", "-"):
                                        answer = first_num - second_num
                                        answer_history = (f"{first_num} - {second_num} = {answer}")
                                        print(answer_history)
                                        calculator_history.append(answer_history)
                                
                                elif user_action in ("multiply", "*"):
                                        answer = first_num * second_num
                                        answer_history = (f"{first_num} * {second_num} = {answer}")
                                        print(answer_history)
                                        calculator_history.append(answer_history)

                                elif user_action in ("degree", "**", "^"):
                                        answer = first_num ** second_num
                                        answer_history = (f"{first_num}^{second_num} = {answer}")
                                        print(answer_history)
                                        calculator_history.append(answer_history)


                        print("Shall we carry on?")
                        user_input_calcul = input("--- ").strip().lower()
                        
                        while user_input_calcul not in ("yes", "no"):
                                print("I don't understand." \
                                "\nShall we carry on?")
                                user_input_calcul = input("--- ").strip().lower()
                        
                        if user_input_calcul == "yes":
                                        continue
                        elif user_input_calcul == "no":
                                        break

        elif user_input_menu == "exit":
                break
        else:
                print("I don't understand.")