import unittest
from calculadora import calcular_tmb_homem, calcular_tmb_mulher

class TestCalculadoraTMB(unittest.TestCase):
    def test_tmb_homem(self):
        self.assertAlmostEqual(calcular_tmb_homem(70, 175, 30), 1648.75, places=1)

    def test_tmb_mulher(self):
        self.assertAlmostEqual(calcular_tmb_mulher(60, 165, 25), 1345.25, places=1)

if __name__ == '__main__':
    unittest.main()