name = []
price = []
quantity = []
unit = []
product_list = []
num = 1
product_number = int(input("Введите количество продуктов в списке: "))
while product_number >= num:
    product_dic = {"Название": input('Введите название : '), "Цена": input('Введите цену: '), "Количество": input("Введите количество: "), "Единица": input("введите единицу измерения: ")}
    name.append(product_dic.get("Название"))
    price.append(product_dic.get("Цена"))
    quantity.append(product_dic.get("Количество"))
    unit.append(product_dic.get("Единица"))
    product_tuple = [num, product_dic]
    product_list.append(product_tuple)
    num += 1
for el in product_list:
    print(el)

a = {"Название": name, "Цена": price, "Количество": quantity, "Единица": unit}
for key in a:
    print(key,'->', a[key])

