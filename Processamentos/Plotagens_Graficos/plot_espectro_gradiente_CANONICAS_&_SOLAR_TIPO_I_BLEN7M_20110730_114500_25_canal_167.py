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
    0.000000000000000000e+00,  # err0 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L1
    1.818887039614450196e-01,  # err1 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L2
    2.000220844233039363e-01,  # err2 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L3
    2.803879108148941701e-01,  # err3 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L4
    2.839939296106970268e-01,  # err4 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L5
    3.191586463486225655e-01,  # err5 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L6
    3.594840117419935699e-01,  # err6 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L7
    3.607748668473308440e-01,  # err7 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L8
    3.873695510064779635e-01,  # err8 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L9
    4.135756532404246677e-01,  # err9 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L10
    4.813642352978468320e-01,  # err10 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L11

    0.000000000000000000e+00,  # err11 = Desvio Pink Noise - L1
    8.292749289926681922e-02,  # err12 = Desvio Pink Noise - L2
    3.881568339482397573e-02,  # err13 = Desvio Pink Noise - L3
    6.702514452740436501e-02,  # err14 = Desvio Pink Noise - L4
    9.487191441332315511e-02,  # err15 = Desvio Pink Noise - L5
    1.307317027476166127e-01,  # err16 = Desvio Pink Noise - L6
    1.653652966854543271e-01,  # err17 = Desvio Pink Noise - L7
    1.657532712829738186e-01,  # err18 = Desvio Pink Noise - L8
    1.814054664423266905e-01,  # err19 = Desvio Pink Noise - L9
    2.218495092411303937e-01,  # err20 = Desvio Pink Noise - L10
    2.604126320236726522e-01,  # err21 = Desvio Pink Noise - L11

    0.000000000000000000e+00,  # err22 = Desvio Red Noise - L1
    1.022798934725334258e-01,  # err23 = Desvio Red Noise - L2
    1.654114330805797894e-01,  # err24 = Desvio Red Noise - L3
    2.248501396266048002e-01,  # err25 = Desvio Red Noise - L4
    2.342698514142647348e-01,  # err26 = Desvio Red Noise - L5
    2.395241240426791984e-01,  # err27 = Desvio Red Noise - L6
    2.841615455989280892e-01,  # err28 = Desvio Red Noise - L7
    2.670071122315827439e-01,  # err29 = Desvio Red Noise - L8
    2.739434119157976300e-01,  # err30 = Desvio Red Noise - L9
    2.734179128651152424e-01,  # err31 = Desvio Red Noise - L10
    2.438620047156201120e-01,  # err32 = Desvio Red Noise - L11

    0.000000000000000000e+00,  # err33 = Desvio White Noise - L1
    4.582729503730989529e-02,  # err34 = Desvio White Noise - L2
    3.010927611098440301e-02,  # err35 = Desvio White Noise - L3
    4.000207491955741490e-02,  # err36 = Desvio White Noise - L4
    3.577063914068297906e-02,  # err37 = Desvio White Noise - L5
    6.155357417560330252e-02,  # err38 = Desvio White Noise - L6
    9.870695784265673400e-02,  # err39 = Desvio White Noise - L7
    1.098014316392480205e-01,  # err40 = Desvio White Noise - L8
    1.531714023662304192e-01,  # err41 = Desvio White Noise - L9
    1.795615002213443445e-01,  # err42 = Desvio White Noise - L10
    2.527161822524726098e-01,  # err43 = Desvio White Noise - L11

    0.000000000000000000e+00,  # err44 = Desvio A0_Turb6mil - L1
    5.196388672481083715e-02,  # err45 = Desvio A0_Turb6mil - L2
    1.062639096407115707e-01,  # err46 = Desvio A0_Turb6mil - L3
    1.698162247180417528e-01,  # err47 = Desvio A0_Turb6mil - L4
    1.647500688068017083e-01,  # err48 = Desvio A0_Turb6mil - L5
    2.121490745727109828e-01,  # err49 = Desvio A0_Turb6mil - L6
    2.200268751860635363e-01,  # err50 = Desvio A0_Turb6mil - L7
    2.435237967361106037e-01,  # err51 = Desvio A0_Turb6mil - L8
    2.376395135018539162e-01,  # err52 = Desvio A0_Turb6mil - L9
    2.998334599475735440e-01,  # err53 = Desvio A0_Turb6mil - L10
    4.310574256998068732e-01,  # err54 = Desvio A0_Turb6mil - L11

    0.000000000000000000e+00,  # err55 = Desvio A5_Chua-Chaos_Y1 - L1
    7.160444457931836038e-02,  # err56 = Desvio A5_Chua-Chaos_Y1 - L2
    2.211034209926045491e-01,  # err57 = Desvio A5_Chua-Chaos_Y1 - L3
    2.357032326311176151e-01,  # err58 = Desvio A5_Chua-Chaos_Y1 - L4
    1.934679550840142093e-01,  # err59 = Desvio A5_Chua-Chaos_Y1 - L5
    2.948569451769261218e-01,  # err60 = Desvio A5_Chua-Chaos_Y1 - L6
    1.843699732826659388e-01,  # err61 = Desvio A5_Chua-Chaos_Y1 - L7
    2.328040154382775284e-01,  # err62 = Desvio A5_Chua-Chaos_Y1 - L8
    2.177127917470107199e-01,  # err63 = Desvio A5_Chua-Chaos_Y1 - L9
    1.307837075173075292e-01,  # err64 = Desvio A5_Chua-Chaos_Y1 - L10
    1.191513226305999235e-01,  # err65 = Desvio A5_Chua-Chaos_Y1 - L11

    0.000000000000000000e+00,  # err66 = Desvio A6-Logist - L1
    8.448260645589282525e-03,  # err67 = Desvio A6-Logist - L2
    1.977348538919577667e-02,  # err68 = Desvio A6-Logist - L3
    4.923443390830519600e-02,  # err69 = Desvio A6-Logist - L4
    5.387158748979149064e-02,  # err70 = Desvio A6-Logist - L5
    5.453660252209637654e-02,  # err71 = Desvio A6-Logist - L6
    1.047911860632088077e-01,  # err72 = Desvio A6-Logist - L7
    1.193641707381618566e-01,  # err73 = Desvio A6-Logist - L8
    1.678962670490296294e-01,  # err74 = Desvio A6-Logist - L9
    2.537844781929228799e-01,  # err75 = Desvio A6-Logist - L10
    2.544327146961998798e-01,  # err76 = Desvio A6-Logist - L11

    0.000000000000000000e+00,  # err77 = Desvio A7-Henon_x - L1
    1.915570813029542074e-02,  # err78 = Desvio A7-Henon_x - L2
    4.045475736875404210e-02,  # err79 = Desvio A7-Henon_x - L3
    4.674069397780619001e-02,  # err80 = Desvio A7-Henon_x - L4
    5.183704177500388782e-02,  # err81 = Desvio A7-Henon_x - L5
    4.454619147044854705e-02,  # err82 = Desvio A7-Henon_x - L6
    1.114025125631120938e-01,  # err83 = Desvio A7-Henon_x - L7
    9.018676562029465105e-02,  # err84 = Desvio A7-Henon_x - L8
    1.883917166129603915e-01,  # err85 = Desvio A7-Henon_x - L9
    1.533921511332417831e-01,  # err86 = Desvio A7-Henon_x - L10
    1.877803859743258919e-01,  # err87 = Desvio A7-Henon_x - L11

    0.000000000000000000e+00,  # err88 = Desvio A8_PModel - L1
    5.152844832662343416e-02,  # err89 = Desvio A8_PModel - L2
    7.937299753390733570e-02,  # err90 = Desvio A8_PModel - L3
    1.090306423235300332e-01,  # err91 = Desvio A8_PModel - L4
    7.766724031172909937e-02,  # err92 = Desvio A8_PModel - L5
    1.159172862225647388e-01,  # err93 = Desvio A8_PModel - L6
    1.629305694049077990e-01,  # err94 = Desvio A8_PModel - L7
    1.938861529556573648e-01,  # err95 = Desvio A8_PModel - L8
    2.583855996460495685e-01,  # err96 = Desvio A8_PModel - L9
    2.750878332887585209e-01,  # err97 = Desvio A8_PModel - L10
    2.318010870367245846e-01,  # err98 = Desvio A8_PModel - L11

])

