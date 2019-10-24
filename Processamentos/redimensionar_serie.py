import numpy as np

serie = np.loadtxt("serie.txt", delimiter="\n")

serie = np.resize(serie, (3600,))

np.savetxt('serie_2048.txt', serie)
