#Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии

def pow_recursive(n, m):
    if m == 0:
        return 1
    else:
        return n * pow_recursive(n, m - 1)

print('Введите первое числоо:')
a = int(input())
print('Введите второе число:')
b = int(input())
res = pow_recursive(a, b)
print(res)
