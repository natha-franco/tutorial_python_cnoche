#Listas con operaciones
#adjuntar
notas = [0, 0, 8.0, 1.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 9.0, 7.5]
suma_de_notas = sum(notas)
print(suma_de_notas)

#La función built-in len () devuelve la longitud
notas = [0, 0, 9.0, 3.0, 4.0, 10.0, 7.0, 7.5, 5.0, 10.0, 5.0, 7.0, 5.0, 6.0, 7.5]
cantidad_notas = len(notas)
print(cantidad_notas)

#Python nos trae el método remove(), que toma como parámetro el valor que queremos eliminar de nuestra lista.
notas = [0, 0, 7.0, 9.0, 6.0, 10.0, 7.0, 7.5, 4.0, 9.0, 7.0, 7.0, 6.0, 8.0, 7.5]
notas.remove(9.0)
print(notas)

#Contar elementos en una lista con el método count()
cantidad_sietes = notas.count(8.0)
print (cantidad_sietes)