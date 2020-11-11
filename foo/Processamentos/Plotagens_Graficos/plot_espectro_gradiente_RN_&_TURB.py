from matplotlib import pyplot as plt
import matplotlib
import matplotlib.lines as mlines
import math
import numpy as np
import pylab

F = pylab.gcf()
# Now check everything with the defaults:
DPI = 120
DefaultSize = F.get_size_inches()
# the default is 100dpi for savefig:
# F.savefig("test1.png")
# this gives me a 797 x 566 pixel image, which is about 100 DPI

# Now make the image twice as big, while keeping the fonts and all the
# same size
F.set_size_inches((DefaultSize[0] * 2, DefaultSize[1] * 2))
Size = F.get_size_inches()

plt.figure(1)

#plt.suptitle("Log 1/L X GAs (Callisto Type I Solar Bursts, 1/f Noises, Turbulent and Chaotic Series)", size="22")
plt.xlabel("Log 1/L", size="22")
plt.ylabel("GA", size="22")

x = np.array([
    math.log(1 / 3600, 10),  # x1 = math.log(1/3600,10) - L1
    math.log(1 / 900, 10),  # x2 = math.log(1/900,10 - L2
    math.log(1 / 400, 10),  # x3 = math.log(1/400,10) - L3
    math.log(1 / 225, 10),  # x4 = math.log(1/225,10) - L4
    math.log(1 / 144, 10),  # x5 = math.log(1/144,10) - L5
    math.log(1 / 100, 10),  # x6 = math.log(1/100,10) - L6
    math.log(1 / 36, 10),  # x7 = math.log(1/36,10) - L7
    math.log(1 / 25, 10),  # x8 = math.log(1/25,10) - L8
    math.log(1 / 16, 10),  # x9 = math.log(1/16,10) - L9
    math.log(1 / 9, 10),  # x10 = math.log(1/9,10) - L10
    math.log(1 / 4, 10), ])  # x11 = math.log(1/4,10) - L11

# L1 até L11 - 3600 = 60², 900 = 30², 400 = 20², 225 = 15², 144 = 12², 100 = 10², 36 = 6², 25 = 5², 16 = 4², 9 = 3²,
# 4 = 2²

err = np.array([
    0.000000000000000000e+00,  # err1 = Desvio Red Noise - L1
    1.022798934725334258e-01,  # err2 = Desvio Red Noise - L2
    1.654114330805797894e-01,  # err3 = Desvio Red Noise - L3
    2.248501396266048002e-01,  # err4 = Desvio Red Noise - L4
    2.342698514142647348e-01,  # err5 = Desvio Red Noise - L5
    2.395241240426791984e-01,  # err6 = Desvio Red Noise - L6
    2.841615455989280892e-01,  # err7 = Desvio Red Noise - L7
    2.670071122315827439e-01,  # err8 = Desvio Red Noise - L8
    2.739434119157976300e-01,  # err9 = Desvio Red Noise - L9
    2.734179128651152424e-01,  # err10 = Desvio Red Noise - L10
    2.438620047156201120e-01,  # err11 = Desvio Red Noise - L11

    0.000000000000000000e+00,  # err12 = Desvio A0_Turb6mil - L1
    5.196388672481083715e-02,  # err13 = Desvio A0_Turb6mil - L2
    1.062639096407115707e-01,  # err14 = Desvio A0_Turb6mil - L3
    1.698162247180417528e-01,  # err15 = Desvio A0_Turb6mil - L4
    1.647500688068017083e-01,  # err16 = Desvio A0_Turb6mil - L5
    2.121490745727109828e-01,  # err17 = Desvio A0_Turb6mil - L6
    2.200268751860635363e-01,  # err18 = Desvio A0_Turb6mil - L7
    2.435237967361106037e-01,  # err19 = Desvio A0_Turb6mil - L8
    2.376395135018539162e-01,  # err20 = Desvio A0_Turb6mil - L9
    2.998334599475735440e-01,  # err21 = Desvio A0_Turb6mil - L10
    4.310574256998068732e-01,  # err22 = Desvio A0_Turb6mil - L11
])

