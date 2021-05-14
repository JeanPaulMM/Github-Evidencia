class Triangulo:
    def __init__(self, altura, base):
        self.base=base
        self.altura=altura
        
        def calcular_area(self):
            return self.base*self.altura
        
base=int(input("Digite la base: "))
altura=int(input("Digite la altura: "))

triangulo=Triangulo(3,6)
print(triangulo.calcular_area())