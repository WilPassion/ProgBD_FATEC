class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Amanda", 22, 60, 170)

# Chamando os métodos da instância pessoa1
print(vars(pessoa1))
pessoa1.envelhecer(1)
print(vars(pessoa1))
pessoa1.engordar(5)
print(vars(pessoa1))
pessoa1.emagrecer(10)
print(vars(pessoa1))
pessoa1.crescer(3)
print(vars(pessoa1))