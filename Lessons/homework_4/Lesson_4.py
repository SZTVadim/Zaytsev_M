# Задание 1: Работа с типами данных

text = "Привет"
number = 42
float_number = 3.14
numbers = [1, 2, 3]

print(type(text))
print(type(number))
print(type(float_number))
print(type(numbers))

# Задание 2: Преобразование регистра строк

text_1 = "Python PROGRAMMING"

print(text_1.lower())
print(text_1.upper())
print(text_1.capitalize())
print(text_1.title())

# Задание 3: Удаление пробелов

text_2 = " Hello World "

print(text_2.strip())
print(text_2.lstrip())
print(text_2.rstrip())

# Задание 4: Разделение и объединение строк

fruits = "яблоко,банан,апельсин,груша"
fruits_list = fruits.split(",")
fruits_text = " ".join(fruits_list)

print(fruits_list)
print(fruits_text)

# Задание 5: Замена подстрок

text_3 = "Я изучаю Python. Python - это круто!"

print(text_3.replace("Python", "Java"))

# Задание 6: Поиск и подсчет

text_4 = "Python программирование на Python"

print(text_4.find("Python"))
print(text_4.count("Python"))
print(text_4.find("Java"))

# Задание 7: Проверка типа символов

print("Hello123".isalnum())
print("12345".isdigit())
print("Hello".isalpha())
print("   ".isspace())

# Задание 8: Срезы строк

text_5 = "Python very good"

print(text_5[:3])
print(text_5[-3:])
print(text_5[::2])
print(text_5[::-1])

# Задание 9: Экранирование символов

print('Он сказал: "Привет"')
print("Первая строка\nВторая строка")
