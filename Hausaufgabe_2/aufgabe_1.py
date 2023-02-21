# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# Пример:
# 5 -> 1 0 1 1 0
# 2

import random


print("Примем за аверс '0', а за реверс '1'")
print('Введите нужное количество монет: ')
n = int(input())
countAv = 0
countRev = 0

münzen = []
for i in range(n):
    seite = random.randint(0, 1)
    münzen.append(seite)
print(münzen)

for münze in münzen:
    if münze == 0:
        countAv += 1
    elif münze == 1:
        countRev += 1

if countAv < countRev:
    print(f"Нужно перевернуть {countAv}.")
else:
    print(f"Нужно перевернуть {countRev}.")
