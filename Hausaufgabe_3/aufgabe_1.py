# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random


print('Введите длину диапазона: ')
n = int(input())
print('Введите искомое число: ')
gesuchtes = int(input())

count = 0
nums = []
for i in range(n):
    nums.append(random.randint(1, 100))
print(nums)
for i in nums:
    if i == gesuchtes:
        count = count + 1
if len(nums) != 0:
    minDifferent = abs(gesuchtes - nums[0])
    element = nums[0]
for j in range(0, len(nums)):
    Different = abs(gesuchtes - nums[j])
    if minDifferent >= Different:
        minDifferent = Different
        element = nums[j]
print(element)
