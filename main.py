n = int(input("Введите количество минут прошедших с начала суток: "))
minutes_in_day=1440
n=n% minutes_in_day
hours=n//60
minutes = n%60
print(f"Часы: {hours}, Минуты: {minutes}")