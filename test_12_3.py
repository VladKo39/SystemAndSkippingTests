''''''
'''test_12_3 formed from runner and runner_and_tournament'''
import unittest
from runner_and_tournament import Runner, Tournament

TestCase = unittest.TestCase


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, ' Тесты в этом кейсе заморожены')
    def test_walk(self):
        wolker = Runner('Тихоня')
        for i in range(10):
            wolker.walk()
        self.assertEqual(wolker.distance, 50, 'test_walk: Test is filed!')
        
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Торопыжка')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, 'test_run: Test is filed!')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        wolker = Runner('Александра')
        runner = Runner('Александр')

        for i in range(10):
            wolker.walk(), runner.run()
        self.assertNotEqual(wolker.distance, runner.distance, 'test_challenge: Test is filed!')


class TournamentTest(TestCase):
    is_frozen = True

    # дополнить атрибутом is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usan = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_fist_tur(self):
        tur = Tournament(90, self.usan, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tur(self):
        tur = Tournament(90, self.andrey, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tur(self):
        tur = Tournament(90, self.usan, self.andrey, self.nik)
        resault = {k: str(v) for k, v in tur.start().items()}

        TournamentTest.all_results.append(resault)
        self.assertTrue(resault[3], 'Ник')


if __name__ == '__main__':
    unittest.main()
