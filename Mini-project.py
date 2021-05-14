print("Bienvenido al restaurante Yonguei")
print("Porfavor llene nuestro registro de clientes, gracias.")

Personas=int(input("¿Cuantas personas vienen con usted el dia de hoy?(incluyase): "))
i=1
while (i<=Personas):
    print("Persona",i)
    class persona:
        def __init__(self, nombre, edad):
            self.name=nombre
            self.age=edad
            
            def person(nombre, edad):
                return self.nombre
                return self.edad
    nombre=input("Nombre: ")
    edad=int(input("Edad: "))
    todo=(nombre, edad)
    print(todo);i+=1

#LISTA DE CODIGOS QR(RESERVACIONES)
Lista=["q023X", "2aB3s", "rtt2I", "m96op"]

#RESERVACION
reserva=input("Tiene mesa reservada?(si/no): ")
if reserva=="si":
    codigoqr=input("Porfavor inserte su codigo QR para validarlo: ")
    if codigoqr in Lista:
        print("Correcto codigo QR canjeado exitosamente continue a la mesa que reservo: ")
else:
    print("Bien, siga llenando el registro porfavor.")

#DESCUENTO POR CUMPLEAÑOS(SI/NO)
cumpleaños=input("Hoy es su cumpleaños?(si/no): ")
if cumpleaños=="si":
    print("Bien se le hara un descuento del 25%  por su cumpleaños, ¡felicidades!.")
else:
    print("Bien, registro completado, continue a cualquiera de las mesas que este libre, antes verifique que no tenga un cartel de 'reservado', gracias.")

#SELECCION DE MENU
Seleccion=input("Que menu desea mirar(principal/bebidas/postres): ")
if (Seleccion=="principal"):
    print("****MENU PRINCIPAL****\n","______________________\n", "1.Arroz blanco\n", "2.Carne de cerdo\n", "3.Carne de res\n", "4.Arroz chino\n", "5.Frijoles\n", "6.Pescado frito")
    print("-----------------")
    #CUANTOS PRODUCTOS SE ORDENARAN
    Productos=int(input("¿Cuantas cosas ordenara?: "))
    a=1
    totalmp=0
    #SUMA DE CADA PRODUCTO QUE SE PIDE POR MEDIO DE UN CICLO
    while (a<=Productos):
        orden=int(input("Digite el numero del alimento que desea ordenar: "))
        if orden==1:
            totalmp=totalmp+3000
        if orden==2:
            totalmp=totalmp+10000
        if orden==3:
            totalmp=totalmp+10000
        if orden==4:
            totalmp=totalmp+6000
        if orden==5:
            totalmp=totalmp+4500
        if orden==6:
            totalmp=totalmp+7000
        a+=1
    print("El total es: ",totalmp)
elif (Seleccion=="bebidas"):
    print(" ****BEBIDAS****\n","______________________\n", "1.Cocacola\n", "2.Manzana postobon\n", "3.Colombiana\n", "4.H2o con gas\n", "5.Soda\n", "6.jugos naturales")
    print("-----------------")
    #CUANTOS PRODUCTOS SE ORDENARAN
    Productos=int(input("¿Cuantas bebidas ordenara?: "))
    a=1
    totalb=0
    #SUMA DE CADA PRODUCTO QUE SE PIDE POR MEDIO DE UN CICLO
    while (a<=Productos):
        orden=int(input("Digite el numero del alimento que desea ordenar: "))
        if orden==1:
            totalb=totalb+5000
        if orden==2:
            totalb=totalb+3000
        if orden==3:
            totalb=totalb+3000
        if orden==4:
            totalb=totalb+2500
        if orden==5:
            totalb=totalb+3500
        if orden==6:
            totalb=totalb+1500
        a+=1
    print("El total es: ",totalb)
elif (Seleccion=="postres"):
    print("****POSTRES****\n", "______________________\n","1.Pastel de chocolate\n", "2.Pastel de vainilla\n", "3.Helados artesanales\n", "4.Gelatina")
    print("-----------------")
    #CUANTOS PRODUCTOS SE ORDENARAN
    Productos=int(input("¿Cuantas bebidas ordenara?: "))
    a=1
    totalp=0
    #SUMA DE CADA PRODUCTO QUE SE PIDE POR MEDIO DE UN CICLO
    while (a<=Productos):
        orden=int(input("Digite el numero del alimento que desea ordenar: "))
        if orden==1:
            totalp=totalp+7000
        if orden==2:
            totalp=totalp+6000
        if orden==3:
            totalp=totalp+2000
        if orden==4:
            totalp=totalp+3000
        a+=1
    print("El total es: ",totalp)

cuenta=0

if cumpleaños=="no":
    cuenta=(totalmp+totalb+totalp)
    print("El total de la cuenta es: ",cuenta)

if cumpleaños=="si":
    cuenta=(totalmp+totalb+totalp)
    descuento=cuenta*0.25
    cuentafinal=cuenta-descuento

pago=int(input("Con cuanto dinero desea cancelar: "))

if cumpleaños=="no":
    devuelta=pago-cuenta

if cumpleaños=="si":
    devuelta=pago-cuentafinal
