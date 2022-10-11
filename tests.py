import unittest
from main import *


class Testrep(unittest.TestCase):
    def test_rep(self):
        # Идёт проверка функции ответа бота, где мы подаём строку и ожидаем один из двух исходов
        # где для переменной game (нужна для отслеживания того, что продолжается диалог или нет)
        # и если True, то диалог продолжается, а если False, то диалог заканчивается, при этом в случае с True
        # требуется проверять, если есть слово, то ответить, если нет, то попросить научить
        self.assertEqual(reply('бра'), True)
        self.assertEqual(reply('пока'), False)


if __name__ == '__main__':
    unittest.main()
