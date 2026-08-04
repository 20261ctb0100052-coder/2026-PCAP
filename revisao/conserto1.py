# conserto 1: trecho do "AAdivinha o Numero" (Aula 16)
import random
print("=== ADIVINHE O NUMERO ===")
segredo = random.randint(1, 10)
palpite = int(input("digite um número de 1 a 10: "))
if palpite