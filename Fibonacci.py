# This is a sample Python script.
anterior: int = 0
proximo: int = 0

while proximo < 50:
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior

  if proximo != 0:
      continue
  proximo = proximo + 1