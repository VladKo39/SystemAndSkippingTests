import unittest
import test_12_3

suite_ = unittest.TestSuite()
# получен метод suite_12_3
loader_ = unittest.TestLoader()
#
suite_.addTest(loader_.loadTestsFromTestCase(test_12_3.RunnerTest))
suite_.addTest(loader_.loadTestsFromTestCase(test_12_3.TournamentTest))
# В Новый метод также добавляет тесты,
# с помощью метода «TestLoader» и функции «loadTestsFromTestCase».
# Указываем путь к нашему «TestCase», то есть модуль, откуда мы его берём, и название класса.

runner_ = unittest.TextTestRunner(verbosity=2)
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
runner_.run(suite_)


