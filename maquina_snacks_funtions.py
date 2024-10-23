from numpy import double

lista_productos=({'id':0,'nombre':'Sandwich','precio':120},
                {'id':1,'nombre':'papas','precio':300},
                {'id':2,'nombre':'refresco','precio':50})
#print(f''' lista productos : {lista_productos}''')
def mostrar_ticket(ticket):
    total=double(0)
    if len(ticket)>0:
        for producto in ticket:
            print(f" - {producto.get('nombre')} - ${producto.get('precio')}")
            total=total+double(producto.get('precio'))
    print(f'Total -> {total}')
def obtener_producto(id):
    for producto in lista_productos:
        if(str(producto.get('id'))==str(id)):
            return producto
def comprar_snack():
    producto_escogido=input('Que snacks quieres (id)? :')
    print(f'Ok, snacks agregado: {obtener_producto(producto_escogido)}')
    return obtener_producto(producto_escogido)
def mostrar_menu():
    print(f''' 
Snacks disponibles:''')
    for contador, producto in enumerate(lista_productos):
        print(f'''Id: {producto.get('id')} -> {producto.get('nombre')} - precio: {producto.get('precio')}''')
    print(f''' 
    Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Salir''')
    opcion=input('Escoja una opción: ')
    return opcion

