from maquina_snacks_funtions import *

ticket = []
#comprar_snack()
#print (ticket)
opcion = mostrar_menu()

while opcion != '3':
    if opcion == '1':
        ticket.append(comprar_snack())
        opcion = mostrar_menu()
    elif opcion == '2':
        mostrar_ticket(ticket)
        opcion = mostrar_menu()
    else:
        opcion = mostrar_menu()
