def escolhe_maior():
    numero1 = input("Qual o primeiro número? ")
    numero2 = input("Qual o segundo número? ")
    
    maior = numero1

    if numero1 < numero2:
        maior = numero2

    print( "O maior número é: " + str(maior) )

def encriptar(texto):
    x = []
    for c in texto:
        j = ord(c)
        if 33 <= j <= 126:
            e = ((j - 33 - 14) % 94) + 33
            x.append(chr(e))
        else:
            x.append(c)
    print(''.join(x))

def retorna_flag():
    flag = "56$'mfdaUSdQSQXg`USaQWjWUgfSVSo"
    x = []
    for c in flag:
        j = ord(c)
        if 33 <= j <= 126:
            d = ((j - 33 + 14) % 94) + 33
            x.append(chr(d))
        else:
            x.append(c)
    print(''.join(x))

escolhe_maior()