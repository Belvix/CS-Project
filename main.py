#CS Project XII-A
#Memebers- Gokul, Srichaitanya, Adarsh
#Project topic - Food ordering app

import json

customer = False
manager = False

while True:
    print(customer)
    start=input("Are you a customer or a mangager? Type c for customer and m for manager")
    restaurantlist = open("Restaurants/Restaurants.txt", 'r+')
    if start=='c' or 'C' or 'customer' or 'Customer' and customer ==False and manager==False:
        customer = True
        manager = False
        print("Welcome customer. Please take a look at the list of restaurants to choose from:-")
        for restaurant in restaurantlist:
            print(restaurant)
            #restaurant = json.loads(restaurant)
            #print(restaurant['index']+':-'+restaurant['name'])
        
    if start=='m' or 'M' or 'manager' or 'Manager' and customer ==False and manager==False:
        manager = True
        customer = False
    if start=='exit':
        print("exiting")
        restaurantlist.close()
        break
    if customer==True:
        print("Welcome customer. Please take a look at the list of restaurants to choose from:-")
        for restaurant in restaurantlist:
            print(restaurant)
            #restaurant = json.loads(restaurant)
            #print(restaurant['index']+':-'+restaurant['name'])
        
