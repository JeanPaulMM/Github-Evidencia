class manzana:
    def __init__(self,casa,color,pisos):
        self.Numerocasa=casa
        self.colorcasa=color
        self.pisoscasa=pisos
        
        def conjunto():
            return self.casa
            return self.color
            return self.pisos
        
casa=input("proporcione el numero de la casa: ")
color=input("proporcione el color de la casa: ")
pisos=input("Cuantos pisos tiene la casa: ")

print ("El n° de la casa es: ",casa,", El color de la casa es: ",color,", Los pisos que tiene la casa son: ",pisos)

casa1=manzana("62","amarillo", "3" )