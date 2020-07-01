#raices
import cmath
num=float(input('escribe el número '))
num_sqrt=cmath.sqrt(num)
print('la raíz de {0} es: {1}. parte entera: {2} Parte imaginaria: {3}'.format(num, num_sqrt,num_sqrt.real,num_sqrt.imag))
