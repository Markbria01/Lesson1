#Создайте список из чисел 3, 5, 7, 9 и 10.5
#Выведите содержимое списка на экран
#Добавьте в конец списка строку "Python"
#Выведите длину списка на экран

list1 = [3, 5, 7, 9, 10.5]
print(list1)


#Выведите на экран начальный элемент списка
#Выведите на экран последний элемент списка
#Напечатайте элементы списка со второго по четвертый включительно
#Удалите из списка строку "Python"


list1.append('Python')
print(len(list1))

print(list1[0])
print(list1[-1])
print(list1[1:4])

del list1[-1]

print(list1)


#Создайте словарь:
#{"city": "Москва", "temperature": "20"}
#Выведите на экран значение ключа city
#Уменьшите значение "temperature" на 5
#Выведите на экран весь словарь

weather_city = {
    'city': 'Москва', 
    'temperature': '20'
    }

print(weather_city['city'])
print(weather_city)


weather_city['temperature'] = 15

print(weather_city)

#Проверьте, есть ли в словаре ключ country
#Выведите значение по-умолчанию "Россия" для ключа country
#Добавьте в словарь элемент date со значением "27.05.2019"
#Выведите на экран длину словаря


print(weather_city.get('country'))

weather_city['country'] = 'Россия'

weather_city['date'] = '16.05.2021'

print(weather_city)

print(len(weather_city))