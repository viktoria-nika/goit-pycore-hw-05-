import re
from typing import Callable
# імпортуємо потрібні модулі для розвязування задачі

def generator_numbers(text: str): # створюємо функцію для генерування чисел, ка приймає наш текст для опрацювання
    nums = re.findall(r'\d*\.\d+|\d+', text)  # за домомогою функції findall з модуля re вибираємо числа з тексту 
    for i in nums:   # створюємо генератор за допомогою конструктора yield
        yield float(i)

def sum_profit(text: str, func: Callable):  # створюємо функцію для обчислення загальної суми чисел використовуючи створений генероатор
    sum_d = sum(func(text))
    return sum_d

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")