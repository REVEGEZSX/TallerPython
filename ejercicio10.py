diccionario={"platano":1.35, "manzana":0.80, "pera":0.85, "naranja":0.70}
f=input("ingrese el nombre de la fruta: ")
if(f in diccionario):
    p=float(input("Cantidad de kilos que desea comprar: "))
    total=p*diccionario[f]
    print("Total de la compra: ",total)
else:
    print("Esa fruta no se encuentra disponible")
