a = input("Введите строку из нескольких слов через пробел: ").split()
for ind, el in enumerate(a, 1):
    print(ind, el[:10])