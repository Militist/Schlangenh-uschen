# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0

print("Введите число: ")
num = int(input())

a1 = num // 100
a2 = (num // 100) % 10
a3 = num % 10

sum = a1 + a2 + a3

print(sum)
