'''
pide un caracter al usuario y determina si es una vocal
'''
caracter = input ("ingresa un caracter")
vocales = ['a','e','i','o','u']

if caracter.lower() in vocales:
    print("es una vocal")
else:
    print("no es una vocal")