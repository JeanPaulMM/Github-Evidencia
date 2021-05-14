Seleccion=input("Que menu desea mirar(principal/bebidas/postres): ")
if (Seleccion=="principal"):
    print("****MENU PRINCIPAL****\n","______________________\n", "1.Arroz blanco\n", "2.Carne de cerdo\n", "3.Carne de res\n", "4.Arroz chino\n", "5.Frijoles\n", "6.Pescado frito")
    print("-----------------")
    Productos=int(input("¿Cuantas cosas ordenara?: "))
    a=1
    total=0
    while (a<=Productos):
        orden=int(input("Digite el numero del alimento que desea ordenar: "))
        if orden==1:
            total=total+1500
        if orden==2:
            total=total+3000
        if orden==3:
            total=total+3000
        a+=1
    print("El total es: ",total)
elif (Seleccion=="bebidas"):
    print(" ****BEBIDAS****\n","______________________\n", "1.Cocacola\n", "2.Manzana postobon\n", "3.Colombiana\n", "4.H2o con gas\n", "5.Soda\n", "6.jugos naturales")
    print("-----------------")
elif (Seleccion=="postres"):
    print("****POSTRES****\n", "______________________\n","1.Pastel de chocolate\n", "2.Pastel de vainilla\n", "3.Helados artesanales\n", "4.Gelatina")
    print("-----------------")