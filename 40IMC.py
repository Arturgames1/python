'''calcula el imc e interpretalo'''

peso = int(input("ingresa tu peso"))
altura = int(input("ingresa tu altura en m"))

imc= peso/pow(altura,2)
print(imc)
if imc < 18.5:
    print("tienes peso bajo")
elif(imc < 25):
    print("tienes peso normal")
    