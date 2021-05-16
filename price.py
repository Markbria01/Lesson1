#Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает объединенными через разделитель delimiter
#Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return (one + delimiter + two)

tonul = get_summ("Learn", "Python")
print(tonul.upper())





def format_price(price):
    price = int(price)
    return f" Цена: {price} руб."

result = format_price(56.24)
print(result)