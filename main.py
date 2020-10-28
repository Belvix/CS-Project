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
    print("----==Restaurant Select Menu==----")
    restaurant_list = [line.rstrip('\n') for line in restaurants]
    restaurant_dict_list = [json.loads(restaurant) for restaurant in restaurant_list]
    while not restart:
        menu_reshow = True
        print("Choose a restaurant number to show menu, type logout to exit, cart to show cart:- ")
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
                        print("Enter a food item to add:- ")
                        for items in menu_dict:
                            print(items['index']+':- '+items['item'])
                        menu_choice = input()
                        for items in menu_dict:
                            if menu_choice==items['index']:
                                cart.append(items['item'])
                        if menu_choice == 'back':
                            menu_reshow = False
                        elif menu_choice == 'cart':
                            c=1
                            if len(cart)!=0:
                                print("Your cart contains:")
                                for i in cart:
                                    print(str(c)+':'+i)
                                    c+=1
                                cont = input("Continue?\ny to add more, n to select another restaurant\n")
                                if cont == 'y':
                                    continue
                                if cont == 'n':
                                    break
                            else:
                                print("Empty Cart")
                        else:
                            print("Select a different index")
                       
            elif command == 'logout':
                restart = True
            elif command == 'cart':
                c=1
                if len(cart)!=0:
                    print("Your cart contains:")
                    for i in cart:
                        print(str(c)+':'+i)
                        c+=1
                    cont = input("Continue? y/n")
                    if cont == 'y':
                        continue
                    if cont == 'n':
                        break
                else:
                    print("Empty Cart")
            else:
                print("Select a different index")
    
while True:
    restaurantlist = open("Restaurants/Restaurants.txt", 'r+')
    restaurants = restaurantlist.readlines()
    #customer = False
    #manager = False
    start=input("Enter 'Order' to order food, type 'Manage' is you're a manager, 'exit' to close:- ")
    if restart == True:
        restart = False
        
    if start=='o' or start=='O' or start=='order' or start=='Order':
        #customer = True
        #manager = False
        print("Welcome Customer")
        customer()
        
    elif start=='m' or start=='M' or start=='manage' or start=='Manage':
        print("Welcome Manager")
        #manager = True
        #customer = False

    elif start=='exit':
        print("exiting")
        restaurantlist.close()
        break
    

        
