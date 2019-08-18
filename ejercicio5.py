listas=[]
cont=0
for i in range (10):
    lista=float(input("Ingrese el numero: " ))
    listas.append(lista)
    if (lista==5):
        cont=cont+1 
print(listas)
mayor= max(listas)
print ("El numero mayor de la lista es: ",mayor)
suma=sum(listas)
prom=suma/len(listas)
print("El promedio de los numeros de la lista es: ",prom)
print("Cantidad de numeros 5: ",cont)
    
