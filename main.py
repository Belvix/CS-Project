#CS Project XII-A
#Memebers- Gokul, Srichaitanya, Adarsh
#Project topic - Food ordering app

import json

restart = False
cart = []

def customer():
    global restaurants
    global restart
    global cart
    menu_reshow = True
    print("Welcome customer. Please take a look at the list of restaurants to choose from:-")
    restaurant_list = [line.rstrip('\n') for line in restaurants]
    restaurant_dict_list = [json.loads(restaurant) for restaurant in restaurant_list]
    while not restart:
        menu_reshow = True
        print("Choose a restaurant number to show menu, type logout to exit, cart to show cart")
        for restaurant in restaurant_dict_list:
            print(restaurant['index']+':-'+restaurant['name'])
        command = input()

        #elif command in [rest['index'] for rest in restaurant_dict_list]:
        for restaurant in restaurant_dict_list:
            if command == restaurant['index']:
                with open(restaurant['menu'],'r') as menu:
                    menu_string=menu.readline()
                    menu_dict = json.loads(menu_string)
                    while menu_reshow:
                        print("Enter a food item to add")
                        for items in menu_dict:
                            print(items['index']+':- '+items['item'])
                        menu_choice = input()
                        if menu_choice == 'back':
                            menu_reshow = False
        if command == 'logout':
            restart = True
                       
        elif command == 'back':
            customer()
        elif command == 'cart':
            print(cart)
    
while True:
    print(restart)
    restaurantlist = open("Restaurants/Restaurants.txt", 'r+')
    restaurants = restaurantlist.readlines()
    #customer = False
    #manager = False
    start=input("Type C to order food, type M is you're a manager, exit to close")
    if restart == True:
        restart = False
        
    if start=='c' or start=='C' or start=='customer' or start=='Customer':
        #customer = True
        #manager = False
        customer()
        
    elif start=='m' or start=='M' or start=='manager' or start=='Manager':
        print("Welcome Manager")
        #manager = True
        #customer = False

    elif start=='exit':
        print("exiting")
        restaurantlist.close()
        break
    

        
