import unittest
from calculadora import calcular_tmb_homem, calcular_tmb_mulher

class TestCalculadoraTMB(unittest.TestCase):
    
    def test_tmb_homem_valores_normais(self):
        """Teste para homem com valores normais"""
        resultado = calcular_tmb_homem(70, 175, 30)
        esperado = 10*70 + 6.25*175 - 5*30 + 5  # 1648.75
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_tmb_mulher_valores_normais(self):
        """Teste para mulher com valores normais"""
        resultado = calcular_tmb_mulher(60, 165, 25)
        esperado = 10*60 + 6.25*165 - 5*25 - 161  # 1345.25
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_tmb_homem_valores_limite(self):
        """Teste para homem com valores mínimos"""
        resultado = calcular_tmb_homem(1, 1, 1)
        esperado = 10*1 + 6.25*1 - 5*1 + 5  # 11.25
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_tmb_mulher_valores_limite(self):
        """Teste para mulher com valores mínimos"""
        resultado = calcular_tmb_mulher(1, 1, 1)
        esperado = 10*1 + 6.25*1 - 5*1 - 161  # -154.75
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_tmb_homem_valores_altos(self):
        """Teste para homem com valores altos"""
        resultado = calcular_tmb_homem(100, 190, 50)
        esperado = 10*100 + 6.25*190 - 5*50 + 5  # 2132.5
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_tmb_mulher_valores_altos(self):
        """Teste para mulher com valores altos"""
        resultado = calcular_tmb_mulher(80, 170, 40)
        esperado = 10*80 + 6.25*170 - 5*40 - 161  # 1501.5
        self.assertAlmostEqual(resultado, esperado, places=2)
    
    def test_comparacao_homem_mulher(self):
        """Teste comparando TMB de homem e mulher com mesmos dados"""
        peso, altura, idade = 70, 175, 30
        tmb_homem = calcular_tmb_homem(peso, altura, idade)
        tmb_mulher = calcular_tmb_mulher(peso, altura, idade)
        
        # Homem deve ter TMB maior que mulher (devido à fórmula)
        self.assertGreater(tmb_homem, tmb_mulher)
    
    def test_tipos_retorno_numericos(self):
        """Teste verificando se os retornos são numéricos"""
        tmb_homem = calcular_tmb_homem(70, 175, 30)
        tmb_mulher = calcular_tmb_mulher(60, 165, 25)
        
        self.assertIsInstance(tmb_homem, (int, float))
        self.assertIsInstance(tmb_mulher, (int, float))

if __name__ == '__main__':
    unittest.main()
