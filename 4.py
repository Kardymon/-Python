a = int(input("Введите целое положительное число: "))
b = 0
while a > b:
    c = a % 10
    if c > b:
        b = c
    a = a // 10
print(b)
