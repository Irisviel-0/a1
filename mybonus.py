from math import sqrt as sqrt


grid_map = []    # Put the map in a list as a two-dimentional data
for num in range(1, 11):
    ''' The for loop will generate each column of the map at a time '''
    grid_map.append([x+str(num) for x in "ABCDEFGHIJ"])


def restaurants_in_range(distance, epicenter):
    ''' Return a list of restaurants which are strictly less than distance
        away from the rat infestation epicenters'''
    results_list = []
    for i in range(0, 10):
        for j in range(0, 10):
            to_mr = sqrt((epicenter[0] - i - 0.5) ** 2 + 
                         (epicenter[1] - j - 0.5) ** 2)
            to_cr = sqrt((epicenter[0] - i) ** 2 + (epicenter[1] - j) ** 2)
            if to_cr < distance:
                results_list.append(grid_map[i][j] + 'CR')
            if to_mr < distance:
                results_list.append(grid_map[i][j] + 'MR')
    return results_list


def find_restaurants_to_shut(distance, list_of_epicentres):
    restaurants_list = []
    for p in list_of_epicentres:
        restaurants_list = restaurants_list.__add__(
                                   [sorted(restaurants_in_range(distance, p))])
    return restaurants_list


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_restaurants_to_shut(1.0, [[3.0, 3.0]]))
    print(find_restaurants_to_shut(0.4, [[1.0, 1.0], [2.0, 2.0]]))
