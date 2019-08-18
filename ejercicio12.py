class Cliente():
    def  __init__(self):
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
        Clien = Cliente()
        Clien.Nombre =input("Ingrese el Nombre : ")
        Clien.Direccion=input("Ingrese la Direccion : ")
        Clien.Telefono=input("Ingrese el Telefono : ")
        Clien.Correo=input("Ingrese el Correo : ")
        Clien.Preferente=bool(input("Preferencial : "))
        print("")
        cliente = {'Nombre' : Clien.Nombre , 'Direccion' : Clien.Direccion , 'Telefono': Clien.Telefono, 'Correo': Clien.Correo, 'Preferente':  Clien.Preferente }
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        for key in cliente:
            print (key,':', cliente[key])
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
