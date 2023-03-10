#Listas enlazadas
# A Nodo de lista enlazada
class Node:
    def _init_(self, data=None, next=None):
        self.data = data
        self.next = next


# Función para imprimir una lista enlazada dada
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=' —> ')
        ptr = ptr.next

    print('None')


# Función para construir una lista enlazada a partir de un conjunto dado de claves
def construct(keys):
    head = None

    # empieza desde el final de la lista
    for i in reversed(range(len(keys))):
        # asigna un nuevo nodo en un heap y establece sus datos
        head = Node(keys[i], head)

    return head


if _name_ == '_main_':
    # Teclas de entrada
    keys = [1, 2, 3, 4]

    # apunta al nodo principal de la lista enlazada
    head = construct(keys)

    # Lista enlazada de impresión
    printList(head)