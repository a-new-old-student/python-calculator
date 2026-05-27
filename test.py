def math():
    user_input = int(input("--- "))
    while True:
        if user_input == 1:
            break
        else:
            print("Лох")
            user_input = int(input("--- "))
    return user_input

user = math()