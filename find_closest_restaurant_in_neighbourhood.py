from find_my_neighbourhood import find_all_restaurants_in_neighbourhood as find_all_restaurants_in_neighbourhood
def find_closest_restaurant_in_neighbourhood(x, y):
    list2 = find_all_restaurants_in_neighbourhood(x, y)
    if y == (int(x)+int(y)+0.5) - x:
        print(list2)
    elif y < (int(x)+int(y)+0.5) - x:
        print(list2[0])
    else:
        print(list2[1])
              
    return list2


def find_farthest_restaurant_in_neighbourhood(x, y):
    list3 = find_all_restaurants_in_neighbourhood(x, y)
    if y == (int(x)+int(y)+0.5) - x:
        print(list3)
    elif y < (int(x)+int(y)+0.5) - x:
        print(list3[1])
    else:
        print(list3[0])
              
    return list3

if __name__ == "__main__":
   for i in range(100):
        for j in range(100):
            print(find_closest_restaurant_in_neighbourhood(i/10, j/10))
            print(find_closest_restaurant_in_neighbourhood(i/10, j/10))
