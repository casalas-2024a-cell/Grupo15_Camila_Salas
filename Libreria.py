import random
print(random.random())

print(random.randint(5,25))

a=(random.randint(0,100))
b=int(input("Ingrese un numero entre 0 y 100:"))
print("El numero", a, "es mayor al numero", b,"", a>b)

import math

print(math.ceil(5.896))
print(math.floor(2.896))
print(math.sqrt(100))
print(math.pow(5,5))

####Operación con String
a= "Camila"
print(a[2])
print(a[5])
print(len(a))

a= "Julian"
print(a[1:4])
print(a[1:])
print(a[:4])
print(a[:])
print(a[-3])
print(a[-4:-1])