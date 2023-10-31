"""Algoritmo para determinar si es un triangulo e indicar el tipo de triangulo que es

ladoUno = int(input("Ingrese lado uno: "))
ladoDos = int(input("Ingrese lado dos: "))
ladoTres = int(input("Ingrese lado tres: "))

if (ladoUno + ladoDos > ladoTres) and (ladoUno + ladoTres > ladoDos) and (ladoDos + ladoTres > ladoUno):
  print("Es un triangulo")
  if (ladoUno == ladoDos) and (ladoUno == ladoTres):
    print("Es un triangulo equilatero")
  elif (ladoUno == ladoDos) or (ladoUno == ladoTres) or (ladoDos == ladoTres):
    print("Es un triangulo isosceles")
  else:
    print("Es un triangulo escaleno")
else:
  print("No es un triangulo")"""


"""Leer si un numero entero y determinar si es mayor o menor o es igual

numero = int(input("Ingrese un numero: "))

if numero > 0:
  print("El numero es mayor a cero")
elif numero < 0:
  print("El numero es menor a cero")
else:
  print("El numero es igual a cero")
"""

#Leer tres numeros y determinar el promedio, el numero mayor (si existe) y el numero menor (si existe)
#Ivan Sierra

numeroUno = float(input("Ingrese el primer numero: "))
numeroDos = float(input("Ingrese el segundo numero: "))
numeroTres = float(input("Ingrese el tercer numero: "))

promedio = (numeroUno + numeroDos + numeroTres) / 3
print("El promedio de los numeros es: ", promedio)

if numeroUno > numeroDos and numeroUno > numeroTres:
  print("El numero mayor es: ", numeroUno)
elif numeroDos > numeroUno and numeroDos > numeroTres:
  print("El numero mayor es: ", numeroDos)
elif numeroTres > numeroUno and numeroTres > numeroDos:
  print("El numero mayor es: ", numeroTres)
else:
  print("Hay numeros mayores que son iguales")
  
if numeroUno < numeroDos and numeroUno < numeroTres:
  print("El numero menor es: ", numeroUno)
elif numeroDos < numeroUno and numeroDos < numeroTres:
  print("El numero menor es: ", numeroDos) 
elif numeroTres < numeroUno and numeroTres < numeroDos:
  print("El numero menor es: ", numeroTres)
else:
  print("Hay numeros menores que son iguales")