y = np.array([
    1.234397530555725098e+00,  # y1 = GA Red Noise - L1
    1.423616975545883179e+00,  # y2 = GA Red Noise - L2
    1.491200963656107659e+00,  # y3 = GA Red Noise - L3
    1.636851325631141663e+00,  # y4 = GA Red Noise - L4
    1.545265154838562083e+00,  # y5 = GA Red Noise - L5
    1.529780613051520355e+00,  # y6 = GA Red Noise - L6
    1.469976834058761561e+00,  # y7 = GA Red Noise - L7
    1.479939395354853637e+00,  # y8 = GA Red Noise - L8
    1.419872680770026374e+00,  # y9 = GA Red Noise - L9
    1.373785946667194446e+00,  # y10 = GA Red Noise - L10
    1.196902371446291635e+00,  # y11 = GA Red Noise - L11

    1.161935806274414062e+00,  # y12 = GA A0_Turb6mil - L1
    1.330193281173706055e+00,  # y13 = GA A0_Turb6mil - L2
    1.421731458769904144e+00,  # y14 = GA A0_Turb6mil - L3
    1.381623163819313049e+00,  # y15 = GA A0_Turb6mil - L4
    1.407230782508850142e+00,  # y16 = GA A0_Turb6mil - L5
    1.408475759956571816e+00,  # y17 = GA A0_Turb6mil - L6
    1.365505071878433174e+00,  # y18 = GA A0_Turb6mil - L7
    1.292956912269194847e+00,  # y19 = GA A0_Turb6mil - L8
    1.283838476604885592e+00,  # y20 = GA A0_Turb6mil - L9
    1.228831811100244531e+00,  # y21 = GA A0_Turb6mil - L10
    9.580298647615644869e-01,  # y22 = GA A0_Turb6mil - L11

])

#####################
#####################

plt.errorbar(x[0], y[0], yerr=err[0], marker='$\u2729$', capsize=0, markersize="22", color="red")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA Red Noise - L1 (SEM DESVIO)

