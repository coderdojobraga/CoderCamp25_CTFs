import string

def decripta_cesar(encriptado, deslocamento):
    resultado = []
    for ch in encriptado:
        if ch.islower():
            idx = (ord(ch) - ord('a') - deslocamento) % 26
            resultado.append(chr(ord('a') + idx))
        elif ch.isupper():
            idx = (ord(ch) - ord('A') - deslocamento) % 26
            resultado.append(chr(ord('A') + idx))
        else:
            resultado.append(ch)
    return ''.join(resultado)

def decripta_atbash(encriptado):
    """Decifra um texto usando a cifra de Atbash."""
    resultado = []
    for ch in encriptado:
        if ch.islower():
            idx = ord(ch) - ord('a')
            resultado.append(chr(ord('a') + (25 - idx)))
        elif ch.isupper():
            idx = ord(ch) - ord('A')
            resultado.append(chr(ord('A') + (25 - idx)))
        else:
            resultado.append(ch)
    return ''.join(resultado)

def main(encriptado):
    for i in range(26):
        atbash_then_cesar = decripta_cesar(decripta_atbash(encriptado), i)
        print(f"Atbash → César -{i}: {atbash_then_cesar}")
        cesar_depois_atbash = decripta_atbash(decripta_cesar(encriptado, i))
        print(f"César -{i} → Atbash: {cesar_depois_atbash}")


encriptado = "BA25{bzldm-4-z-azopvl-dkcdlw}"
main(encriptado)
