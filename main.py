#CS Project XII-A
#Memebers- Gokul, Srichaitanya, Adarsh
#Project topic - Food ordering app

import json
import sys

restart = False
cart=[]
cart_items = []

def cart_display(items):
    if len(cart)!=0:
        print("Your cart contains:")
        while True:
            done=[]
            for i in cart:
                if i not in done:
                    done.append(i)
                    c=0
                    for j in cart:
                        if j==i:
                            c+=1
                    items.append([i,c])
            else:
                    break
    else:
        print("Empty cart")
        return 0
    c = 1
    for i in items:
        print(str(c),":-",i[0],'x'+str(i[1]))
        c+=1

    

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
        for r in restaurant_dict_list:
                print(r['index']+':-'+r['name'])
        command = input()
        for restaurant in restaurant_dict_list:

            if command == restaurant['index']:
                with open(restaurant['menu'],'r') as menu:
                    menu_string=menu.readline()         #string form of menu
                    menu_dict = json.loads(menu_string)     #string to list of dictionaries
                    menu.close()
                    while menu_reshow:
                        print("Enter a food item to add, back to go back to restaurant list or type cart to see cart:- ")
                        for items in menu_dict:
                            print(items['index']+':- '+items['item'])
                        menu_choice = input()
                        for items in menu_dict:
                            if menu_choice==items['index']:
                                cart.append(items['item'])
                        if menu_choice == 'back':
                            menu_reshow = False
                        elif menu_choice == 'cart':
                            cart_display(cart_items)
                            cont = input("Continue?\ny to add more, n to select another restaurant, checkout to print receipt\n")
                            if cont == 'y':
                                continue
                            if cont == 'n':
                                break
                            if cont == 'checkout' or cont=='Checkout':
                                wobj=open("receipt.txt",'w')
                                for i in range(len(cart_items)):
                                    s = str(i+1)+":-"+cart_items[i][0]+" x"+str(cart_items[i][1])+'\n'
                                    wobj.write(s)
                                wobj.close()
                                sys.exit()
                    else:
                            print("Select a different index")
                       
            elif command == 'logout':
                restart = True
            elif command == 'cart':
                cart_display(cart_items)
                cont = input("Continue?\ny to add more, n to select another restaurant, checkout to print receipt\n")
                if cont == 'y':
                    continue
                if cont == 'n':
                    break
                if cont == 'checkout' or cont=='Checkout':
                    wobj=open("receipt.txt",'w')
                    for i in range(len(cart_items)):
                        s = str(i+1)+":-"+cart_items[i][0]+" x"+str(cart_items[i][1])+'\n'
                        wobj.write(s)
                    wobj.close()
                    print("Thanks for using the program")
                    sys.exit()
            else:
                print("Select a different index")
                continue
    
while True:
    restaurantlist = open("Restaurants/Restaurants.txt", 'r+')
    restaurants = restaurantlist.readlines()
    start=input("Enter 'Order' to order food, 'exit' to close:- ")
    if restart == True:
        restart = False
        
    if start=='o' or start=='O' or start=='order' or start=='Order':
        print("Welcome Customer")
        customer()
        
    elif start=='exit':
        print("exiting")
        restaurantlist.close()
        break
    

        
