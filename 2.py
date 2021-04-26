sec = int(input("Введите время в секундах: "))
min = sec // 60
hours = min // 60
print(f'введенное время: {hours:02d}:{min % 60:02d}:{sec % 60:02d}')
