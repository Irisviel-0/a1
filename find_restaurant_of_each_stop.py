import find_my_neighbourhood
import find_closest_restaurant_in_neighbourhood
def find_closest_restaurant(x, y):
    x = float(x)
    y = float(y)
    NameStr = 'ABCDEFGHIJ '
    a = NameStr[int(y)]+str(int(x)+1)
    aa = a+'CR'
    ab = a+'MR'
    b = NameStr[int(y+1)]+str(int(x)+1)
    ba = b+'CR'
    bb = b+'MR'
    c = NameStr[int(y+1)]+str(int(x)+2)
    ca = c+'CR'
    d = NameStr[int(y)]+str(int(x)+2)
    da = d+'CR'
    db = d+'MR'
    e = NameStr[int(y-1)]+str(int(x)+1)
    eb = e+'MR'
    f = NameStr[int(y)]+str(int(x))
    fb = f+'MR'
    list4 = []
    if x == int(x) and y == int(y)+0.5:
        list4.append(aa)
        if int(x) == 0:
            list4.append(ba)
            list4.append(ab)
        else:
            list4.append(ba)
            list4.append(fb)
            list4.append(ab)
    elif x == int(x)+0.5 and y == int(y):
        list4.append(aa)
        if int(y) == 0:
            list4.append(ab)
            list4.append(da)
        else:
            list4.append(ab)
            list4.append(eb)
            list4.append(da)
        if int(x) == 9:
            del list4[-1]
        else:
            list4 = list4
    elif y == (int(x)+int(y)+0.5) - x:
        list4.append(aa)
        list4.append(ab)
    elif y == (int(x)+int(y)+0.5) + x:
        list4.append(ab)
        list4.append(ba)
    elif y == (int(x)+int(y)+1.5) - x:
        list4.append(ab)
        list4.append(ca)
    elif y == (int(x)+int(y)+1.5) + x:
        list4.append(ab)
        listr.append(da)
    elif y < (int(x)+int(y)+0.5) - x:
        list4.append(aa)
    elif y > (int(x)+int(y)+0.5) + x:
        list4.append(ba)
    elif y > (int(x)+int(y)+1.5) - x:
        list4.append(ca)
    elif y < (int(x)+int(y)+1.5) + x:
        list4.append(da)
    else:
        list4.append(ab)


        return list4

    
def find_closest_restaurant_on_path(list5):
    Ronpa = []
    for item in list5:
        x = float(item[0])
        y = float(item[1])
        A = find_closest_restaurant(x, y)
        Ronpa.append(A)
    print(Ronpa)


if __name__ == "__main__":
   for i in range(100):
        for j in range(100):
            print(find_closest_restaurant_on_path([[i,j],[(i+j)%10, abs(i-j)]]))
#没运行不知道好不好用，自己感觉没有问题喵……
