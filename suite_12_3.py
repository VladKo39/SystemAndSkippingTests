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

# calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_and_tournament.CalcTest))
# '''
# собираем все тесты в один «test_suite»,
#  но мы также можем организовать их по отдельности и запускать каждую группу тестов самостоятельно.
# На данный момент мы запустим все тесты как единый блок и увидим,
# что все прошло успешно, включая тесты из «test_calc» и «test_new_calc»
# '''
#
# runner = unittest.TextTestRunner(verbosity=2)  # 1
# '''
# Существует параметр «verbosity».Он позволяет изменять уровень детализации вывода тестов.
# Например, как видно, показываются конкретные тесты, которые мы прошли
# runner=unittest.TextTestRunner(verbosity=1)
# >>>Ran 4 tests in 0.000s
# А при runner=unittest.TextTestRunner(verbosity=2)
# какие конкретно тесты были пройдены
# test_add (a2Test_calc_metod_unit.CalcTest.test_add)
# Test for add function in calculator ... ok
# test_div (a2Test_calc_metod_unit.CalcTest.test_div) ... ok
# test_mul (a2Test_calc_metod_unit.CalcTest.test_mul) ... ok
# test_sub (a2Test_calc_metod_unit.CalcTest.test_sub) ... ok
#
#
# 1
# Настроить запуск тестов. Можно создать отдельный файл «runner»,
# но также можно сделать это прямо здесь:
# мы обращаемся к «unittest» и используем «TextTestRunner»
# '''
# runner.run(calcST)  # 2
# '''2
# запустить тесты прямо здесь.
#  Необходимо указать, по какому «TestSuite» будет производиться запуск.
# В нашем случае это «calcST».
# Если мы запустим тесты, то увидим, что все они пройдены, и всё работает прекрасно
# '''
