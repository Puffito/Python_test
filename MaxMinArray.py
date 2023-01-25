numeros = []
for i in range(10):
    numeros.append(int(input("Introduce un número real\n")))
numeros.sort()
print(numeros[-1])
print(numeros[0])