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
    if start=='c' or 'C' or 'customer' or 'Customer':
        customer = True
        manager = False
        print("Welcome customer. Please take a look at the list of restaurants to choose from:-")
        restaurants = restaurantlist.readlines()
        restaurants = [line.rstrip('\n') for line in restaurants]
        for i in restaurants:
            print(i)
            
            #restaurant = json.loads(restaurant)
            #print(restaurant['index']+':-'+restaurant['name'])
        
    elif start=='m' or 'M' or 'manager' or 'Manager':
        manager = True
        customer = False
        
    elif start=='exit':
        print("exiting")
        restaurantlist.close()
        break

        
