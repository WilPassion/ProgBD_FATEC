class Funcionario():
    def __init__(self, nome, salario):
        self.__nome = nome #Encapsulamento do nome como um atributo privado
        self.__salario = salario #Encapsulamento do nome como um atributo privado

    def obterNome(self):
        return self.__nome #Encapsulamento do nome: acessado apenas através de um método
    
    def obterSalario(self):
        return self.__salario
    
    def aplicarAumento(self, percentual):
        if percentual > 0:
            aumento = self.__salario * percentual / 100
            self.__salario = aumento
            print("Aumento de {}".format(percentual)) #Encapsulamento do salário: acessado/modificado apenas dentro da classe
        else:
            print("Percentual inválido")

#Teste da ckasse
funcionario1 = Funcionario("João", 3000)
print("Nome", funcionario1.obterNome())
print("Salário:", funcionario1.obterSalario())
funcionario1.aplicarAumento(20)
print("Salário reajustado: {}".format(funcionario1.obterSalario()))