y = np.array([
    5.200299024581909180e-01,  # y0 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L1
    6.492353826761245728e-01,  # y1 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L2
    6.473098761505551302e-01,  # y2 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L3
    6.991776339709758759e-01,  # y3 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L4
    7.268978154659271329e-01,  # y4 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L5
    8.162264236145548857e-01,  # y5 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L6
    7.899758884310722484e-01,  # y6 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L7
    7.542468911140329801e-01,  # y7 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L8
    7.476957111226187891e-01,  # y8 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L9
    6.709427936002612114e-01,  # y9 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L10
    5.035539552900526461e-01,  # y10 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L11

    1.562191605567932129e+00,  # y11 = GA Pink Noise - L1
    1.733395159244537354e+00,  # y12 = GA Pink Noise - L2
    1.824261214998033287e+00,  # y13 = GA Pink Noise - L3
    1.792525112628936768e+00,  # y14 = GA Pink Noise - L4
    1.782632098197937109e+00,  # y15 = GA Pink Noise - L5
    1.809760444694095138e+00,  # y16 = GA Pink Noise - L6
    1.722051341533660906e+00,  # y17 = GA Pink Noise - L7
    1.716792451010809906e+00,  # y18 = GA Pink Noise - L8
    1.624108693864610542e+00,  # y19 = GA Pink Noise - L9
    1.532709142267703939e+00,  # y20 = GA Pink Noise - L10
    1.246322635412216107e+00,  # y21 = GA Pink Noise - L11

    1.234397530555725098e+00,  # y22 = GA Red Noise - L1
    1.423616975545883179e+00,  # y23 = GA Red Noise - L2
    1.491200963656107659e+00,  # y24 = GA Red Noise - L3
    1.636851325631141663e+00,  # y25 = GA Red Noise - L4
    1.545265154838562083e+00,  # y26 = GA Red Noise - L5
    1.529780613051520355e+00,  # y27 = GA Red Noise - L6
    1.469976834058761561e+00,  # y28 = GA Red Noise - L7
    1.479939395354853637e+00,  # y29 = GA Red Noise - L8
    1.419872680770026374e+00,  # y30 = GA Red Noise - L9
    1.373785946667194446e+00,  # y31 = GA Red Noise - L10
    1.196902371446291635e+00,  # y32 = GA Red Noise - L11

    1.672415256500244141e+00,  # y33 = GA White Noise - L1
    1.805989593267440796e+00,  # y34 = GA White Noise - L2
    1.844718562232123382e+00,  # y35 = GA White Noise - L3
    1.878736235201358795e+00,  # y36 = GA White Noise - L4
    1.879872035980224565e+00,  # y37 = GA White Noise - L5
    1.865250657002131218e+00,  # y38 = GA White Noise - L6
    1.809510090351104772e+00,  # y49 = GA White Noise - L7
    1.785826299753453972e+00,  # y40 = GA White Noise - L8
    1.701461219787597567e+00,  # y41 = GA White Noise - L9
    1.655520069897174817e+00,  # y42 = GA White Noise - L10
    1.244268350071377149e+00,  # y43 = GA White Noise - L11

    1.161935806274414062e+00,  # y44 = GA A0_Turb6mil - L1
    1.330193281173706055e+00,  # y45 = GA A0_Turb6mil - L2
    1.421731458769904144e+00,  # y46 = GA A0_Turb6mil - L3
    1.381623163819313049e+00,  # y47 = GA A0_Turb6mil - L4
    1.407230782508850142e+00,  # y48 = GA A0_Turb6mil - L5
    1.408475759956571816e+00,  # y49 = GA A0_Turb6mil - L6
    1.365505071878433174e+00,  # y50 = GA A0_Turb6mil - L7
    1.292956912269194847e+00,  # y51 = GA A0_Turb6mil - L8
    1.283838476604885592e+00,  # y52 = GA A0_Turb6mil - L9
    1.228831811100244531e+00,  # y53 = GA A0_Turb6mil - L10
    9.580298647615644869e-01,  # y54 = GA A0_Turb6mil - L11

    7.842429876327514648e-01,  # y55 = GA A5_Chua-Chaos_Y1 - L1
    7.557827979326248169e-01,  # y56 = GA A5_Chua-Chaos_Y1 - L2
    6.953620546393923796e-01,  # y57 = GA A5_Chua-Chaos_Y1 - L3
    8.447197563946247101e-01,  # y58 = GA A5_Chua-Chaos_Y1 - L4
    8.128034853935242054e-01,  # y59 = GA A5_Chua-Chaos_Y1 - L5
    9.569090364707840690e-01,  # y60 = GA A5_Chua-Chaos_Y1 - L6
    1.130665800571441615e+00,  # y61 = GA A5_Chua-Chaos_Y1 - L7
    1.118756199048625000e+00,  # y62 = GA A5_Chua-Chaos_Y1 - L8
    1.101531460550096320e+00,  # y63 = GA A5_Chua-Chaos_Y1 - L9
    1.039251133203506372e+00,  # y64 = GA A5_Chua-Chaos_Y1 - L10
    1.028940767447153792e+00,  # y65 = GA A5_Chua-Chaos_Y1 - L11

    1.732169389724731445e+00,  # y66 = GA A6-Logist - L1
    1.839761018753051758e+00,  # y67 = GA A6-Logist - L2
    1.879981372091505287e+00,  # y68 = GA A6-Logist - L3
    1.856412500143051147e+00,  # y69 = GA A6-Logist - L4
    1.877669363021850613e+00,  # y70 = GA A6-Logist - L5
    1.872551663054360382e+00,  # y71 = GA A6-Logist - L6
    1.815555084943771380e+00,  # y72 = GA A6-Logist - L7
    1.791010438568062302e+00,  # y73 = GA A6-Logist - L8
    1.715466373761495023e+00,  # y74 = GA A6-Logist - L9
    1.604995469748973891e+00,  # y75 = GA A6-Logist - L10
    1.207765057616763560e+00,  # y76 = GA A6-Logist - L11

    1.736812233924865723e+00,  # y77 = GA A7-Henon_x - L1
    1.835977464914321899e+00,  # y78 = GA A7-Henon_x - L2
    1.863068342208862305e+00,  # y79 = GA A7-Henon_x - L3
    1.853009536862373352e+00,  # y80 = GA A7-Henon_x - L4
    1.886032142639160192e+00,  # y81 = GA A7-Henon_x - L5
    1.884076502588060142e+00,  # y82 = GA A7-Henon_x - L6
    1.821291923522949219e+00,  # y83 = GA A7-Henon_x - L7
    1.826002392503950356e+00,  # y84 = GA A7-Henon_x - L8
    1.653088703155517480e+00,  # y85 = GA A7-Henon_x - L9
    1.746920525878667751e+00,  # y86 = GA A7-Henon_x - L10
    1.149006404876709020e+00,  # y87 = GA A7-Henon_x - L11

    6.560088396072387695e-01, # y88 = GA A8_PModel - L1
    8.588469177484512329e-01, # y89 = GA A8_PModel - L2
    9.457062681516011926e-01, # y90 = GA A8_PModel - L3
    9.659395813941955566e-01, # y91 = GA A8_PModel - L4
    1.028566238880157524e+00, # y92 = GA A8_PModel - L5
    1.012238595220777748e+00, # y93 = GA A8_PModel - L6
    1.068692412972450212e+00, # y94 = GA A8_PModel - L7
    9.884538435273699797e-01, # y95 = GA A8_PModel - L8
    1.031506154007381770e+00, # y96 = GA A8_PModel - L9
    9.365553028881550279e-01, # y97 = GA A8_PModel - L10
    7.843818859259287235e-01, # y98 = GA A8_PModel - L11

])

