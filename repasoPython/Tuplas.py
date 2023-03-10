#Tuplas
#Crear tupla Python
tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)

#Operaciones con tuplas
#Como hemos comentado, las tuplas son tipos inmutables, lo que significa que una vez asignado su valor,
# no puede ser modificado. Si se intenta, tendremos un TypeError.
tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError

#Al igual que las listas, las tuplas también pueden ser anidadas.
tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a

#Métodos tuplas
#El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.
l = [1, 1, 1, 3, 5]
print(l.count(1)) #3

#El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.
l = [7, 7, 7, 3, 5]
print(l.index(5)) #4

#En el caso de no encontrarse, se devuelve un ValueError.
l = [7, 7, 7, 3, 5]
#print(l.index(35)) #Error! ValueError

#El método index() también acepta un segundo parámetro opcional, que indica a partir de que índice empezar a buscar el objeto.
l = [7, 7, 7, 3, 5]
print(l.index(7, 2)) #2