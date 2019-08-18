diccionario={}
motor = True
i=0
while(motor):
    palabra=input("Ingrese la palabra y su traduccion ")
    par=palabra.split(":")
    llave=par[0]
    valor=par[1]
    diccionario.update({llave:valor})
    f=input("si desea terminar dijite 0")
    if(f=="0"):
        break

print("diccionario ", diccionario)

frase=input("ingrese una frase ")
a=len(frase.split())
for i in range(a):
    fra=frase.split(" ")
    pa=fra[i]
    if pa in diccionario:
        print("Traduccion ", diccionario[pa])




