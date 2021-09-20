import abc
from unittest import main

def main():
    pass

class Calculadora (object):
    def calcular(self, v1, v2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar(v1, v2)
            return resultado

class OperacaoFabrica(object):
    def criar(self, operador):
        if(operador == '+'):
            return Soma()
        elif (operador == '-'):
            return Subtracao()
        elif (operador == '/'):
            return Divisao()
        elif (operador == '*'):
            return Multiplicacao()

class Operacao(metaclass=abc.ABCMeta):
    abc.abstractmethod
    def executar(self, v1, v2):
        pass

class Soma(Operacao):
    def executar(self, v1, v2):
        resultado = v1 + v2
        return resultado

class Subtracao(Operacao):
    def executar(self, v1, v2):
        resultado = v1 - v2
        return resultado


class Divisao(Operacao):
    def executar(self, v1, v2):
        resultado = v1 / v2
        return resultado

class Multiplicacao(Operacao):
    def executar(self, v1, v2):
        resultado = v1 * v2
        return resultado


calculador = Calculadora()
x = calculador.calcular(3, 2, '+')
print("Soma: ", x)

y = calculador.calcular(3, 2,  '-')
print("Subtração: ", y)

z = calculador.calcular(3, 2,  '/')
print("Divisão: ", z)

w = calculador.calcular(3, 2,  '*')
print("Multiplicação: ", w)

if __name__ == '__main__':
    main()