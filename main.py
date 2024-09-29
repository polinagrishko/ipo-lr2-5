def time(n):
    min = 24 * 60
    
    n = n % min
    
    hours = n // 60
    min = n % 60
    
    return hours, min

n = int(input("Введите количество минут с начала суток: "))

hours, minutes = time(n)
print(f"Часы: {hours}, Минуты: {min}")