plt.errorbar(x[1], y[1], yerr=err[1], marker='$\u25A1$', capsize=0, markersize="22", color="red")
plt.plot(x[1], y[1] + err[1], marker="v", ls="", color="red", ms="22")
plt.plot(x[1], y[1] - err[1], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA Red Noise - L2 (COM DESVIO)

plt.errorbar(x[2], y[2], yerr=err[2], marker='$\u266B$', capsize=0, markersize="22", color="red")
plt.plot(x[2], y[2] + err[2], marker="v", ls="", color="red", ms="22")
plt.plot(x[2], y[2] - err[2], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L3 X GA Red Noise - L3 (COM DESVIO)

plt.errorbar(x[3], y[3], yerr=err[3], marker='$\u2690$', capsize=0, markersize="22", color="red")
plt.plot(x[3], y[3] + err[3], marker="v", ls="", color="red", ms="22")
plt.plot(x[3], y[3] - err[3], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L4 X GA Red Noise - L4 (COM DESVIO)

plt.errorbar(x[4], y[4], yerr=err[4], marker='x', capsize=0, markersize="22", color="red")
plt.plot(x[4], y[4] + err[4], marker="v", ls="", color="red", ms="22")
plt.plot(x[4], y[4] - err[4], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L5 X GA Red Noise - L5 (COM DESVIO)

plt.errorbar(x[5], y[5], yerr=err[5], marker='$\u2693$', capsize=0, markersize="22", color="red")
plt.plot(x[5], y[5] + err[5], marker="v", ls="", color="red", ms="22")
plt.plot(x[5], y[5] - err[5], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L6 X GA Red Noise - L6 (COM DESVIO)

plt.errorbar(x[6], y[6], yerr=err[6], marker='$\u25CB$', capsize=0, markersize="22", color="red")
plt.plot(x[6], y[6] + err[6], marker="v", ls="", color="red", ms="22")
plt.plot(x[6], y[6] - err[6], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L7 X GA Red Noise - L7 (COM DESVIO)

plt.errorbar(x[7], y[7], yerr=err[7], marker='$\u2667$', capsize=0, markersize="22", color="red")
plt.plot(x[7], y[7] + err[7], marker="v", ls="", color="red", ms="22")
plt.plot(x[7], y[7] - err[7], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L8 X GA Red Noise - L8 (COM DESVIO)

plt.errorbar(x[8], y[8], yerr=err[8], marker='$\u2622$', capsize=0, markersize="22", color="red")
plt.plot(x[8], y[8] + err[8], marker="v", ls="", color="red", ms="22")
plt.plot(x[8], y[8] - err[8], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L9 X GA Red Noise - L9 (COM DESVIO)

plt.errorbar(x[9], y[9], yerr=err[9], marker='$\u26c2$', capsize=0, markersize="22", color="red")
plt.plot(x[9], y[9] + err[9], marker="v", ls="", color="red", ms="22")
plt.plot(x[9], y[9] - err[9], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L10 X GA Red Noise - L10 (COM DESVIO)

plt.errorbar(x[10], y[10], yerr=err[10], marker='$\u263e$', capsize=0, markersize="22", color="red")
plt.plot(x[10], y[10] + err[10], marker="v", ls="", color="red", ms="22")
plt.plot(x[10], y[10] - err[10], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L11 X GA Red Noise - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[11], yerr=err[11], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:royal blue")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A0_Turb6mil - L1 (SEM DESVIO)

plt.errorbar(x[1], y[12], yerr=err[12], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[1], y[12] + err[12], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[1], y[12] - err[12], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA A0_Turb6mil - L2 (COM DESVIO)


plt.errorbar(x[2], y[13], yerr=err[13], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[2], y[13] + err[13], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[2], y[13] - err[13], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L3 X GA A0_Turb6mil - L3 (COM DESVIO)


plt.errorbar(x[3], y[14], yerr=err[14], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[3], y[14] + err[14], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[3], y[14] - err[14], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L4 X GA A0_Turb6mil - L4 (COM DESVIO)


plt.errorbar(x[4], y[15], yerr=err[15], marker='x', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[4], y[15] + err[15], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[4], y[15] - err[15], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L5 X GA A0_Turb6mil - L5 (COM DESVIO)


plt.errorbar(x[5], y[16], yerr=err[16], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[5], y[16] + err[16], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[5], y[16] - err[16], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L6 X GA A0_Turb6mil - L6 (COM DESVIO)

plt.errorbar(x[6], y[17], yerr=err[17], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[6], y[17] + err[17], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[6], y[17] - err[17], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L7 X GA A0_Turb6mil - L7 (COM DESVIO)

plt.errorbar(x[7], y[18], yerr=err[18], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[7], y[18] + err[18], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[7], y[18] - err[18], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L8 X GA A0_Turb6mil - L8 (COM DESVIO)

plt.errorbar(x[8], y[19], yerr=err[19], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[8], y[19] + err[19], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[8], y[19] - err[19], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L9 X GA A0_Turb6mil - L9 (COM DESVIO)

plt.errorbar(x[9], y[20], yerr=err[20], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[9], y[20] + err[20], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[9], y[20] - err[20], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L0 X GA A0_Turb6mil - L10 (COM DESVIO)

plt.errorbar(x[10], y[21], yerr=err[21], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[10], y[21] + err[21], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[10], y[21] - err[21], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L11 X GA A0_Turb6mil - L11 (COM DESVIO)

plt.plot(x[0:11], y[0:11], linestyle="solid", label="RN", color="red")
plt.plot(x[0:11], y[11:22], linestyle="solid", label="A0_Turb6mil", color="xkcd:royal blue")

plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

plt.savefig("callisto-x-1-f-noises-and-turbulent-series-and-chaotic-series-gas-L1-L11.pdf", format="pdf",
            figsize=(1600, 1600), dpi=120)
plt.show()
plt.close()

F = pylab.gcf()
# Now check everything with the defaults:
DPI = 120
DefaultSize = F.get_size_inches()

# the default is 100dpi for savefig:
# F.savefig("test1.png")
# this gives me a 797 x 566 pixel image, which is about 100 DPI

# Now make the image twice as big, while keeping the fonts and all the
# same size
F.set_size_inches((DefaultSize[0] * 2, DefaultSize[1] * 2))
Size = F.get_size_inches()

plt.figure(1)

RN = mlines.Line2D([], [], linestyle="solid", label="Red Noise", color="red")
A0_Turb6mil = mlines.Line2D([], [], linestyle="solid", label='A0_Turb6mil', color="xkcd:royal blue")

L1 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2729$', ms="18", label='L1 = 3600')
L2 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u25A1$', ms="18", label='L2 = 900')
L3 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u266B$', ms="18", label='L3 = 400')
L4 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2690$', ms="18", label='L4 = 225')
L5 = mlines.Line2D([], [], linestyle="", color='black', marker='x', ms="18", label='L5 = 144')
L6 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2693$', ms="18", label='L6 = 100')
L7 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u25CB$', ms="18", label='L7 = 36')
L8 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2667$', ms="18", label='L8 = 25')
L9 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2622$', ms="18", label='L9 = 16')
L10 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u26c2$', ms="18", label='L10 = 9')
L11 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u263e$', ms="18", label='L11 = 4')

legend = plt.legend(loc='center',
                    handles=[RN, A0_Turb6mil, L1, L2,
                             L3, L4, L5, L6, L7, L8, L9, L10, L11], fontsize="18", title="Legenda\n")

plt.setp(legend.get_title(), fontsize='18')
plt.grid(False)
plt.axis('off')
plt.savefig('legend.pdf', format="pdf", figsize=(1600, 1600), dpi=120)
plt.show()
plt.close()
