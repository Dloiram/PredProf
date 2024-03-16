def products(): 
    a = open("products.txt", "r+", encoding='utf-8').readlines()
    for i in range(len(a)):
        a[i] = list(map(str,a[i].split(";")))
        a[i][-1] = a[i][-1][:-1]
    return a
    
""" Функция считывания Файла """

a = products()


c = 0

for i in range(len(a)):
    if a[i][0] == "Закуски":
        c += float(a[i][-1]) * float(a[i][-2])
"""Тело кода"""


print(c)
