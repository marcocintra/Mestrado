# -*- coding: utf-8 -*-

import numpy as np
import subprocess

matriz = np.loadtxt('serie_BLEN7M_20110730_054503_25_canal_167_2025-45X45.txt')
tamanhomatriz = np.shape(matriz)
print(tamanhomatriz)

arraydematrizesshort = list(matriz.reshape(-1, 45, 45))
################################################
################################################
# MATRIZ QUADRADA PARA 3600 PONTOS É 60, 60 (-1, 60, 60)
################################################
################################################
print(len(arraydematrizesshort))
arraydematrizes = list(arraydematrizesshort[0].reshape(-1, 45, 45))

print(np.size(arraydematrizes[0]))
print(np.shape(arraydematrizes[0]))

cont = 0
ga = np.zeros((len(arraydematrizes)), dtype=np.float)
# número de GAs = número de matrizes analisadas
media = np.zeros(1, dtype=np.float)
desviopadrao = np.zeros(1, dtype=np.float)

while (cont < len(arraydematrizes)):
    np.savetxt('minimatriz' + str(cont) + '.txt', arraydematrizes[cont])
    p = subprocess.check_output(["python", "main.py", 'minimatriz' + str(cont) + '.txt', "0.02", "0.01", "1"])
    print(p.decode('ascii'))
    ga[cont] = p.decode('ascii').split()[10]
    cont = cont + 1

media[0] = np.mean(ga)
desviopadrao[0] = np.std(ga)

print("Média: " + str(media[0]))
print("Desvio Padrão: " + str(desviopadrao[0]))

np.savetxt('GA-serie_BLEN7M_20110730_054503_25_canal_167_2025-45X45.txt', ga)
np.savetxt('MEDIA-serie_BLEN7M_20110730_054503_25_canal_167_2025-45X45.txt', media)
np.savetxt('DESVIO-serie_BLEN7M_20110730_054503_25_canal_167_2025-45X45.txt', desviopadrao)
