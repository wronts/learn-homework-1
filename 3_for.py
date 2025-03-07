"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phone_sales_statistics = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def main():
    total_count = 0
    len_count = 0
    for item in range(len(phone_sales_statistics)):
        product = phone_sales_statistics[item]["product"]
        items_sold = phone_sales_statistics[item]["items_sold"]
        total_count += sum(items_sold)
        len_count += len(items_sold)

        print(f'Всего смартфонов "{product}" продано {sum(items_sold)} шт.')
        print(f'В среднем смартфонов "{product}" продано {sum(items_sold) / len(items_sold):.0f} шт.')
        print()
    print(f'Всего продано смартфонов: {total_count}')
    print(f'В среднем продано смартфонов: {total_count / len_count :.0f}')


if __name__ == "__main__":
    main()
