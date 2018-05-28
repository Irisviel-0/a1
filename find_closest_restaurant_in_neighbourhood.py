import find_my_neibourhood
def find_closest_restaurant_in_neighbourhood(x, y):
    list2 = find_all_restaurants_in_neibourhood(x, y)
    if y == (int(x)+int(y)+0.5) - x:
        print(list2)
    elif y < (int(x)+int(y)+0.5) - x:
        print(list2[0])
    else:
        print(list2[1])
              
    return list2


def find_farthest_restaurant_in_neighbourhood(x, y):
    list3 = find_all_restaurants_in_neibourhood(x, y)
    if y == (int(x)+int(y)+0.5) - x:
        print(list3)
    elif y < (int(x)+int(y)+0.5) - x:
        print(list3[1])
    else:
        print(list3[0])
              
    return list3
    
    
