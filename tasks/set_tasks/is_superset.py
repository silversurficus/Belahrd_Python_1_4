"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает True, множество включает в себя другое,
и False, если нет

Не использовать if
"""


def is_superset(set_1: set, set_2: set) -> bool:
    return bool(set_1.issuperset(set_2))


if __name__ == '__main__':
    assert is_superset({1, 2, 3, 4}, {1, 2})
    assert not is_superset({5, 6, 3, 4}, {1, 2})
    print('Решено!')
