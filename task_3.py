"""Задайте последовательность чисел. Напишите программу, которая выведет
 список неповторяющихся элементов исходной последовательности."""

our_list = list(map(int, input("Введите числа через пробел: ").split()))
new_list = []
[new_list.append(i) for i in our_list if i not in new_list]
print(f"Первоначальный список: {our_list}")
print(f"Список неповторяющихся элементов исходной последовательности: {new_list}")