#####################
#####################

plt.errorbar(x[0], y[0], yerr=err[0], marker='$\u2729$', capsize=0, markersize="22", color="black")
# NÃO HÁ DESVIO PARA GA DE L1


plt.errorbar(x[1], y[1], yerr=err[1], marker='$\u25A1$', capsize=0, markersize="22", color="black")
plt.plot(x[1], y[1] + err[1], marker="v", ls="", color="black", ms="22")
plt.plot(x[1], y[1] - err[1], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[2], y[2], yerr=err[2], marker='$\u266B$', capsize=0, markersize="22", color="black")
plt.plot(x[2], y[2] + err[2], marker="v", ls="", color="black", ms="22")
plt.plot(x[2], y[2] - err[2], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[3], y[3], yerr=err[3], marker='$\u2690$', capsize=0, markersize="22", color="black")
plt.plot(x[3], y[3] + err[3], marker="v", ls="", color="black", ms="22")
plt.plot(x[3], y[3] - err[3], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[4], y[4], yerr=err[4], marker='x', capsize=0, markersize="22", color="black")
plt.plot(x[4], y[4] + err[4], marker="v", ls="", color="black", ms="22")
plt.plot(x[4], y[4] - err[4], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[5], y[5], yerr=err[5], marker='$\u2693$', capsize=0, markersize="22", color="black")
plt.plot(x[5], y[5] + err[5], marker="v", ls="", color="black", ms="22")
plt.plot(x[5], y[5] - err[5], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[6], y[6], yerr=err[6], marker='$\u25CB$', capsize=0, markersize="22", color="black")
plt.plot(x[6], y[6] + err[6], marker="v", ls="", color="black", ms="22")
plt.plot(x[6], y[6] - err[6], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[7], y[7], yerr=err[7], marker='$\u2667$', capsize=0, markersize="22", color="black")
plt.plot(x[7], y[7] + err[7], marker="v", ls="", color="black", ms="22")
plt.plot(x[7], y[7] - err[7], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[8], y[8], yerr=err[8], marker='$\u2622$', capsize=0, markersize="22", color="black")
plt.plot(x[8], y[8] + err[8], marker="v", ls="", color="black", ms="22")
plt.plot(x[8], y[8] - err[8], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[9], y[9], yerr=err[9], marker='$\u26c2$', capsize=0, markersize="22", color="black")
plt.plot(x[9], y[9] + err[9], marker="v", ls="", color="black", ms="22")
plt.plot(x[9], y[9] - err[9], marker="^", ls="", color="black", ms="22")


