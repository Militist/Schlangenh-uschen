# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите первую сторону плитки: ')
n = int(input())
print('Введите вторую сторону плитки: ')
m = int(input())
print('Введите количесвто желанных долек: ')
k = int(input())
m, n, k = [int(input()) for i in range(3)]

num = n * m
if k < num and (k % n == 0 or k % m == 0):
    print('yes')
else:
    print('no')
