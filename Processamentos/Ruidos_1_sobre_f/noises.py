import colorednoise
import numpy as np

x = colorednoise.powerlaw_psd_gaussian(2, 8192, fmin=0)

np.savetxt('serie_2_RN_python_8192.txt',x)
