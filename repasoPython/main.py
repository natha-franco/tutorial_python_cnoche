#Tipos de datos
#Numeros enteros

numero1: int = 78 #tipado estatico
numero2 = 45 #tipado dinamico
print(numero1)
print(numero2)

#Numeros reales

numero3: float = 4.9
numero4 = 5.0
print(numero3)
print(numero4)

#Booleanos toma dos valores Verdadero o Falso

esColombiano: bool = True
esArgentino = False
print(esColombiano)
print(esArgentino)

#Caracter y Cadena de catacteres
mensaje = "Cadena con una comilla simple ', una comilla doble \" y una diagonal invertida \\"
print(mensaje)

# Operadores
# Aritmeticos
numero5 = 78
numero6 = 46
suma = numero5 + numero6
resta = numero5 - numero6
multiplicacion = numero5 * numero6
division = numero5 / numero6
modulo = numero5 % numero6
print("la suma es: ", suma)
print("la resta es: ", resta)
print("la multiplicacion es: ", multiplicacion)
print("la division es: ", division)
print("El modulo es: ", modulo)

#Asignación
x = 5
y = 7
z = 3

#Logicos
# and (y)
p = 5
q = 9
print(p < 7 and q < 9)

#or (o)
print(p < 7 or q < 9)

#not
print(not(q > 2 and p < 7))

#Relacionales
edad1 = 23
edad2 =18
print(edad1 == edad2) #Igualdad
print(edad1 > edad2) #Mayor que
print(edad1 < edad2) #Menor que
print(edad1 >= edad2) #Mayor o igual que
print(edad1 <= edad2) #Menor o igual que
print(edad1 != edad2) #No igual
