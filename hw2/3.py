month_list = [[1, 2, 12, "зима"], [3, 4, 5, "весна"], [6, 7, 8, "лето"], [9, 10, 11, "осень"]]
dic_list = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
a = int(input("Введите номер месяца: "))

for el in month_list:
    if a in el:
        print(f"сезон {el[-1]} - через list")

for key, value in dic_list.items():
    if a in value:
        print(f'сезон {key} - через dic')
