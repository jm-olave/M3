# condicionales
a = 8
b = 10
c = 13
if a >=c:
    print("entra a if")
elif (a<=c or c == b) and ( b>c):
    print("entra al elif")
else:
    print("entra al else")

# IMC calculadora
peso = int(input("peso del paciente:"))
altura = float(input("altura del paciente:"))
imc = peso/(altura**2)

if imc < 18.5:
    print("Se encuentra con muy bajo peso")
elif imc >=19 and imc <=24.9:
    print("Se encuentra en un peso normal")
elif imc >= 25 and imc<=29.9:
    print("Se encuentra en sobrepeso")
elif imc > 30:
    print("se encuentra en obesidad")
print(f'imc es{imc}')