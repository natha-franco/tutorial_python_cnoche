#Estructuras selectivas y repetitivas
#While
x = 0
total=0
while x<5:
    nota=int(input("Ingrese la nota: "))
    if nota>4:
        total=total+1
    x=x+1
print("Han aprobado ",total)

#For
suma=0
for f in range(10):
    valor=int(input("Ingrese un valor: "))
    if f>4:
        suma=suma+valor
print("La suma de los últimos 5 valores es: ")
print(suma)