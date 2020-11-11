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
    0.000000000000000000e+00,  # err1 = Desvio White Noise - L1
    4.582729503730989529e-02,  # err2 = Desvio White Noise - L2
    3.010927611098440301e-02,  # err3 = Desvio White Noise - L3
    4.000207491955741490e-02,  # err4 = Desvio White Noise - L4
    3.577063914068297906e-02,  # err5 = Desvio White Noise - L5
    6.155357417560330252e-02,  # err6 = Desvio White Noise - L6
    9.870695784265673400e-02,  # err7 = Desvio White Noise - L7
    1.098014316392480205e-01,  # err8 = Desvio White Noise - L8
    1.531714023662304192e-01,  # err9 = Desvio White Noise - L9
    1.795615002213443445e-01,  # err10 = Desvio White Noise - L10
    2.527161822524726098e-01,  # err11 = Desvio White Noise - L11

    0.000000000000000000e+00,  # err12 = Desvio Pink Noise - L1
    8.292749289926681922e-02,  # err13 = Desvio Pink Noise - L2
    3.881568339482397573e-02,  # err14 = Desvio Pink Noise - L3
    6.702514452740436501e-02,  # err15 = Desvio Pink Noise - L4
    9.487191441332315511e-02,  # err16 = Desvio Pink Noise - L5
    1.307317027476166127e-01,  # err17 = Desvio Pink Noise - L6
    1.653652966854543271e-01,  # err18 = Desvio Pink Noise - L7
    1.657532712829738186e-01,  # err19 = Desvio Pink Noise - L8
    1.814054664423266905e-01,  # err20 = Desvio Pink Noise - L9
    2.218495092411303937e-01,  # err21 = Desvio Pink Noise - L10
    2.604126320236726522e-01,  # err22 = Desvio Pink Noise - L11

    0.000000000000000000e+00,  # err23 = Desvio A6-Logist - L1
    8.448260645589282525e-03,  # err24 = Desvio A6-Logist - L2
    1.977348538919577667e-02,  # err25 = Desvio A6-Logist - L3
    4.923443390830519600e-02,  # err26 = Desvio A6-Logist - L4
    5.387158748979149064e-02,  # err27 = Desvio A6-Logist - L5
    5.453660252209637654e-02,  # err28 = Desvio A6-Logist - L6
    1.047911860632088077e-01,  # err29 = Desvio A6-Logist - L7
    1.193641707381618566e-01,  # err30 = Desvio A6-Logist - L8
    1.678962670490296294e-01,  # err31 = Desvio A6-Logist - L9
    2.537844781929228799e-01,  # err32 = Desvio A6-Logist - L10
    2.544327146961998798e-01,  # err33 = Desvio A6-Logist - L11

    0.000000000000000000e+00,  # err34 = Desvio A7-Henon_x - L1
    1.915570813029542074e-02,  # err35 = Desvio A7-Henon_x - L2
    4.045475736875404210e-02,  # err36 = Desvio A7-Henon_x - L3
    4.674069397780619001e-02,  # err37 = Desvio A7-Henon_x - L4
    5.183704177500388782e-02,  # err38 = Desvio A7-Henon_x - L5
    4.454619147044854705e-02,  # err39 = Desvio A7-Henon_x - L6
    1.114025125631120938e-01,  # err40 = Desvio A7-Henon_x - L7
    9.018676562029465105e-02,  # err41 = Desvio A7-Henon_x - L8
    1.883917166129603915e-01,  # err42 = Desvio A7-Henon_x - L9
    1.533921511332417831e-01,  # err43 = Desvio A7-Henon_x - L10
    1.877803859743258919e-01,  # err44 = Desvio A7-Henon_x - L11

])

