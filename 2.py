sec = int(input('Введите секунды: '))
min = sec // 60
hours = min // 60
print(f"Время: {hours:02d}:{min % 60:02d}:{sec % 60:02d}")



