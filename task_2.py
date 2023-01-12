"""Задайте натуральное число N. Напишите программу, которая составит
 список простых множителей числа N."""

number = int(input("Введите число: "))
list_of_numbers = []
input_number = number
i = 2
while i <= number:
    if number % i == 0:
        list_of_numbers.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f" Список простых множителей числа {input_number} : {list_of_numbers}")