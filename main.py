#CS Project XII-A
#Memebers- Gokul, Srichaitanya, Adarsh
#Project topic - Food ordering app

import json

customer = False
manager = False
restart = False


while True:
    print(customer)
    start=input("Type C to order food, type M is you're a manager")
    restaurantlist = open("Restaurants/Restaurants.txt", 'r+')
    if start=='c' or start=='C' or start=='customer' or start=='Customer':
        customer = True
        manager = False
        print("Welcome customer. Please take a look at the list of restaurants to choose from:-")
        restaurants = restaurantlist.readlines()
        restaurants = [line.rstrip('\n') for line in restaurants]
        print(restaurants)
        for restaurant in restaurants:
            restaurant = json.loads(restaurant)
            print(restaurant['index']+':-'+restaurant['name'])
        
    elif start=='m' or start=='M' or start=='manager' or start=='Manager':
        manager = True
        customer = False
    elif restart == True:
        restart = False
        customer = False
        manager = False
    elif start=='exit':
        print("exiting")
        restaurantlist.close()
        break

        
