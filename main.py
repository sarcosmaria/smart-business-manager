titulo = "Smart Business Manager"
print (titulo)

menu_principal = ("Registrar clientes", "Listar clientes", "Actualizar Cliente", "salir")
while True:
    for  numero, texto in (enumerate(menu_principal, start=1)):
        print (f"{numero}. {texto}")

    opcion = input("Selecciona una opcion: ") 

    if opcion == "1":
        print("Registrar clientes")
    elif opcion == "2":
        print("Listar clientes")
    elif opcion == "3":
        print("Actualizar cliente")
    elif opcion == "4":
        print("salir")
        break
    else:
        print("opcion no valida")


