def products():
    a = open("products.txt", "r+", encoding='utf-8').readlines()
    for i in range(len(a)):
        a[i] = list(map(str,a[i].split(";")))
        a[i][-1] = a[i][-1][:-1]
    return a


a = products()
a[0].append("promocode")
for i in range(1,len(a)):
    a[i].append(str(a[i][1][0] + a[i][1][1] + a[i][2][0] + a[i][2][1] + a[i][1][-1] + a[i][1][-2] + a[i][2][4] + a[i][2][3]))
    