y = np.array([
    1.672415256500244141e+00,  # y1 = GA White Noise - L1
    1.805989593267440796e+00,  # y2 = GA White Noise - L2
    1.844718562232123382e+00,  # y3 = GA White Noise - L3
    1.878736235201358795e+00,  # y4 = GA White Noise - L4
    1.879872035980224565e+00,  # y5 = GA White Noise - L5
    1.865250657002131218e+00,  # y6 = GA White Noise - L6
    1.809510090351104772e+00,  # y7 = GA White Noise - L7
    1.785826299753453972e+00,  # y8 = GA White Noise - L8
    1.701461219787597567e+00,  # y9 = GA White Noise - L9
    1.655520069897174817e+00,  # y10 = GA White Noise - L10
    1.244268350071377149e+00,  # y11 = GA White Noise - L11

    1.562191605567932129e+00,  # y12 = GA Pink Noise - L1
    1.733395159244537354e+00,  # y13 = GA Pink Noise - L2
    1.824261214998033287e+00,  # y14 = GA Pink Noise - L3
    1.792525112628936768e+00,  # y15 = GA Pink Noise - L4
    1.782632098197937109e+00,  # y16 = GA Pink Noise - L5
    1.809760444694095138e+00,  # y17 = GA Pink Noise - L6
    1.722051341533660906e+00,  # y18 = GA Pink Noise - L7
    1.716792451010809906e+00,  # y19 = GA Pink Noise - L8
    1.624108693864610542e+00,  # y20 = GA Pink Noise - L9
    1.532709142267703939e+00,  # y21 = GA Pink Noise - L10
    1.246322635412216107e+00,  # y22 = GA Pink Noise - L11

    1.732169389724731445e+00,  # y23 = GA A6-Logist - L1
    1.839761018753051758e+00,  # y24 = GA A6-Logist - L2
    1.879981372091505287e+00,  # y25 = GA A6-Logist - L3
    1.856412500143051147e+00,  # y26 = GA A6-Logist - L4
    1.877669363021850613e+00,  # y27 = GA A6-Logist - L5
    1.872551663054360382e+00,  # y28 = GA A6-Logist - L6
    1.815555084943771380e+00,  # y29 = GA A6-Logist - L7
    1.791010438568062302e+00,  # y30 = GA A6-Logist - L8
    1.715466373761495023e+00,  # y31 = GA A6-Logist - L9
    1.604995469748973891e+00,  # y32 = GA A6-Logist - L10
    1.207765057616763560e+00,  # y33 = GA A6-Logist - L11

    1.736812233924865723e+00,  # y34 = GA A7-Henon_x - L1
    1.835977464914321899e+00,  # y35 = GA A7-Henon_x - L2
    1.863068342208862305e+00,  # y36 = GA A7-Henon_x - L3
    1.853009536862373352e+00,  # y37 = GA A7-Henon_x - L4
    1.886032142639160192e+00,  # y38 = GA A7-Henon_x - L5
    1.884076502588060142e+00,  # y39 = GA A7-Henon_x - L6
    1.821291923522949219e+00,  # y40 = GA A7-Henon_x - L7
    1.826002392503950356e+00,  # y41 = GA A7-Henon_x - L8
    1.653088703155517480e+00,  # y42 = GA A7-Henon_x - L9
    1.746920525878667751e+00,  # y43 = GA A7-Henon_x - L10
    1.149006404876709020e+00,  # y44 = GA A7-Henon_x - L11

])

#####################
#####################

