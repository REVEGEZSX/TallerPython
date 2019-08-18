class Cliente():
    def  __init__(self):
        self.id=""
        self.Nombre=""
        self.Direccion=""
        self.Telefono=""
        self.Correo=""
        self.Preferente=""

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Eliga una opcion: "))
            print("")
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

salir = False
opcion = 0
interno = 0
cliente = {}
while not salir:
 
    print ("1. Añadir Cliente")
    print ("2. Eliminar Cliente")
    print ("3. Mostrar Cliente")
    print ("4. Listado todos los Clientes")
    print ("5. Lista clientes preferenciales")
    print ("6. Terminar")
 
    opcion = pedirNumeroEntero()

    if opcion == 1:
        IC = Cliente()
        IC.id = input("Ingrese un id recuerde que: ", interno, " fue el ultimo")
        IC.Nombre =input("Ingrese el Nombre : ")
        IC.Direccion=input("Ingrese la Direccion : ")
        IC.Telefono=input("Ingrese el Telefono : ")
        IC.Correo=input("Ingrese el Correo : ")
        IC.Preferente=bool(input("Preferencial : "))
        interno=interno+1
        dCliente = {IC.id['Nombre' : IC.Nombre , 'Direccion' : IC.Direccion , 'Telefono': IC.Telefono, 'Correo': IC.Correo, 'Preferente':  IC.Preferente]}
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print (dCliente)
        print("")   
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        print("Opcion 5")
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 6")
 
print ("Fin")