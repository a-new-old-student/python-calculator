def get_num(prompt):
    while True:
        try:
            print(prompt)
            user_num = int(input("--- "))
            break

        except ValueError:
            print("That's not a number.")

    return user_num

