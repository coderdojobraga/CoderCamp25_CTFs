import segredo

def descobre_nr_secreto(segredo):
  d = segredo.distancia(0)
  a = segredo.distancia(-1)

  if (a < d):
    return -d
  else:
    return d
  
segredo.testa(descobre_nr_secreto)