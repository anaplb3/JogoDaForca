'''print("processing...")
for i in range(11):
   progress_bar(i, 10, 40)
   time.sleep(1)
print("ok")

from tqdm import tqdm
from time import sleep
for i in tqdm(range(1000)):
	sleep(0.01)'''

funcoes = [["p","r", "i", "n", "t"], ["t", "r", "y"], ["e", "x", "c", "p", "t", "i", "o", "n"], ["i", "m", "p", "o", "r", "t"], ["f", "r", "o", "m"], ["f", "o", "r"], ["r", "a", "n", "g", "e"], ["r", "e", "t", "u", "r", "n"], ["f", "o", "r", "m", "a", "t"]]
listaFuncoes = [["_","_", "_", "_", "_"], ["_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_"], ["_", "_", "_"], ["_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"]]

musica = [["j", "u", "s", "t", "i", "n", " ", "b", "i", "e", "b", "e", "r"], ["a","c", "/", "d","c"], ["t", "a", "y", "l", "o", "r", " ", "s", "w", "i", "f", "t"], ["f", "o", "s", "t", "e", "r", " ", "t", "h", "e", " ", "p", "e", "o", "p", "l", "e"], ["d","a", "v", "i", "d", " ", "g", "u", "e", "t", "t", "a"], ["a", "l", "a", "n", " ", "w", "a", "l", "k", "e", "r"], ["b", "e", "y", "o", "n", "c", "e"], ["j", "u", "s", "t", "i", "n", " ", "t", "i", "m", "b", "e", "r", "l", "a", "k", "e"], ["f", "a", "l", "c", "ã", "o"], ["b", "o", "b", " ", "m", "a", "r", "l", "e", "y"]]
listaMusica = [["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_","_", "/", "_","_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_","_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_", " ", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"], ["_", "_", "_", "_", "_", "_"], ["_", "_", "_", " ", "_", "_", "_", "_", "_", "_"]]

print("len musica: ", len(musica)-1)
print("len funcoes: ", len(funcoes)-1)
#ljust(150), end=""