from collections import defaultdict
from math import sqrt as sqrt


grid_map = []    # Put the map in a list as a two-dimentional data
for num in range(1, 11):
    ''' The for loop will generate each column of the map at a time '''
    grid_map.append([x+str(num) for x in "ABCDEFGHIJ"])
    

def find_closest_restaurant(x, y):
    ''' Return the closest restaurant from a give position '''
    results_dict = defaultdict(list)
    for i in range(0, 10):
        for j in range(0, 10):
            to_mr = sqrt((x - i - 0.5) ** 2 + (y - j - 0.5) ** 2)
            to_cr = sqrt((x - i) ** 2 + (y - j) ** 2)
            results_dict[to_cr].append(grid_map[i][j] + 'CR')
            results_dict[to_mr].append(grid_map[i][j] + 'MR')
    return results_dict[min(results_dict.keys())]


def find_closest_restaurant_on_path(list_of_stops):
    ''' Return the closest restaurants for each given stop in a list '''
    results = []
    for position in list_of_stops:
        results = results.__add__([find_closest_restaurant(position[0], 
                                                           position[1])])
    return sorted(results)

if __name__ == "__main__":
   for i in range(100):
        for j in range(100):
            print(find_closest_restaurant_on_path([[i,j],[(i+j)%10, abs(i-j)]]))
