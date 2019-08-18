import math
x1=int(input("ingrese la primera coordenada en X: "))
x2=int(input("ingrese la segunda coordenada en X: "))
y1=int(input("ingrese la primera coordenada en Y: "))
y2=int(input("ingrese la segunda coordenada en Y: "))
d=math.sqrt((math.pow((x2-x1),2))+(math.pow((y2-y1),2)))
print("La distancia entre dos puntos es: ",d)
