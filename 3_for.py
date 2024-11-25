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

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
sales = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

#Функция расчета суммарной продажи каждого товара
def count_sold(product_sales):
    one_product_total_sold = 0
    for sold in product_sales:
        one_product_total_sold += sold
    return one_product_total_sold

#Посчитать и вывести суммарное количество продаж для каждого товара
for product_sales in sales:
    product_total_sold = count_sold(product_sales['items_sold'])
    print (f'Общее количество проданных {product_sales["product"]} - {product_total_sold}')


#Посчитать и вывести среднее количество продаж для каждого товара
for product_sales in sales:
    product_total_sold = count_sold(product_sales['items_sold'])
    product_sold_avg = round(product_total_sold / len(product_sales['items_sold']),2)
    print (f'Среднее количество продаж {product_sales["product"]} - {product_sold_avg}')


#Посчитать и вывести суммарное количество продаж всех товаров
sold_count = 0
for one_sales in sales:
    sold_count += count_sold(one_sales['items_sold'])
print (f'Суммарное количество проданных товаров - {sold_count}')

#Посчитать и вывести среднее количество продаж всех товаров
print (f'Среднее количество проданных товаров - {sold_count/len(sales)}')

if __name__ == "__main__":
    main()
