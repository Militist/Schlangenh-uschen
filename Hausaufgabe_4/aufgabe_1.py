# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите число N элементов:"))
num_list_1=[]
for i in range(n):
    num = int(input("Введите число:"))
    num_list_1.append(num)
print(num_list_1)


m = int(input("Введите число M элементов:"))
num_list_2 = []
for i in range(m):
    num = int(input("Введите число:"))
    num_list_2.append(num)
print(num_list_2)

num_list3 = num_list_1+num_list_2

print(num_list3)

checked_nums_list = []
for i in num_list3:
    if num_list3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print(i)