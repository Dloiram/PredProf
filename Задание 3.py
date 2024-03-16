def products():
    a = open("products.txt", "r+", encoding='utf-8').readlines()
    for i in range(len(a)):
        a[i] = list(map(str,a[i].split(";")))
        a[i][-1] = a[i][-1][:-1]
    return a
"""Считывание файла"""


a = products()

b = input("Введите название котегории: ")

n = ""

while b != "молоко":
    f = 0
    mini = 9999
    for i in range(1,len(a)):
        if a[i][0] == b and float(a[i][-1]) <= mini:
            mini = float(a[i][-1])
            n = a[i][1]
            f = 1
    """Поиск по критериям"""
    if f:
        print("В категории: " + str(b) + " товар: " + str(n) + " был куплен " + str(mini) + " раз")
    else:
        print("Такой категории не существует в нашей БД")
    b = input("Введите название котегории: ")
    """Отбор решений и вывод"""
