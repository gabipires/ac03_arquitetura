from unittest import TestCase, main
from calculadora import Calculadora

class Testes(TestCase):

    def teste_soma(self):
        calculadora1 = Calculadora()
        resultado = calculadora1.calcular(2,2,'+')
        print("Resultado teste soma: ", resultado)
        self.assertEqual(resultado, 4)


    def teste_subtracao(self):
        calculadora2 = Calculadora()
        resultado = calculadora2.calcular(5,2,'-')
        print("Resultado teste subtração: ", resultado)
        self.assertEqual(resultado, 3)


    def teste_divisao(self):
        calculadora3 = Calculadora()
        resultado = calculadora3.calcular(10,2,'/')
        print("Resultado teste divisão: ", resultado)
        self.assertEqual(resultado, 5)


    def teste_multiplicacao(self):
        calculadora4 = Calculadora()
        resultado = calculadora4.calcular(5,5,'*')
        print("Resultado teste multiplicação: ", resultado)
        self.assertEqual(resultado, 25)

if __name__ == '__main__':
    main()