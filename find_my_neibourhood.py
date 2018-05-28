def find_my_neibourhood(x, y):
        NameStr = 'ABCDEFGHIJ'
        a = NameStr[int(y)]+str(int(x)+1)

        return a

def find_all_restaurants_in_neibourhood(x, y):
    Neib = find_my_neibourhood(x, y)
    list1 = [str(Neib)+'CR', str(Neib)+'MR']
        
    return list1
