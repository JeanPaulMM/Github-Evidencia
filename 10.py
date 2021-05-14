class persona:
    def __init__(self, nombre, edad, color, cc):
        this.nombre=nombre
        this.edad=edad
        this.colorpiel=color
        this.identificacion=cc
        
        def informacion(this):
            print("Nombre: ", this.nombre)
            print("Edad: ",this.edad)
            print("Color de piel: ", this.color)
            print("Identificacion: ", this.cc)
            
nombre=input("Escriba su nombre: ")
edad=input("Digite su Edad: ")
color=input("Color de piel(clara, morena, oscura): ")
cc=input("Identificacion: ")

