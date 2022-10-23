# leer nombre de invitados y agregarlos a una lista si han trido regalo
# tener la oipcion de detener la adicion de invitados
# imprimir invitados que llevaron regalo

#Creamos 2 listas vacias
invitados = []
no_invitado = []

#Preguntamos al usuario cuantos invitados van a la fiesta de Splatero
cantidad = int(input("Cuantos invitados desea invitar señor Splatero: "))

#Greneramos un cilo para que se repitan las preguntas mientras la cantidad sea mayor que 0
while cantidad > 0:
    #Pedimos que indique si trajo o no regalo
    lista = input("Chico trajo usted regalo? \n1) Si \n2) No \n")
    #Pedimos el dato
    dato = input("Ingrese nombre del regalo: ")
    #Comprobamos la decision del usuario para saber en que lista se guardara el dato
    if lista == 'Si':
        invitados.append(str(dato))
    else:
        no_invitado.append(str(dato))
        #no_invitado.append(str(dato)) no lo mostramos porque
        # en realidad no nos piden agregarlo a la lista pero lo deje como una opcion por si se necesita o para que se entienda mejor

    #Quitamos de a uno en uno los intentos de el valor inicial que l usuario indico para poder detener el ciclo
    cantidad-=1
#Finalmente imprimimos los regalos de los invitados
print("Invitados Con Regalo: ", len(invitados), "\n Regalos de los invitados : " , invitados)
