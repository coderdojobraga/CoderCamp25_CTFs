
palavra = input("Indique a palavra a alterar: ")

def alteradorDePalavra(palavra):
    resultado = ""
    for letra in palavra:
        nova_letra = chr(ord(letra) + 1)
        resultado += nova_letra
    return resultado[::-1]  # Inverte a palavra


print("🔒 Palavra alterada:", alteradorDePalavra(palavra))
