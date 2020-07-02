#Área del Triángulo
import cmath
a=float(input('un lado es: '))
b=float(input('otro lado es: '))
c=float(input('otro lado es: '))
s=(a+b+c)/2
area=cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print('El área es:')
print(area)
