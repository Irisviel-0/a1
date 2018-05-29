from math import sqrt as sqrt
from collections import defaultdict


grid_map = []    # Put the map in a list as a two-dimentional data
for num in range(1, 11):
    ''' The for loop will generate each column of the map at a time '''
    grid_map.append([x+str(num) for x in "ABCDEFGHIJ"])

    
def distance_to_restaurant(x, y):
    ''' Return a defaultdict including distance(keys) 
        and neighbourhoods(values)'''
    to_mr = sqrt((x - int(x) - 0.5) ** 2 + (y - int(y) - 0.5) ** 2)
    to_cr = sqrt((x - int(x)) ** 2 + (y - int(y)) ** 2)
    results_dict = defaultdict(list)
    results_dict[to_cr].append(grid_map[int(x)][int(y)] + 'CR')
    results_dict[to_mr].append(grid_map[int(x)][int(y)] + 'MR')
    return results_dict


def find_closest_restaurant_in_neighbourhood(x, y):
    ''' Return the closest restaurant '''
    distance_dict = distance_to_restaurant(x, y)
    return distance_dict[min(distance_dict.keys())]


def find_farthest_restaurant_in_neighbourhood(x, y):
    ''' Return the farthes restaurant '''
    distance_dict = distance_to_restaurant(x, y)
    return distance_dict[max(distance_dict.keys())]

if __name__ == "__main__":
   for i in range(100):
        for j in range(100):
            print(find_closest_restaurant_in_neighbourhood(i/10, j/10))
            print(find_closest_restaurant_in_neighbourhood(i/10, j/10))
