def time_from_minutes(n):
    minutes_in_day = 24 * 60
    
    n = n % minutes_in_day
    
    hours = n // 60
    minutes = n % 60
    
    return hours, minutes

n = int(input("Введите количество минут с начала суток: "))

hours, minutes = time_from_minutes(n)
print(f"Часы: {hours}, Минуты: {minutes}")