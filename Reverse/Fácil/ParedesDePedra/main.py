import codec

labirinto = ["caminho", "caminho", "parede", "caminho", "caminho", "parede"]

contador = 0

for passo in labirinto:
    if passo == "caminho":
        contador += 1
    else:
        print("Bateu numa parede! Tente de novo.")
        exit()

if contador == 6:
    codec.desencriptar("56$'m^ST[d[`fae}W}bSdWVWeo")