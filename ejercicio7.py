n=int(input("Digite la cantidad de personas: "))
cont=0
for i in range(n):
    peso=float(input("Ingrese el peso de la persona "))
    esta=float(input("Ingrese la estatura de la persona "))
    imc=(peso/(esta*esta))
    cont=cont+imc
prom=cont/n
if(prom<=15):
    print(prom, "Delgadez muy severa")
    
if(prom>=15 and prom<16):
    print(prom," Delgadez severa")
    
if(prom>=16 and prom<18.5):
    print(prom," Delgadez")
          
if(prom>=18.5 and prom<25):
          print(prom," Peso saludable")

if(prom>=25 and prom<30):
          print(prom," Sobrepeso")

if(prom>=30 and prom<35):
          print(prom," Obesidad severa")

if(prom>=40):
          print(prom," Obesidad morbida")

