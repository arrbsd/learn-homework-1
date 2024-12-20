"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""

def discounted(price, discount, max_discount=20):
    try:
        # переводим к вещественному типу
        price = float(price)
        discount = float(discount)

        # переводим к целому типу
        max_discount = int(max_discount)

        # ...
        # Выполняем код функции из примера про функции
        # ...

    except (ValueError, TypeError) as e:
        return f"Неверный ввод данных {e}"

if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("тысяча", "20983"))
    print(discounted(100.0, 5, "10"))
