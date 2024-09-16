import os
os.system("cls || clear")
# Variáveis para armazenar as estatísticas
armazenamento = []
soma_pares = 0
soma_impares = 0
Quantidade_numeros = 5
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_geral = 0

# Variáveis para armazenar os números
for i in range(Quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º número: "))
    armazenamento.append(numero)

    soma_geral += numero

# Pares e impares
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        quantidade_positivos += 1

maior_numero = max(armazenamento)
menor_numero = min(armazenamento)

# Calculando as médias
media_geral = soma_geral / 5

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"Média de números pares: {media_pares:.2f}")
if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
    print(f"Média de números impares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")

for numero in reversed(armazenamento):
    print(f"{numero}")