plt.errorbar(x[10], y[10], yerr=err[10], marker='$\u263e$', capsize=0, markersize="22", color="black")
plt.plot(x[10], y[10] + err[10], marker="v", ls="", color="black", ms="22")
plt.plot(x[10], y[10] - err[10], marker="^", ls="", color="black", ms="22")


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

plt.errorbar(x[0], y[22], yerr=err[22], marker='$\u2729$', capsize=0, markersize="22", color="red")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA Red Noise - L1 (SEM DESVIO)

plt.errorbar(x[1], y[23], yerr=err[23], marker='$\u25A1$', capsize=0, markersize="22", color="red")
plt.plot(x[1], y[23] + err[23], marker="v", ls="", color="red", ms="22")
plt.plot(x[1], y[23] - err[23], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA Red Noise - L2 (COM DESVIO)

plt.errorbar(x[2], y[24], yerr=err[24], marker='$\u266B$', capsize=0, markersize="22", color="red")
plt.plot(x[2], y[24] + err[24], marker="v", ls="", color="red", ms="22")
plt.plot(x[2], y[24] - err[24], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L3 X GA Red Noise - L3 (COM DESVIO)

plt.errorbar(x[3], y[25], yerr=err[25], marker='$\u2690$', capsize=0, markersize="22", color="red")
plt.plot(x[3], y[25] + err[25], marker="v", ls="", color="red", ms="22")
plt.plot(x[3], y[25] - err[25], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L4 X GA Red Noise - L4 (COM DESVIO)

plt.errorbar(x[4], y[26], yerr=err[26], marker='x', capsize=0, markersize="22", color="red")
plt.plot(x[4], y[26] + err[26], marker="v", ls="", color="red", ms="22")
plt.plot(x[4], y[26] - err[26], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L5 X GA Red Noise - L5 (COM DESVIO)

plt.errorbar(x[5], y[27], yerr=err[27], marker='$\u2693$', capsize=0, markersize="22", color="red")
plt.plot(x[5], y[27] + err[27], marker="v", ls="", color="red", ms="22")
plt.plot(x[5], y[27] - err[27], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L6 X GA Red Noise - L6 (COM DESVIO)

plt.errorbar(x[6], y[28], yerr=err[28], marker='$\u25CB$', capsize=0, markersize="22", color="red")
plt.plot(x[6], y[28] + err[28], marker="v", ls="", color="red", ms="22")
plt.plot(x[6], y[28] - err[28], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L7 X GA Red Noise - L7 (COM DESVIO)

plt.errorbar(x[7], y[29], yerr=err[29], marker='$\u2667$', capsize=0, markersize="22", color="red")
plt.plot(x[7], y[29] + err[29], marker="v", ls="", color="red", ms="22")
plt.plot(x[7], y[29] - err[29], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L8 X GA Red Noise - L8 (COM DESVIO)

plt.errorbar(x[8], y[30], yerr=err[30], marker='$\u2622$', capsize=0, markersize="22", color="red")
plt.plot(x[8], y[30] + err[30], marker="v", ls="", color="red", ms="22")
plt.plot(x[8], y[30] - err[30], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L9 X GA Red Noise - L9 (COM DESVIO)

plt.errorbar(x[9], y[31], yerr=err[31], marker='$\u26c2$', capsize=0, markersize="22", color="red")
plt.plot(x[9], y[31] + err[31], marker="v", ls="", color="red", ms="22")
plt.plot(x[9], y[31] - err[31], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L10 X GA Red Noise - L10 (COM DESVIO)

plt.errorbar(x[10], y[32], yerr=err[32], marker='$\u263e$', capsize=0, markersize="22", color="red")
plt.plot(x[10], y[32] + err[32], marker="v", ls="", color="red", ms="22")
plt.plot(x[10], y[32] - err[32], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L11 X GA Red Noise - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[33], yerr=err[33], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:light grey")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA White Noise - L1 (SEM DESVIO)

plt.errorbar(x[1], y[34], yerr=err[34], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[1], y[34] + err[34], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[1], y[34] - err[34], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L2 X GA White Noise - L2 (COM DESVIO)


plt.errorbar(x[2], y[35], yerr=err[35], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[2], y[35] + err[35], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[2], y[35] - err[35], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L3 X GA White Noise - L3 (COM DESVIO)


plt.errorbar(x[3], y[36], yerr=err[36], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[3], y[36] + err[36], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[3], y[36] - err[36], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L4 X GA White Noise - L4 (COM DESVIO)


plt.errorbar(x[4], y[37], yerr=err[37], marker='x', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[4], y[37] + err[37], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[4], y[37] - err[37], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L5 X GA White Noise - L5 (COM DESVIO)


plt.errorbar(x[5], y[38], yerr=err[38], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[5], y[38] + err[38], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[5], y[38] - err[38], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L6 X GA White Noise - L6 (COM DESVIO)

plt.errorbar(x[6], y[39], yerr=err[39], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[6], y[39] + err[39], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[6], y[39] - err[39], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L7 X GA White Noise - L7 (COM DESVIO)

plt.errorbar(x[7], y[40], yerr=err[40], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[7], y[40] + err[40], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[7], y[40] - err[40], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L8 X GA White Noise - L8 (COM DESVIO)

plt.errorbar(x[8], y[41], yerr=err[41], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[8], y[41] + err[41], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[8], y[41] - err[41], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L9 X GA White Noise - L9 (COM DESVIO)

plt.errorbar(x[9], y[42], yerr=err[42], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[9], y[42] + err[42], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[9], y[42] - err[42], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L0 X GA White Noise - L10 (COM DESVIO)

plt.errorbar(x[10], y[43], yerr=err[43], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:light grey")
plt.plot(x[10], y[43] + err[43], marker="v", ls="", color="xkcd:light grey", ms="22")
plt.plot(x[10], y[43] - err[43], marker="^", ls="", color="xkcd:light grey", ms="22")
# PONTO LOG 1/L11 X GA White Noise - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[44], yerr=err[44], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:royal blue")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A0_Turb6mil - L1 (SEM DESVIO)

plt.errorbar(x[1], y[45], yerr=err[45], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[1], y[45] + err[45], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[1], y[45] - err[45], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA A0_Turb6mil - L2 (COM DESVIO)


plt.errorbar(x[2], y[46], yerr=err[46], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[2], y[46] + err[46], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[2], y[46] - err[46], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L3 X GA A0_Turb6mil - L3 (COM DESVIO)


plt.errorbar(x[3], y[47], yerr=err[47], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[3], y[47] + err[47], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[3], y[47] - err[47], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L4 X GA A0_Turb6mil - L4 (COM DESVIO)


plt.errorbar(x[4], y[48], yerr=err[48], marker='x', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[4], y[48] + err[48], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[4], y[48] - err[48], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L5 X GA A0_Turb6mil - L5 (COM DESVIO)


plt.errorbar(x[5], y[49], yerr=err[49], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[5], y[49] + err[49], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[5], y[49] - err[49], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L6 X GA A0_Turb6mil - L6 (COM DESVIO)

plt.errorbar(x[6], y[50], yerr=err[50], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[6], y[50] + err[50], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[6], y[50] - err[50], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L7 X GA A0_Turb6mil - L7 (COM DESVIO)

plt.errorbar(x[7], y[51], yerr=err[51], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[7], y[51] + err[51], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[7], y[51] - err[51], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L8 X GA A0_Turb6mil - L8 (COM DESVIO)

plt.errorbar(x[8], y[52], yerr=err[52], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[8], y[52] + err[52], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[8], y[52] - err[52], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L9 X GA A0_Turb6mil - L9 (COM DESVIO)

plt.errorbar(x[9], y[53], yerr=err[53], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[9], y[53] + err[53], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[9], y[53] - err[53], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L0 X GA A0_Turb6mil - L10 (COM DESVIO)

plt.errorbar(x[10], y[54], yerr=err[54], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[10], y[54] + err[54], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[10], y[54] - err[54], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L11 X GA A0_Turb6mil - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[55], yerr=err[55], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:green")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A5_Chua-Chaos_Y1 - L1 (SEM DESVIO)

plt.errorbar(x[1], y[56], yerr=err[56], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[1], y[56] + err[56], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[1], y[56] - err[56], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA A5_Chua-Chaos_Y1 - L2 (COM DESVIO)


plt.errorbar(x[2], y[57], yerr=err[57], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[2], y[57] + err[57], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[2], y[57] - err[57], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L3 X GA A5_Chua-Chaos_Y1 - L3 (COM DESVIO)


plt.errorbar(x[3], y[58], yerr=err[58], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[3], y[58] + err[58], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[3], y[58] - err[58], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L4 X GA A5_Chua-Chaos_Y1 - L4 (COM DESVIO)


plt.errorbar(x[4], y[59], yerr=err[59], marker='x', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[4], y[59] + err[59], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[4], y[59] - err[59], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L5 X GA A5_Chua-Chaos_Y1 - L5 (COM DESVIO)


plt.errorbar(x[5], y[60], yerr=err[60], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[5], y[60] + err[60], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[5], y[60] - err[60], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L6 X GA A5_Chua-Chaos_Y1 - L6 (COM DESVIO)

plt.errorbar(x[6], y[61], yerr=err[61], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[6], y[61] + err[61], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[6], y[61] - err[61], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L7 X GA A5_Chua-Chaos_Y1 - L7 (COM DESVIO)

plt.errorbar(x[7], y[62], yerr=err[62], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[7], y[62] + err[62], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[7], y[62] - err[62], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L8 X GA A5_Chua-Chaos_Y1 - L8 (COM DESVIO)

plt.errorbar(x[8], y[63], yerr=err[63], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[8], y[63] + err[63], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[8], y[63] - err[63], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L9 X GA A5_Chua-Chaos_Y1 - L9 (COM DESVIO)

plt.errorbar(x[9], y[64], yerr=err[64], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[9], y[64] + err[64], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[9], y[64] - err[64], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L0 X GA A5_Chua-Chaos_Y1 - L10 (COM DESVIO)

plt.errorbar(x[10], y[65], yerr=err[65], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[10], y[65] + err[65], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[10], y[65] - err[65], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L11 X GA A5_Chua-Chaos_Y1 - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[66], yerr=err[66], marker='$\u2729$', capsize=0, markersize="22", color="yellow")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A6-Logist - L1 (SEM DESVIO)

plt.errorbar(x[1], y[67], yerr=err[67], marker='$\u25A1$', capsize=0, markersize="22", color="yellow")
plt.plot(x[1], y[67] + err[67], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[1], y[67] - err[67], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA A6-Logist - L2 (COM DESVIO)


plt.errorbar(x[2], y[68], yerr=err[68], marker='$\u266B$', capsize=0, markersize="22", color="yellow")
plt.plot(x[2], y[68] + err[68], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[2], y[68] - err[68], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L3 X GA A6-Logist - L3 (COM DESVIO)


plt.errorbar(x[3], y[69], yerr=err[69], marker='$\u2690$', capsize=0, markersize="22", color="yellow")
plt.plot(x[3], y[69] + err[69], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[3], y[69] - err[69], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L4 X GA A6-Logist - L4 (COM DESVIO)


plt.errorbar(x[4], y[70], yerr=err[70], marker='x', capsize=0, markersize="22", color="yellow")
plt.plot(x[4], y[70] + err[70], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[4], y[70] - err[70], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L5 X GA A6-Logist - L5 (COM DESVIO)


plt.errorbar(x[5], y[71], yerr=err[71], marker='$\u2693$', capsize=0, markersize="22", color="yellow")
plt.plot(x[5], y[71] + err[71], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[5], y[71] - err[71], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L6 X GA A6-Logist - L6 (COM DESVIO)

plt.errorbar(x[6], y[72], yerr=err[72], marker='$\u25CB$', capsize=0, markersize="22", color="yellow")
plt.plot(x[6], y[72] + err[72], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[6], y[72] - err[72], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L7 X GA A6-Logist - L7 (COM DESVIO)

plt.errorbar(x[7], y[73], yerr=err[73], marker='$\u2667$', capsize=0, markersize="22", color="yellow")
plt.plot(x[7], y[73] + err[73], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[7], y[73] - err[73], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L8 X GA A6-Logist - L8 (COM DESVIO)

plt.errorbar(x[8], y[74], yerr=err[74], marker='$\u2622$', capsize=0, markersize="22", color="yellow")
plt.plot(x[8], y[74] + err[74], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[8], y[74] - err[74], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L9 X GA A6-Logist - L9 (COM DESVIO)

plt.errorbar(x[9], y[75], yerr=err[75], marker='$\u26c2$', capsize=0, markersize="22", color="yellow")
plt.plot(x[9], y[75] + err[75], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[9], y[75] - err[75], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L0 X GA A6-Logist - L10 (COM DESVIO)

plt.errorbar(x[10], y[76], yerr=err[76], marker='$\u263e$', capsize=0, markersize="22", color="yellow")
plt.plot(x[10], y[76] + err[76], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[10], y[76] - err[76], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L11 X GA A6-Logist - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[77], yerr=err[77], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:purple")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A7-Henon_x - L1 (SEM DESVIO)

plt.errorbar(x[1], y[78], yerr=err[78], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[1], y[78] + err[78], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[1], y[78] - err[78], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA A7-Henon_x - L2 (COM DESVIO)


plt.errorbar(x[2], y[79], yerr=err[79], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[2], y[79] + err[79], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[2], y[79] - err[79], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L3 X GA A7-Henon_x - L3 (COM DESVIO)


plt.errorbar(x[3], y[80], yerr=err[80], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[3], y[80] + err[80], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[3], y[80] - err[80], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L4 X GA A7-Henon_x - L4 (COM DESVIO)


plt.errorbar(x[4], y[81], yerr=err[81], marker='x', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[4], y[81] + err[81], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[4], y[81] - err[81], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L5 X GA A7-Henon_x - L5 (COM DESVIO)


plt.errorbar(x[5], y[82], yerr=err[82], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[5], y[82] + err[82], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[5], y[82] - err[82], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L6 X GA A7-Henon_x - L6 (COM DESVIO)

plt.errorbar(x[6], y[83], yerr=err[83], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[6], y[83] + err[83], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[6], y[83] - err[83], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L7 X GA A7-Henon_x - L7 (COM DESVIO)

plt.errorbar(x[7], y[84], yerr=err[84], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[7], y[84] + err[84], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[7], y[84] - err[84], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L8 X GA A7-Henon_x - L8 (COM DESVIO)

plt.errorbar(x[8], y[85], yerr=err[85], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[8], y[85] + err[85], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[8], y[85] - err[85], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L9 X GA A7-Henon_x - L9 (COM DESVIO)

plt.errorbar(x[9], y[86], yerr=err[86], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[9], y[86] + err[86], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[9], y[86] - err[86], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L0 X GA A7-Henon_x - L10 (COM DESVIO)

plt.errorbar(x[10], y[87], yerr=err[87], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[10], y[87] + err[87], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[10], y[87] - err[87], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L11 X GA A7-Henon_x - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[88], yerr=err[88], marker='$\u2729$', capsize=0, markersize="22", color="orange")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A8_PModel - L1 (SEM DESVIO)

plt.errorbar(x[1], y[89], yerr=err[89], marker='$\u25A1$', capsize=0, markersize="22", color="orange")
plt.plot(x[1], y[89] + err[89], marker="v", ls="", color="orange", ms="22")
plt.plot(x[1], y[89] - err[89], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L2 X GA A8_PModel - L2 (COM DESVIO)


plt.errorbar(x[2], y[90], yerr=err[90], marker='$\u266B$', capsize=0, markersize="22", color="orange")
plt.plot(x[2], y[90] + err[90], marker="v", ls="", color="orange", ms="22")
plt.plot(x[2], y[90] - err[90], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L3 X GA A8_PModel - L3 (COM DESVIO)


plt.errorbar(x[3], y[91], yerr=err[91], marker='$\u2690$', capsize=0, markersize="22", color="orange")
plt.plot(x[3], y[91] + err[91], marker="v", ls="", color="orange", ms="22")
plt.plot(x[3], y[91] - err[91], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L4 X GA A8_PModel - L4 (COM DESVIO)


plt.errorbar(x[4], y[92], yerr=err[92], marker='x', capsize=0, markersize="22", color="orange")
plt.plot(x[4], y[92] + err[92], marker="v", ls="", color="orange", ms="22")
plt.plot(x[4], y[92] - err[92], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L5 X GA A8_PModel - L5 (COM DESVIO)


plt.errorbar(x[5], y[93], yerr=err[93], marker='$\u2693$', capsize=0, markersize="22", color="orange")
plt.plot(x[5], y[93] + err[93], marker="v", ls="", color="orange", ms="22")
plt.plot(x[5], y[93] - err[93], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L6 X GA A8_PModel - L6 (COM DESVIO)

plt.errorbar(x[6], y[94], yerr=err[94], marker='$\u25CB$', capsize=0, markersize="22", color="orange")
plt.plot(x[6], y[94] + err[94], marker="v", ls="", color="orange", ms="22")
plt.plot(x[6], y[94] - err[94], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L7 X GA A8_PModel - L7 (COM DESVIO)

plt.errorbar(x[7], y[95], yerr=err[95], marker='$\u2667$', capsize=0, markersize="22", color="orange")
plt.plot(x[7], y[95] + err[95], marker="v", ls="", color="orange", ms="22")
plt.plot(x[7], y[95] - err[95], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L8 X GA A8_PModel - L8 (COM DESVIO)

plt.errorbar(x[8], y[96], yerr=err[96], marker='$\u2622$', capsize=0, markersize="22", color="orange")
plt.plot(x[8], y[96] + err[96], marker="v", ls="", color="orange", ms="22")
plt.plot(x[8], y[96] - err[96], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L9 X GA A8_PModel - L9 (COM DESVIO)

plt.errorbar(x[9], y[97], yerr=err[97], marker='$\u26c2$', capsize=0, markersize="22", color="orange")
plt.plot(x[9], y[97] + err[97], marker="v", ls="", color="orange", ms="22")
plt.plot(x[9], y[97] - err[97], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L0 X GA A8_PModel - L10 (COM DESVIO)

plt.errorbar(x[10], y[98], yerr=err[98], marker='$\u263e$', capsize=0, markersize="22", color="orange")
plt.plot(x[10], y[98] + err[98], marker="v", ls="", color="orange", ms="22")
plt.plot(x[10], y[98] - err[98], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L11 X GA A8_PModel - L11 (COM DESVIO)

plt.plot(x[0:11], y[0:11], linestyle="solid", label="CA", color="black")
plt.plot(x[0:11], y[11:22], linestyle="solid", label="PN", color="pink")
plt.plot(x[0:11], y[22:33], linestyle="solid", label="RN", color="red")
plt.plot(x[0:11], y[33:44], linestyle="solid", label="WN", color="xkcd:light grey")
plt.plot(x[0:11], y[44:55], linestyle="solid", label="A0_Turb6mil", color="xkcd:royal blue")
plt.plot(x[0:11], y[55:66], linestyle="solid", label="A5_Chua_Chaos_Y1", color="xkcd:green")
plt.plot(x[0:11], y[66:77], linestyle="solid", label="A6_Logist", color="yellow")
plt.plot(x[0:11], y[77:88], linestyle="solid", label="A7_Henon_x", color="xkcd:purple")
plt.plot(x[0:11], y[88:99], linestyle="solid", label="A8_PModel", color="orange")

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

CA = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_114500_25 - Canal 167)', color="black")
WN = mlines.Line2D([], [], linestyle="solid", label='White Noise', color="xkcd:light grey")
PN = mlines.Line2D([], [], linestyle="solid", label="Pink Noise", color="pink")
RN = mlines.Line2D([], [], linestyle="solid", label="Red Noise", color="red")
A0_Turb6mil = mlines.Line2D([], [], linestyle="solid", label='A0_Turb6mil', color="xkcd:royal blue")
A5_Chua_Chaos_Y1 = mlines.Line2D([], [], linestyle="solid", label='A5_Chua_Chaos_Y1', color="xkcd:green")
A6_Logist = mlines.Line2D([], [], linestyle="solid", label='A6_Logist', color="yellow")
A7_Henon_x = mlines.Line2D([], [], linestyle="solid", label='A7_Henon_x', color="xkcd:purple")
A8_PModel = mlines.Line2D([], [], linestyle="solid", label='A8_PModel', color="orange")

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
                    handles=[CA, WN, PN, RN, A0_Turb6mil, A5_Chua_Chaos_Y1, A6_Logist, A7_Henon_x, A8_PModel, L1, L2,
                             L3, L4, L5, L6, L7, L8, L9, L10, L11], fontsize="18", title="Legenda\n")

plt.setp(legend.get_title(), fontsize='18')
plt.grid(False)
plt.axis('off')
plt.savefig('legend.pdf', format="pdf", figsize=(1600, 1600), dpi=120)
plt.show()
plt.close()
