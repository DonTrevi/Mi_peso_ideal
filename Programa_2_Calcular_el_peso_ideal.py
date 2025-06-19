#Calcular el peso ideal
print("Este programa determina su peso ideal y le dice si está saludable o no")
print("Ingrese su peso actual ")
peso_actual = int(input())
print("Ingrese su altura actual ")
altura = float(input())
imc = peso_actual/(altura**2)
print("Su IMC es de... ")
print(imc)

if imc < 18.5:
	print("Su peso está bajo...")
if imc < 24.9 and imc > 18.5:
	print("Su peso es normal...")
if imc < 29.9 and imc > 25.0:
	print("Está en sobrepeso...")
if imc > 30:
	print("Usted sufre de obesidad...")
