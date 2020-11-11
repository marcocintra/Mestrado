import numpy as np

serie = np.loadtxt("serie_A8_PModel_2025.txt", delimiter="\n")
matriz = np.resize(serie,(45,45))
print(matriz.shape)
print(matriz)
np.savetxt('serie_A8_PModel_2025-45X45.txt', matriz)


