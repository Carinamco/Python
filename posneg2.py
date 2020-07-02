#Determinar si un número es positivo, negatvo o cero
num=float(input('Escribe un número: '))
if num >= 0:
    if num == 0:
        print('cero')
    else:
        print('positivo')   
else:
    print('negativo')
