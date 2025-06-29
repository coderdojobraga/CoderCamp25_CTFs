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

def desencriptar(texto):
    x = []
    for c in texto:
        j = ord(c)
        if 33 <= j <= 126:
            d = ((j - 33 + 14) % 94) + 33
            x.append(chr(d))
        else:
            x.append(c)
    print(''.join(x))