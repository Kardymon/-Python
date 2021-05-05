my_list = [7, 5, 3, 3, 2]
new_value = int(input("введите новое значение: "))
new_list = my_list.copy()
if new_value in my_list:
    for el in my_list:
        index = len(my_list) - 1 - my_list[::-1].index(new_value)
        new_list = my_list.copy()
        new_list.insert(index + 1, new_value)
        print(new_list)
else:
        new_list.append(new_value)
        new_list.sort(reverse = True)
        print(new_list)


