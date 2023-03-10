#Diccionario
#Crear diccionario
d1 = {
  "Nombre": "Nathalia",
  "Edad": 22,
  "Documento": 1002972446
}
print(d1)

#Acceder y modificar elementos
print(d1['Nombre'])
print(d1.get('Nombre'))

#Iterar diccionario
# Imprime los key del diccionario
for x in d1:
    print(x)
#Nombre
#Edad
#Documento
#Direccion

#Diccionarios anidados
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)

#Métodos diccionarios Python
#Clear
d = {'a': 1, 'b': 2}  #El método clear() elimina todo el contenido del diccionari
d.clear()
print(d) #{}

#Items
#El método items() devuelve una lista con los keys
# y values del diccionario. Si se convierte en list se puede indexar
# como si de una lista normal se tratase, siendo los primeros elementos las key y los segundos los value.
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

#Keys El método keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 9}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

#Values El método values() devuelve una lista con todos los values o valores del diccionario.
d = {'a': 1, 'b': 8}
print(list(d.values())) #[1, 2]

#pop El método pop() busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. Daría un error
# si se intenta eliminar una key que no existe.
d = {'a': 1, 'b': 7}
d.pop('a')
print(d) #{'b': 2}

#El método popitem() elimina de manera aleatoria un elemento del diccionario.
d = {'a': 3, 'b': 2}
d.popitem()
print(d)
#{'a': 1}

#El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados
# y si alguna key del nuevo diccionario no esta, es añadida.
d1 = {'a': 1, 'b': 4}
d2 = {'a': 0, 'd': 200}
d1.update(d2)
print(d1)