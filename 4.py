inversion=int(input("¿Cuanto desea invertir?: "))
interes=int(input("¿Cual sera el interes anual?: "))
Tiempo=int(input("¿Por cuantos años lo hara: "))

Total=inversion+(interes*Tiempo)
TotalA=interes*Tiempo

print("El capital obtenido en la inversion de todos los años es:")
print(Total)
print("Y el capital obtenido por año (individualmente) es:")
print(TotalA)