'''
determina si un año es viciesto con la regla de negocios 4 400 
'''
año = 2023

if(año % 4 ==0 and año%100 !=0 ) or \
(año % 400==0):
    print("el año es biciesto")
else:
    print("no es biciesto")