#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.


def contar(string):
    string_lower = string.lower()
    contagem = string_lower.count('a')
    return contagem

texto = input("Digite uma string: ")
quantidade = contar(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
