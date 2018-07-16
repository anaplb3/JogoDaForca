from random import *
import sys
import time




def informacoes():
	lista = ["Bem vindo ao jogo da forca!", "Você tem cinco opções de tema: Frutas, Cores, Séries, Funções do Python e Cantores/Bandas ", "Digite 1 para frutas, 2 para cores, 3 para séries, 4 para funções e 5 para cantores/bandas "]
	for i in lista:
		print(i.center(150))
		time.sleep(1)
	escolha = int(input("Sua escolha: ".rjust(190)))
	return escolha

def jogo(escolha):
	if escolha == 1:
		listaFrutas = [["_","_","_","_","_","_"], ["_", "_", "_", "_"], ["_","_","_","_","_","_","_"], ["_","_","_","_","_","_","_"], ["_","_","_","_","_","_","_"], ["_","_","_","_","_"], ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_"]]
		frutas = [["b", "a", "n", "a", "n", "a"], ["m", "a", "ç", "ã"], ["m", "o", "r", "a", "n", "g", "o"], ["l", "a", "r", "a","n", "j", "a"],["a", "c", "e", "r", "o", "l", "a"], ["l", "i", "m", "ã", "o"], ["m", "e", "x", "e", "r", "i", "c", "a"], ["m", "a", "m", "ã", "o"]]
		print("Você escolheu frutas!".center(150))
		indice = randint(0, len(frutas)-1)
		forca(listaFrutas, frutas, indice)
	elif escolha == 2:
		cores = [["a", "z", "u", "l"], ["r", "o", "s", "a"], ["r", "o", "x", "o"], ["v", "e", "r", "d", "e"], ["v", "i", "o", "l", "e", "t", "a"], ["a", "m", "a", "r", "e", "l", "o"], ["v", "e", "r", "m", "e", "l", "h", "o"]]
		listaCores = [["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"]]
		print("Você escolheu cores!".center(150))
		indice = randint(0, len(cores)-1)
		forca(listaCores, cores, indice)
	elif escolha == 3:
		series = [["f","l","a","s","h"], ["r", "i", "c", "k", " ", "e", " ", "m", "o", "r", "t", "y"], ["b", "o", "j", "a", "c", "k", " ", "h", "o", "r", "s", "e", "m", "a", "n"], ["m", "r", " ", "r", "o", "b", "o", "t"], ["g", "a", "m", "e", " ", "o", "f", " ", "t", "h", "r", "o", "n", "e", "s"], ["v", "i", "k", "i", "n", "g", "s"], ["f", "r", "i", "e", "n", "d", "s"], ["h", "o", "w", " ", "i", " ", "m", "e", "t", " ", "y", "o", "u", "r", " ", "m", "o", "t", "h", "e", "r"]]
		listaSeries = [["_","_","_","_","_"], ["_", "_", "_", "_", " ", "_", " ", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", " ", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", " ", "_", "_", " ", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", " ", "_", " ", "_", "_", "_", " ", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"]]
		print("Você escolheu séries!".format(150))
		indice = randint(0, len(series)-1)
		forca(listaSeries, series, indice)
	elif escolha == 4:
		funcoes = [["p","r", "i", "n", "t"], ["t", "r", "y"], ["e", "x", "c", "e","p", "t", "i", "o", "n"], ["i", "m", "p", "o", "r", "t"], ["f", "r", "o", "m"], ["f", "o", "r"], ["r", "a", "n", "g", "e"], ["r", "e", "t", "u", "r", "n"], ["f", "o", "r", "m", "a", "t"]]
		listaFuncoes = [["_","_", "_", "_", "_"], ["_", "_", "_"], ["_", "_", "_", "_","_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"]]
		print("Você escolheu funções de python!".format(150))
		indice = randint(0, len(funcoes)-1)
		forca(listaFuncoes, funcoes, indice)
	elif escolha == 5:
		musica = [["j", "u", "s", "t", "i", "n", " ", "b", "i", "e", "b", "e", "r"], ["a","c", "/", "d","c"], ["t", "a", "y", "l", "o", "r", " ", "s", "w", "i", "f", "t"], ["f", "o", "s", "t", "e", "r", " ", "t", "h", "e", " ", "p", "e", "o", "p", "l", "e"], ["d","a", "v", "i", "d", " ", "g", "u", "e", "t", "t", "a"], ["a", "l", "a", "n", " ", "w", "a", "l", "k", "e", "r"], ["b", "e", "y", "o", "n", "c", "e"], ["j", "u", "s", "t", "i", "n", " ", "t", "i", "m", "b", "e", "r", "l", "a", "k", "e"], ["f", "a", "l", "c", "ã", "o"], ["b", "o", "b", " ", "m", "a", "r", "l", "e", "y"]]
		listaMusica = [["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_","_", "/", "_","_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_","_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", " ", "_", "_", "_", "_", "_", "_"]]
		print("Você escolheu cantores/bandas!".format(150))
		indice = randint(0, len(musica)-1)
		forca(listaMusica, musica, indice)
	else: 
		print("Opa, escolha inválida")
		escolha = int(input("Sua escolha: ".rjust(190)))
		jogo(escolha)



def forca(lista, palavra, indice):
	erroDef = 0
	certa = 0
	teste = False
	for i in lista[indice]:
		print("",i, end="")
	print("\n")

	while lista[indice] != palavra[indice]:
		chute = input("Seu chute: ")
		word = transformando(palavra, indice)
		x = word.find(chute)
		if x < 0:
			erroDef += 1
			teste = boneco(erroDef, word)
			if erroDef == 6:
				break
			else:
				for ind, value in enumerate(word):
					if value == chute:
						lista[indice][ind] = palavra[indice][ind]
			
			print("\n")
			for i in lista[indice]:
				print("",i, end="")
			
			print("\n")
	print("Parabéns, você ganhou!")
	print("\n")

		


def apresentacao():
	lista = ["|--------", "|       |", "|      ", "|      JOGO DA FORCA", "|        ", "|        "]
	for i in lista:
		print(i)
		time.sleep(1)


def boneco(erro, word):
	perdeu ='\033[34m'+'Iiiiiiiih, você perdeu! Hahahahaha'+'\033[0;0m'
	word = '\033[34m'+'A palavra era {}!'.format(word)+'\033[0;0m'
	if erro == 0:
		print("|--------")
		print("|       |")
		print("|      ")
		print("|      ")
		print("|        ")
		print("|        ")
		print("\n")
	
	elif erro == 1:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      ")
		print("|       ")
		print("|       ")
		print("\n")
	
	elif erro == 2:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      /")
		print("|        ")
		print("|        ")
		print("\n")
	
	elif erro == 3:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      / \ ")
		print("|        ")
		print("|        ")
		print("\n")

	elif erro == 4:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      / \ ")
		print("|       | ")
		print("|        ")
		print("\n")

	elif erro == 5:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      / \ ")
		print("|       | ")
		print("|      / ")
		print("\n")

	elif erro == 6:
		print("|--------")
		print("|       |")
		print("|       0")
		print("|      / \         {}".format(perdeu))
		print("|       |          {}".format(word))
		print("|      / \ ")
		print("\n")

def transformando(palavra, indice):
	word = ""
	for i in palavra[indice]:
		word += i
	return word

def progress_bar(value, max, barsize):
   chars = int(value * barsize / float(max))
   percent = int((value / float(max)) * 100)
   sys.stdout.write("#" * chars)
   sys.stdout.write(" " * (barsize - chars + 2))
   if value >= max:
      sys.stdout.write("Pronto! \n\n")
   else:
      sys.stdout.write("[%3i%%]\r" % (percent))
      sys.stdout.flush()