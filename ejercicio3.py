palabra=input("Ingrese una palabra: ")
c=len(palabra)
for i in range(1,c):
    if i%2==0:
        print (palabra[i])