plt.errorbar(x[0], y[0], yerr=err[0], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:light grey")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA White Noise - L1 (SEM DESVIO)

plt.errorbar(x[1], y[1], yerr=err[1], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[1], y[1] + err[1], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[1], y[1] - err[1], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L2 X GA White Noise - L2 (COM DESVIO)


plt.errorbar(x[2], y[2], yerr=err[2], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[2], y[2] + err[2], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[2], y[2] - err[2], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L3 X GA White Noise - L3 (COM DESVIO)


plt.errorbar(x[3], y[3], yerr=err[3], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[3], y[3] + err[3], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[3], y[3] - err[3], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L4 X GA White Noise - L4 (COM DESVIO)


plt.errorbar(x[4], y[4], yerr=err[4], marker='x', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[4], y[4] + err[4], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[4], y[4] - err[4], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L5 X GA White Noise - L5 (COM DESVIO)


plt.errorbar(x[5], y[5], yerr=err[5], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[5], y[5] + err[5], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[5], y[5] - err[5], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L6 X GA White Noise - L6 (COM DESVIO)

plt.errorbar(x[6], y[6], yerr=err[6], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[6], y[6] + err[6], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[6], y[6] - err[6], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L7 X GA White Noise - L7 (COM DESVIO)

plt.errorbar(x[7], y[7], yerr=err[7], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[7], y[7] + err[7], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[7], y[7] - err[7], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L8 X GA White Noise - L8 (COM DESVIO)

plt.errorbar(x[8], y[8], yerr=err[8], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[8], y[8] + err[8], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[8], y[8] - err[8], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L9 X GA White Noise - L9 (COM DESVIO)

plt.errorbar(x[9], y[9], yerr=err[9], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[9], y[9] + err[9], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[9], y[9] - err[9], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L0 X GA White Noise - L10 (COM DESVIO)

plt.errorbar(x[10], y[10], yerr=err[10], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[10], y[10] + err[10], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[10], y[10] - err[10], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L11 X GA White Noise - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[11], yerr=err[11], marker='$\u2729$', capsize=0, markersize="22", color="pink")
# NÃO HÁ DESVIO PARA GA DE L1
# PONTO LOG 1/L1 X GA Pink Noise - L1 (SEM DESVIO)

plt.errorbar(x[1], y[12], yerr=err[12], marker='$\u25A1$', capsize=0, markersize="22", color="pink")
plt.plot(x[1], y[12] + err[12], marker="v", ls="", color="pink", ms="22")
plt.plot(x[1], y[12] - err[12], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA Pink Noise - L2 (COM DESVIO)

plt.errorbar(x[2], y[13], yerr=err[13], marker='$\u266B$', capsize=0, markersize="22", color="pink")
plt.plot(x[2], y[13] + err[13], marker="v", ls="", color="pink", ms="22")
plt.plot(x[2], y[13] - err[13], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L3 X GA Pink Noise - L3 (COM DESVIO)

plt.errorbar(x[3], y[14], yerr=err[14], marker='$\u2690$', capsize=0, markersize="22", color="pink")
plt.plot(x[3], y[14] + err[14], marker="v", ls="", color="pink", ms="22")
plt.plot(x[3], y[14] - err[14], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L4 X GA Pink Noise - L4 (COM DESVIO)

plt.errorbar(x[4], y[15], yerr=err[15], marker='x', capsize=0, markersize="22", color="pink")
plt.plot(x[4], y[15] + err[15], marker="v", ls="", color="pink", ms="22")
plt.plot(x[4], y[15] - err[15], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L5 X GA Pink Noise - L5 (COM DESVIO)

plt.errorbar(x[5], y[16], yerr=err[16], marker='$\u2693$', capsize=0, markersize="22", color="pink")
plt.plot(x[5], y[16] + err[16], marker="v", ls="", color="pink", ms="22")
plt.plot(x[5], y[16] - err[16], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L6 X GA Pink Noise - L6 (COM DESVIO)

plt.errorbar(x[6], y[17], yerr=err[17], marker='$\u25CB$', capsize=0, markersize="22", color="pink")
plt.plot(x[6], y[17] + err[17], marker="v", ls="", color="pink", ms="22")
plt.plot(x[6], y[17] - err[17], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L7 X GA Pink Noise - L7 (COM DESVIO)

plt.errorbar(x[7], y[18], yerr=err[18], marker='$\u2667$', capsize=0, markersize="22", color="pink")
plt.plot(x[7], y[18] + err[18], marker="v", ls="", color="pink", ms="22")
plt.plot(x[7], y[18] - err[18], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L8 X GA Pink Noise - L8 (COM DESVIO)

plt.errorbar(x[8], y[19], yerr=err[19], marker='$\u2622$', capsize=0, markersize="22", color="pink")
plt.plot(x[8], y[19] + err[19], marker="v", ls="", color="pink", ms="22")
plt.plot(x[8], y[19] - err[19], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L9 X GA Pink Noise - L9 (COM DESVIO)

plt.errorbar(x[9], y[20], yerr=err[20], marker='$\u26c2$', capsize=0, markersize="22", color="pink")
plt.plot(x[9], y[20] + err[20], marker="v", ls="", color="pink", ms="22")
plt.plot(x[9], y[20] - err[20], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L10 X GA Pink Noise - L10 (COM DESVIO)

plt.errorbar(x[10], y[21], yerr=err[21], marker='$\u263e$', capsize=0, markersize="22", color="pink")
plt.plot(x[10], y[21] + err[21], marker="v", ls="", color="pink", ms="22")
plt.plot(x[10], y[21] - err[21], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L11 X GA Pink Noise - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[22], yerr=err[22], marker='$\u2729$', capsize=0, markersize="22", color="yellow")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A6-Logist - L1 (SEM DESVIO)

plt.errorbar(x[1], y[23], yerr=err[23], marker='$\u25A1$', capsize=0, markersize="22", color="yellow")
plt.plot(x[1], y[23] + err[23], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[1], y[23] - err[23], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA A6-Logist - L2 (COM DESVIO)


plt.errorbar(x[2], y[24], yerr=err[24], marker='$\u266B$', capsize=0, markersize="22", color="yellow")
plt.plot(x[2], y[24] + err[24], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[2], y[24] - err[24], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L3 X GA A6-Logist - L3 (COM DESVIO)


plt.errorbar(x[3], y[25], yerr=err[25], marker='$\u2690$', capsize=0, markersize="22", color="yellow")
plt.plot(x[3], y[25] + err[25], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[3], y[25] - err[25], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L4 X GA A6-Logist - L4 (COM DESVIO)


plt.errorbar(x[4], y[26], yerr=err[26], marker='x', capsize=0, markersize="22", color="yellow")
plt.plot(x[4], y[26] + err[26], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[4], y[26] - err[26], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L5 X GA A6-Logist - L5 (COM DESVIO)


plt.errorbar(x[5], y[27], yerr=err[27], marker='$\u2693$', capsize=0, markersize="22", color="yellow")
plt.plot(x[5], y[27] + err[27], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[5], y[27] - err[27], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L6 X GA A6-Logist - L6 (COM DESVIO)

plt.errorbar(x[6], y[28], yerr=err[28], marker='$\u25CB$', capsize=0, markersize="22", color="yellow")
plt.plot(x[6], y[28] + err[28], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[6], y[28] - err[28], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L7 X GA A6-Logist - L7 (COM DESVIO)

plt.errorbar(x[7], y[29], yerr=err[29], marker='$\u2667$', capsize=0, markersize="22", color="yellow")
plt.plot(x[7], y[29] + err[29], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[7], y[29] - err[29], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L8 X GA A6-Logist - L8 (COM DESVIO)

plt.errorbar(x[8], y[30], yerr=err[30], marker='$\u2622$', capsize=0, markersize="22", color="yellow")
plt.plot(x[8], y[30] + err[30], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[8], y[30] - err[30], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L9 X GA A6-Logist - L9 (COM DESVIO)

plt.errorbar(x[9], y[31], yerr=err[31], marker='$\u26c2$', capsize=0, markersize="22", color="yellow")
plt.plot(x[9], y[31] + err[31], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[9], y[31] - err[31], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L0 X GA A6-Logist - L10 (COM DESVIO)

plt.errorbar(x[10], y[32], yerr=err[32], marker='$\u263e$', capsize=0, markersize="22", color="yellow")
plt.plot(x[10], y[32] + err[32], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[10], y[32] - err[32], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L11 X GA A6-Logist - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[33], yerr=err[33], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:purple")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A7-Henon_x - L1 (SEM DESVIO)

plt.errorbar(x[1], y[34], yerr=err[34], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[1], y[34] + err[34], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[1], y[34] - err[34], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA A7-Henon_x - L2 (COM DESVIO)


plt.errorbar(x[2], y[35], yerr=err[35], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[2], y[35] + err[35], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[2], y[35] - err[35], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L3 X GA A7-Henon_x - L3 (COM DESVIO)


plt.errorbar(x[3], y[36], yerr=err[36], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[3], y[36] + err[36], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[3], y[36] - err[36], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L4 X GA A7-Henon_x - L4 (COM DESVIO)


plt.errorbar(x[4], y[37], yerr=err[37], marker='x', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[4], y[37] + err[37], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[4], y[37] - err[37], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L5 X GA A7-Henon_x - L5 (COM DESVIO)


plt.errorbar(x[5], y[38], yerr=err[38], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[5], y[38] + err[38], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[5], y[38] - err[38], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L6 X GA A7-Henon_x - L6 (COM DESVIO)

plt.errorbar(x[6], y[39], yerr=err[39], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[6], y[39] + err[39], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[6], y[39] - err[39], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L7 X GA A7-Henon_x - L7 (COM DESVIO)

plt.errorbar(x[7], y[40], yerr=err[40], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[7], y[40] + err[40], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[7], y[40] - err[40], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L8 X GA A7-Henon_x - L8 (COM DESVIO)

plt.errorbar(x[8], y[41], yerr=err[41], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[8], y[41] + err[41], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[8], y[41] - err[41], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L9 X GA A7-Henon_x - L9 (COM DESVIO)

plt.errorbar(x[9], y[42], yerr=err[42], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[9], y[42] + err[42], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[9], y[42] - err[42], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L0 X GA A7-Henon_x - L10 (COM DESVIO)

plt.errorbar(x[10], y[43], yerr=err[43], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[10], y[43] + err[43], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[10], y[43] - err[43], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L11 X GA A7-Henon_x - L11 (COM DESVIO)

#####################
#####################

plt.plot(x[0:11], y[0:11], linestyle="solid", label="WN", color="xkcd:light grey")
plt.plot(x[0:11], y[11:22], linestyle="solid", label="PN", color="pink")
plt.plot(x[0:11], y[22:33], linestyle="solid", label="A6_Logist", color="yellow")
plt.plot(x[0:11], y[33:44], linestyle="solid", label="A7_Henon_x", color="xkcd:purple")

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

WN = mlines.Line2D([], [], linestyle="solid", label='White Noise', color="xkcd:light grey")
PN = mlines.Line2D([], [], linestyle="solid", label="Pink Noise", color="pink")
A6_Logist = mlines.Line2D([], [], linestyle="solid", label='A6_Logist', color="yellow")
A7_Henon_x = mlines.Line2D([], [], linestyle="solid", label='A7_Henon_x', color="xkcd:purple")


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
                    handles=[WN, PN, A6_Logist, A7_Henon_x, L1, L2,
                             L3, L4, L5, L6, L7, L8, L9, L10, L11], fontsize="18", title="Legenda\n")

plt.setp(legend.get_title(), fontsize='18')
plt.grid(False)
plt.axis('off')
plt.savefig('legend.pdf', format="pdf", figsize=(1600, 1600), dpi=120)
plt.show()
plt.close()
