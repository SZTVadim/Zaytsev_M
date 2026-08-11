# Задание 1. Добавление элементов в список

fruits = ["яблоко"]
print(fruits)

fruits.append("банан")
print(fruits)

fruits.extend(["апельсин", "груша"])
print(fruits)

fruits.insert(1, "виноград")
print(fruits)
print("\n")

# Задание 2. Удаление элементов из списка

fruits_1 = ["яблоко", "банан", "апельсин", "банан"]
print(fruits_1)

fruits_1.remove("банан")
print(fruits_1)

del_fruit = fruits_1.pop()
print(del_fruit)
print(fruits_1)
print("\n")

# Задание 3. Поиск элементов в списке

fruits_2 = ["яблоко", "банан", "апельсин", "банан"]
print(fruits_2)

fruit_index = fruits_2.index("банан")
print(fruit_index)

fruit_count = fruits_2.count("банан")
print(fruit_count)
print("\n")

# Задание 4. Сортировка и реверс списка

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
