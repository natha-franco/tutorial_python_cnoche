#FUNCIONES

def miFuncion():
    print("Hola mundo")


miFuncion()

def mostrarNombre(nombre, apellido):
    print("Su nombre es: " +nombre + " " +apellido)



mostrarNombre("Nathalia", "Franco") #Invocar la funcion


#Datos entrada
base = 9
altura = 12

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#Salida
resultado = calcularAreaTriangulo(base,altura)
print("El area del triangulo es:", resultado)



#Datos entrada de forma manual
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

#Proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area

#Salida
resultado = calcularAreaTriangulo(base,altura)
print("El area del triangulo es:", resultado)


def mostrarMensaje(pais="Colombia"):
    print("Yo soy: "+pais)


mostrarMensaje("Suiza")
mostrarMensaje("Ecuador")
mostrarMensaje()
mostrarMensaje("Bolivia")