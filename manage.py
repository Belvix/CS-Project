#Shichi do  your thing here
def manage():
    global Restaurants
    restaurant_list = [line.rstrip('\n') for line in restaurants]
    restaurant_dict_list = [json.loads(restaurant) for restaurant in restaurant_list]
    for i in restaurant_dict_list:
        print(i["name"])
    


