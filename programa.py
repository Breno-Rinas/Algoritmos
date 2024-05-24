numero = int(input("Digite um número inteiro: "))
sucessores = int(input("Digite quantos sucessores deseja somar: "))
n = 1
numero2 = 0
while n <= sucessores:
    numero += 1
    numero2 += numero
    n += 1
print(f"A soma dos {sucessores} sucessores do número digitado é: {numero2}")