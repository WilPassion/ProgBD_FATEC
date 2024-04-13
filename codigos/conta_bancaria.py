class ContaBancaria():
    def __init__(self):
        self.__saldo = 0 #Encapsulamento do saldo como um atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  #Encapsulamento do saldo: acessado/modificado apenas dentro da classe
            print("Depósito de", valor, "realizado com sucesso.")
        else:
           print("Valor inválido para depósito")     

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo: #valor 100 | saldo 200
            self.__saldo -= valor #Encapsulamento do saldo: acessado/modificado apenas dentro da classe
            print("Total Saque", valor)

    def obter_saldo(self):
        return self.__saldo #Encapsulamento do saldo: acessado apenas através de um método

usuario = ContaBancaria()
usuario.depositar(1000)
print("Saldo: ", usuario.obter_saldo())
usuario.sacar(50)
print("Saldo: ", usuario.obter_saldo())
usuario.sacar(20)
print("Saldo: ", usuario.obter_saldo())

'''
Encapsulamento é um dos princípios fundamentais da programação orientada a objetos (POO) e refere-se à 
técnica de esconder os detalhes internos de uma classe e fornecer uma interface clara e controlada para 
interagir com esses detalhes.***

Existem três níveis de encapsulamento em uma classe:

* Atributos privados: São os atributos que só podem ser acessados e modificados dentro da própria classe***. 
Em Python, isso é frequentemente alcançado prefixando o nome do atributo com dois underscores (__). Isso 
impede que o atributo seja acessado diretamente de fora da classe, garantindo um maior controle sobre seus valores.

* Métodos públicos: São os métodos que são acessíveis de fora da classe e fornecem uma interface para interagir
 com os objetos da classe. Esses métodos podem acessar e modificar os atributos privados da classe de maneira 
 controlada*, aplicando validações ou lógica adicional, se necessário.

* Métodos privados: São os métodos que só podem ser chamados de dentro da própria classe.*** Em Python, isso é 
alcançado prefixando o nome do método com um underscore (_). Esses métodos s*ão úteis para encapsular funcionalidades
 internas da classe que não precisam ser expostas diretamente para os usuários da classe.
'''