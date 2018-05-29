def find_my_neighbourhood(x, y):
        NameStr = 'ABCDEFGHIJ'
        a = NameStr[int(y)]+str(int(x)+1)

        return a

def find_all_restaurants_in_neighbourhood(x, y):
    Neib = find_my_neighbourhood(x, y)
    list1 = [str(Neib)+'CR', str(Neib)+'MR']
        
    return list1

if __name__ == "__main__":
   for i in range(1,100):
        for j in range(1,100):
            print(find_my_neighbourhood(i/10,j/10))
            print(find_all_restaurants_in_neighbourhood(i/10,j/10))
