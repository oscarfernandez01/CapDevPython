# un comando, una palabra reservada , imprime
print("Permite manejar outputs")

# Ejemplo de variables en python int,float,string
name_completed = "Oscar Fernandez"
age_now = 30
temperatura_f = 230.432

print(type(name_completed))
print(type(age_now))
print(type(temperatura_f))

validate_number = input("Introduce un numero")
print(type(validate_number))

if int(validate_number) >= 20:
    print("Verdadero")
elif int(validate_number) <20:
    print("Segundo Verdadero")
else:
    print("Falso")



name_completed = "Oscar Fernandez"

for numero in range(1,10,2):
    print(numero)

contador = 0
while contador<=10:
    print(contador)
    contador += 1
