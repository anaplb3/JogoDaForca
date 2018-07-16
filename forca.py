#!/usr/bin/env python3
from random import *
from bibForca import *
import time

apresentacao()
print("\n")
escolha = informacoes()

print("\n")
print("Gerando palavras...")
for i in range(11):
   progress_bar(i, 10, 40)
   time.sleep(1)

jogo(escolha)


