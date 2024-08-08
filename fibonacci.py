def caching_fibonacci(): # створюємо функцію, яка створює та використовує кеш для зберігання
    # і повторного використання вже обчислених значень чисел Фібоначчі.

    cache  = [] # Створюємо порожній словник cache, для зберігання результатів обчислення 
    def fibonacci(n): # Створюємо функцію з урахуванням використання кешу.
        nonlocal cache
        if n <= 0: # умови функції Фібоначчі
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
             return  fibonacci(n - 1) + fibonacci(n - 2) # рекурсивний випадок
            
    return fibonacci

fib = caching_fibonacci() # виклик функції 
print(fib(10))
print(fib(15))
