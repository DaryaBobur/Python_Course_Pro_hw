# 1. Рядки (Strings):
# Напишіть функцію, яка приймає рядок і повертає його довжину.

def text(string):
    return len(string)

print(text("Hello!"))

# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.

def text(first_str, second_str):
    return f"{first_str} {second_str}!"

print(text("Hello", "World"))

# 2. Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає його квадрат.

def square_number(num):
    return num ** 2

print(square_number(2))

# Створіть функцію, яка приймає два числа і повертає їхню суму.

def amount_number(first_num, second_num):
    return first_num + second_num

print(amount_number(2, 3))

# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.
def numbers(first_num, second_num):
    return divmod(first_num, second_num)

print(numbers(11, 3))

# ще один варіант

def numbers(first_num, second_num):
    num_1 = first_num // second_num
    num_2 = first_num % second_num
    return num_1, num_2

print(numbers(13, 2))

# 3. Списки (Lists):
#
# Напишіть функцію для обчислення середнього значення списку чисел.

def average_value(nums):
    sum_num = 0
    for i in nums:
        sum_num += i
    return sum_num / len(nums)

print(average_value([1,2,3,4,6]))

# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.

def find_common_elements(first_lst, second_lst):
    general_lst = []

    for i in first_lst:
        if i in second_lst:
            general_lst.append(i)
    return general_lst

list_1 = list(range(1, 15, 2))
list_2 = list(range(1, 20, 3))

print(find_common_elements(list_1, list_2))

# 4. Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.

def dictionary_key(dct):
    return dct.keys()

watermelon_profile = {
        "name": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "calories_per_100g": 30,
        "color": "Green with red flesh",
        "season": ["July", "August", "September"],
        "benefits": ["Highly hydrating", "Contains lycopene", "Low in calories"]
}

print(dictionary_key(watermelon_profile))

# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.

def dictionaries(first_dict, second_dict):
    general_dict = first_dict | second_dict
    return general_dict

watermelon_profile = {
        "name": "Watermelon",
        "scientific_name": "Citrullus lanatus",
        "calories_per_100g": 30,
}

watermelon_description = {
    "color": "Green with red flesh",
    "season": ["July", "August", "September"],
    "benefits": ["Highly hydrating", "Contains lycopene", "Low in calories"]
}

print(dictionaries(watermelon_profile, watermelon_description))

# 5. Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.

def union_sets(first_set, second_set):
    general_set = first_set.union(second_set)
    return general_set

set_A = {1, 3, 7, 9, 6}
set_B = {2, 4, 11, 85, 5}

print(union_sets(set_A, set_B))

# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.

def is_subset(set_1, set_2):
    for i in set_1:
        if i not in set_2:
            return False
    return True

my_set_1 = {1, 3, 7, 8}
my_set_2 = {1, 7, 12, 3}

print(is_subset(my_set_1, my_set_2))

# 6. Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.

def numbers(num):
    if num % 2 == 0:
        print("Число парне:", num)
    else:
        print("Число непарне:", num)

numbers(13)

# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.

def num_list(lst):
    new_list = []
    for i in lst:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

numbers = list(range(0, 12))

print(num_list(numbers))

# 7. Написати лямбда-функцію визначальну парне/непарне.
# Функція приймає параметр (число) і якщо парне, видає слово “парне”, якщо ні - то “не парне”.

check_even = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(check_even(6))