# Solução 2
class Quadrado():
    def __init__(self, lado):
        self.setLado(lado)

    def setLado(self, lado):
        self.lado = lado

    def getLado(self):
        return self.lado
    
    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado * 4
    
q1 = Quadrado(5)
print(q1.area())
print(q1.perimetro())    

''' Solução1

class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

q1 = Quadrado(5)

print("Área do quadrado:", q1.area())
print("Perímetro do quadrado:", q1.perimetro())


#print("Área do quadrado:", q1.area())
#print("Perímetro do quadrado:", q1.perimetro())
'''