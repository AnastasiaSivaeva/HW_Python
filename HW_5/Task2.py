# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

name = ['Anton', 'Mary', 'Alex']
salary = [100_000, 150_000, 170_000]
prize = ['10.25%', '12.45%', '15%']


def dict_gen(name: list[str], salary: list[int], prize: list[str]) -> dict[str: float]:
    return {name: sale / 100 * bon for name, sale, bon in zip(name, salary, (float(i[:-1]) for i in prize))}.items()


print(*(dict_gen(name, salary, prize)))