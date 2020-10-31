import json

entered=False
def manage(rest):
    restaurant_list = [line.rstrip('\n') for line in rest]
    restaurant_dict_list = [json.loads(restaurant) for restaurant in restaurant_list]
    restaurant_usernames = [i["username"] for i in restaurant_dict_list]
    while not entered:
        choice = input("Do you want to login, create or delete account?")
        if choice == "create" or choice=="Create":
            print("Please enter the correct answer to create a new restaurant")
        if choice=="login" or choice == "Login":
            while True:
                A = input("Enter Username:")
                if A in restaurant_usernames:
                    password = input("Enter Password")
                    for i in restaurant_dict_list:
                        if i["username"]==A:
                            if i["password"]==password:
                                print("Welcome")
                            else:
                                print("Incorrect Username or Password. Try again1")
                else:
                    print("Incorrect Username or Password. Try again2")
