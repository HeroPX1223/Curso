enunciado = "Itera una lista y di si cada número es par o impar"
print(enunciado)
lista = [10, 7, 23, 50]

for numero in lista:
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    print(numero % 2)