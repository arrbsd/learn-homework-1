"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

def compare_str(str1,str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0

    if str2 != 'learn':
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
    else:
        return 3

print(compare_str("Строка", "Строка"))
print(compare_str("hello", "world"))
print(compare_str("Python", "learn"))
print(compare_str("learn", "Python"))
print(compare_str("Длинная строка", "Просто строка"))
print(compare_str("просто строка", "Длинная строка"))
print(compare_str("Проверка", 20983))
print(compare_str(20983, "Проверка"))

if __name__ == "__main__":
    main()
