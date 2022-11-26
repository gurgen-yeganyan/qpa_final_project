import unittest
from os import remove
from os.path import exists as is_file

from gc_ratio.plotting import represent_gc_ratio


class PlottingTest(unittest.TestCase):
    def test_represent_gc_ratio(self):
        with open('tests/covid_dna.txt') as file:
            dna_data = file.read()
        represent_gc_ratio(dna_data, 300)

        self.assertTrue(is_file('GC_ratio.png'))
        self.assertRaises(TypeError, represent_gc_ratio, 35678, 10)

    def tearDown(self):
        remove('GC_ratio.png')


if __name__ == '__main__':
    unittest.main()
