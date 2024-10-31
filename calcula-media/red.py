import unittest
from green import calcular_media
from refactor import calcular_media2


class TestMedia(unittest.TestCase):
    def test_todas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0)
        self.assertEqual(calcular_media2(0, 0, 0), 0) 

    def test_notas_maximas(self):
        self.assertEqual(calcular_media(10, 10, 10), 10)
        self.assertEqual(calcular_media2(10, 10, 10), 10)

    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(7.5, 8.5, 9.5), 8.5)
        self.assertAlmostEqual(calcular_media2(7.5, 8.5, 9.5), 8.5)
        


if __name__ == '__main__':
    unittest.main()
