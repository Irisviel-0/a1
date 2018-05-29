grid_map = []    # Put the map in a list as a two-dimentional data
for num in range(1, 11):
    ''' The for loop will generate each column of the map at a time '''
    grid_map.append([x+str(num) for x in "ABCDEFGHIJ"])

def find_my_neighbourhood(x, y):
    ''' Using the provided coordinates to locate the neighbourhood '''
    return grid_map[int(x)][int(y)]

def find_all_restaurants_in_neighbourhood(x, y):
    ''' To find all restaurants in specific area '''
    place = find_my_neighbourhood(x, y)
    return [place + 'CR', place + 'MR']

if __name__ == "__main__":
   for i in range(1,100):
        for j in range(1,100):
            print(find_my_neighbourhood(i/10,j/10))
            print(find_all_restaurants_in_neighbourhood(i/10,j/10))
    
