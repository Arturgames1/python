import os
n_archivo= input("Ingresa el nombre del archivo")

file = open(n_archivo, "w")

file.write("<html> Todos los demás elementos del sitio van aquí. </html>")
file.close()

file = open(n_archivo, "r")
print(file.read())


