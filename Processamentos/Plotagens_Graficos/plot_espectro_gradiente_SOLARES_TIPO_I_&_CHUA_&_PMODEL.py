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
    0.000000000000000000e+00,  # err0 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L1
    8.272580884620392427e-02,  # err1 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L2
    8.140513948932960597e-02,  # err2 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L3
    9.396102204932328672e-02,  # err3 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L4
    1.392656366388569378e-01,  # err4 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L5
    1.506513673468982961e-01,  # err5 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L6
    2.260539090609117452e-01,  # err6 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L7
    2.483496172585884787e-01,  # err7 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L8
    2.504345111414491010e-01,  # err8 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L9
    3.371372234764143383e-01,  # err9 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L10
    4.311920570178401357e-01,  # err10 = Desvio Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L11

    0.000000000000000000e+00,  # err11 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L1
    8.494071519060865383e-02,  # err12 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L2
    1.692282741557804004e-01,  # err13 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L3
    1.758648064668782707e-01,  # err14 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L4
    2.322008729344494926e-01,  # err15 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L5
    2.630056362496813183e-01,  # err16 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L6
    2.954061527063696624e-01,  # err17 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L7
    3.331946058466571103e-01,  # err18 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L8
    3.348239693096669578e-01,  # err19 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L9
    4.008903201973248454e-01,  # err20 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L10
    4.653122936330963966e-01,  # err21 = Desvio Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L11

    0.000000000000000000e+00,  # err22 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L1
    3.307705719130953348e-01,  # err23 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L2
    3.020602716414902966e-01,  # err24 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L3
    3.516625619531701386e-01,  # err25 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L4
    3.301890418327814158e-01,  # err26 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L5
    3.286104597853983789e-01,  # err27 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L6
    3.128124595891492166e-01,  # err28 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L7
    3.353228027901562491e-01,  # err29 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L8
    3.743184390276747542e-01,  # err30 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L9
    3.967881269559457302e-01,  # err31 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L10
    4.871775941413406530e-01,  # err32 = Desvio Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L11

    0.000000000000000000e+00,  # err33 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L1
    1.310571436720052996e-01,  # err34 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L2
    2.046953731579561342e-01,  # err35 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L3
    2.081418069322308606e-01,  # err36 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L4
    2.318195698334452048e-01,  # err37 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L5
    2.587040352292213075e-01,  # err38 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L6
    3.129627926456499121e-01,  # err39 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L7
    2.915368746556507018e-01,  # err40 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L8
    3.436605071208434503e-01,  # err41 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L9
    3.941312487783361074e-01,  # err42 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L10
    4.806504863836137953e-01,  # err43 = Desvio Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L11

    0.000000000000000000e+00,  # err44 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L1
    7.222228509405471952e-02,  # err45 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L2
    1.932706596793432319e-01,  # err46 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L3
    2.147154507435630744e-01,  # err47 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L4
    2.365194871388503484e-01,  # err48 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L5
    2.436017525941982231e-01,  # err49 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L6
    3.284046004258457385e-01,  # err50 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L7
    2.983995532115837901e-01,  # err51 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L8
    3.500408379218015176e-01,  # err52 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L9
    3.984367329217702314e-01,  # err53 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L10
    4.674747791685765486e-01,  # err54 = Desvio Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L11

    0.000000000000000000e+00,  # err55 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L1
    2.841029750002432852e-02,  # err56 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L2
    9.347155226063340316e-02,  # err57 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L3
    1.369433660594086277e-01,  # err58 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L4
    1.471418107080518511e-01,  # err59 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L5
    1.651061532998703285e-01,  # err60 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L6
    2.452996949427591888e-01,  # err61 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L7
    2.481025499739747397e-01,  # err62 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L8
    3.165374661538862822e-01,  # err63 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L9
    3.522661886853469260e-01,  # err64 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L10
    4.882595875069588587e-01,  # err65 = Desvio Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L11

    0.000000000000000000e+00,  # err66 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L1
    1.562449267406652575e-01,  # err67 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L2
    1.852136260051525096e-01,  # err68 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L3
    2.658140379175916723e-01,  # err69 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L4
    2.450698848972124033e-01,  # err70 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L5
    2.570522299893985285e-01,  # err71 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L6
    2.908769337797570409e-01,  # err72 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L7
    3.279708799430716137e-01,  # err73 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L8
    3.224376332554956814e-01,  # err74 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L9
    3.935758791616086882e-01,  # err75 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L10
    5.084710573687100110e-01,  # err76 = Desvio Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L11

    0.000000000000000000e+00,  # err77 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L1
    1.818887039614450196e-01,  # err78 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L2
    2.000220844233039363e-01,  # err79 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L3
    2.803879108148941701e-01,  # err80 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L4
    2.839939296106970268e-01,  # err81 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L5
    3.191586463486225655e-01,  # err82 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L6
    3.594840117419935699e-01,  # err83 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L7
    3.607748668473308440e-01,  # err84 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L8
    3.873695510064779635e-01,  # err86 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L9
    4.135756532404246677e-01,  # err86 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L10
    4.813642352978468320e-01,  # err87 = Desvio Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L11

    0.000000000000000000e+00,  # err88 = Desvio A5_Chua-Chaos_Y1 - L1
    7.160444457931836038e-02,  # err89 = Desvio A5_Chua-Chaos_Y1 - L2
    2.211034209926045491e-01,  # err90 = Desvio A5_Chua-Chaos_Y1 - L3
    2.357032326311176151e-01,  # err91 = Desvio A5_Chua-Chaos_Y1 - L4
    1.934679550840142093e-01,  # err92 = Desvio A5_Chua-Chaos_Y1 - L5
    2.948569451769261218e-01,  # err93 = Desvio A5_Chua-Chaos_Y1 - L6
    1.843699732826659388e-01,  # err94 = Desvio A5_Chua-Chaos_Y1 - L7
    2.328040154382775284e-01,  # err95 = Desvio A5_Chua-Chaos_Y1 - L8
    2.177127917470107199e-01,  # err96 = Desvio A5_Chua-Chaos_Y1 - L9
    1.307837075173075292e-01,  # err97 = Desvio A5_Chua-Chaos_Y1 - L10
    1.191513226305999235e-01,  # err98 = Desvio A5_Chua-Chaos_Y1 - L11

    0.000000000000000000e+00,  # err99 = Desvio A8_PModel - L1
    5.152844832662343416e-02,  # err100 = Desvio A8_PModel - L2
    7.937299753390733570e-02,  # err101 = Desvio A8_PModel - L3
    1.090306423235300332e-01,  # err102 = Desvio A8_PModel - L4
    7.766724031172909937e-02,  # err103 = Desvio A8_PModel - L5
    1.159172862225647388e-01,  # err104 = Desvio A8_PModel - L6
    1.629305694049077990e-01,  # err105 = Desvio A8_PModel - L7
    1.938861529556573648e-01,  # err106 = Desvio A8_PModel - L8
    2.583855996460495685e-01,  # err107 = Desvio A8_PModel - L9
    2.750878332887585209e-01,  # err108 = Desvio A8_PModel - L10
    2.318010870367245846e-01,  # err109 = Desvio A8_PModel - L11

])

y = np.array([
    2.227088212966918945e-01,  # y0 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L1
    3.272130526602268219e-01,  # y1 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L2
    3.702402495675616856e-01,  # y2 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L3
    4.171368014067411423e-01,  # y3 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L4
    4.531595867872237893e-01,  # y4 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L5
    4.926138578189743766e-01,  # y5 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L6
    5.892074615135789450e-01,  # y6 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L7
    6.033068045249415645e-01,  # y7 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L8
    5.796785250637266351e-01,  # y8 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L9
    5.492566481046378124e-01,  # y9 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L10
    3.884129671255747707e-01,  # y10 = GA Type I Burst (BLEN7M_20110730_054503_25_canal_167) - L11

    3.649891018867492676e-01,  # y11 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L1
    4.593167006969451904e-01,  # y12 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L2
    5.538901454872555696e-01,  # y13 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L3
    5.546728204935789108e-01,  # y14 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L4
    6.098845857381820501e-01,  # y15 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L5
    6.143618449568748474e-01,  # y16 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L6
    6.962263554334640059e-01,  # y17 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L7
    7.163310515590839422e-01,  # y18 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L8
    6.781928806834750523e-01,  # y19 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L9
    6.468571288511156814e-01,  # y20 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L10
    4.553839765654669747e-01,  # y21 = GA Type I Burst (BLEN7M_20110730_060002_25_canal_167) - L11

    4.130297005176544189e-01,  # y22 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L1
    4.919479340314865112e-01,  # y23 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L2
    5.586983131037818184e-01,  # y24 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L3
    6.508406158536672592e-01,  # y25 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L4
    6.771574747562408847e-01,  # y26 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L5
    6.816901821229193192e-01,  # y27 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L6
    7.502588321268558458e-01,  # y28 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L7
    7.594812414091494102e-01,  # y29 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L8
    7.219445746474796310e-01,  # y30 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L9
    6.688520904257893029e-01,  # y31 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L10
    4.678909173938963217e-01,  # y32 = GA Type I Burst (BLEN7M_20110730_061502_25_canal_167) - L11

    4.862808585166931152e-01,  # y33 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L1
    6.096868738532066345e-01,  # y34 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L2
    6.472717358006371269e-01,  # y35 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L3
    7.248395010828971863e-01,  # y36 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L4
    7.733169424533844483e-01,  # y37 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L5
    7.722447870506180534e-01,  # y38 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L6
    8.431149655580520985e-01,  # y39 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L7
    8.377507608901295644e-01,  # y40 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L8
    7.773540119992362607e-01,  # y41 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L9
    7.186386603675782858e-01,  # y42 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L10
    5.117504441075855226e-01,  # y43 = GA Type I Burst (BLEN7M_20110730_063002_25_canal_167) - L11

    3.810779154300689697e-01,  # y44 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L1
    4.817636162042617798e-01,  # y45 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L2
    5.653708626826604577e-01,  # y46 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L3
    6.195136718451976776e-01,  # y47 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L4
    6.465628921985626665e-01,  # y48 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L5
    6.843728141652213326e-01,  # y49 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L6
    7.319224170595407530e-01,  # y50 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L7
    6.993398084822628480e-01,  # y51 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L8
    6.881836578581068675e-01,  # y52 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L9
    6.228512154519557642e-01,  # y53 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L10
    4.599196896288130221e-01,  # y54 = GA Type I Burst (BLEN7M_20110730_064502_25_canal_167) - L11

    3.963913917541503906e-01,  # y55 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L1
    5.658796131610870361e-01,  # y56 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L2
    6.541440221998426896e-01,  # y57 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L3
    6.663960665464401245e-01,  # y58 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L4
    7.551105499267578569e-01,  # y59 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L5
    7.725255952941046944e-01,  # y60 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L6
    8.527805641293525474e-01,  # y61 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L7
    8.194718555443816221e-01,  # y62 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L8
    8.111527056164211658e-01,  # y63 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L9
    7.333467329852283445e-01,  # y64 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L10
    5.581355250544017821e-01,  # y65 = GA Type I Burst (BLEN7M_20110730_100002_25_canal_167) - L11

    4.946447908878326416e-01,  # y66 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L1
    5.798109471797943115e-01,  # y67 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L2
    6.134144630697038192e-01,  # y68 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L3
    6.974936034530401230e-01,  # y69 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L4
    7.257754111289977939e-01,  # y70 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L5
    7.698601567082934416e-01,  # y71 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L6
    8.061915262788533765e-01,  # y72 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L7
    8.308845294329026965e-01,  # y73 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L8
    8.416062594122356577e-01,  # y74 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L9
    7.482066721655428188e-01,  # y75 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L10
    5.800106914838155658e-01,  # y76 = GA Type I Burst (BLEN7M_20110730_110003_25_canal_167) - L11

    5.200299024581909180e-01,  # y77 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L1
    6.492353826761245728e-01,  # y78 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L2
    6.473098761505551302e-01,  # y79 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L3
    6.991776339709758759e-01,  # y80 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L4
    7.268978154659271329e-01,  # y81 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L5
    8.162264236145548857e-01,  # y82 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L6
    7.899758884310722484e-01,  # y83 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L7
    7.542468911140329801e-01,  # y84 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L8
    7.476957111226187891e-01,  # y85 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L9
    6.709427936002612114e-01,  # y86 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L10
    5.035539552900526461e-01,  # y87 = GA Type I Burst (BLEN7M_20110730_114500_25_canal_167) - L11

    7.842429876327514648e-01,  # y88 = GA A5_Chua-Chaos_Y1 - L1
    7.557827979326248169e-01,  # y89 = GA A5_Chua-Chaos_Y1 - L2
    6.953620546393923796e-01,  # y90 = GA A5_Chua-Chaos_Y1 - L3
    8.447197563946247101e-01,  # y91 = GA A5_Chua-Chaos_Y1 - L4
    8.128034853935242054e-01,  # y92 = GA A5_Chua-Chaos_Y1 - L5
    9.569090364707840690e-01,  # y93 = GA A5_Chua-Chaos_Y1 - L6
    1.130665800571441615e+00,  # y94 = GA A5_Chua-Chaos_Y1 - L7
    1.118756199048625000e+00,  # y95 = GA A5_Chua-Chaos_Y1 - L8
    1.101531460550096320e+00,  # y96 = GA A5_Chua-Chaos_Y1 - L9
    1.039251133203506372e+00,  # y97 = GA A5_Chua-Chaos_Y1 - L10
    1.028940767447153792e+00,  # y98 = GA A5_Chua-Chaos_Y1 - L11

    6.560088396072387695e-01, # y99 = GA A8_PModel - L1
    8.588469177484512329e-01, # y100 = GA A8_PModel - L2
    9.457062681516011926e-01, # y101 = GA A8_PModel - L3
    9.659395813941955566e-01, # y102 = GA A8_PModel - L4
    1.028566238880157524e+00, # y103 = GA A8_PModel - L5
    1.012238595220777748e+00, # y104 = GA A8_PModel - L6
    1.068692412972450212e+00, # y105 = GA A8_PModel - L7
    9.884538435273699797e-01, # y106 = GA A8_PModel - L8
    1.031506154007381770e+00, # y107 = GA A8_PModel - L9
    9.365553028881550279e-01, # y108 = GA A8_PModel - L10
    7.843818859259287235e-01, # y109 = GA A8_PModel - L11

])

#####################
#####################

plt.errorbar(x[0], y[0], yerr=err[0], marker='$\u2729$', capsize=0, markersize="22", color="black")
# NÃO HÁ DESVIO PARA GA DE L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[1], yerr=err[1], marker='$\u25A1$', capsize=0, markersize="22", color="black")
plt.plot(x[1], y[1] + err[1], marker="v", ls="", color="black", ms="22")
plt.plot(x[1], y[1] - err[1], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L2 (COM DESVIO)

plt.errorbar(x[2], y[2], yerr=err[2], marker='$\u266B$', capsize=0, markersize="22", color="black")
plt.plot(x[2], y[2] + err[2], marker="v", ls="", color="black", ms="22")
plt.plot(x[2], y[2] - err[2], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L3 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L3 (COM DESVIO)

plt.errorbar(x[3], y[3], yerr=err[3], marker='$\u2690$', capsize=0, markersize="22", color="black")
plt.plot(x[3], y[3] + err[3], marker="v", ls="", color="black", ms="22")
plt.plot(x[3], y[3] - err[3], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L4 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L4 (COM DESVIO)

plt.errorbar(x[4], y[4], yerr=err[4], marker='x', capsize=0, markersize="22", color="black")
plt.plot(x[4], y[4] + err[4], marker="v", ls="", color="black", ms="22")
plt.plot(x[4], y[4] - err[4], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L5 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L5 (COM DESVIO)

plt.errorbar(x[5], y[5], yerr=err[5], marker='$\u2693$', capsize=0, markersize="22", color="black")
plt.plot(x[5], y[5] + err[5], marker="v", ls="", color="black", ms="22")
plt.plot(x[5], y[5] - err[5], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L6 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[6], yerr=err[6], marker='$\u25CB$', capsize=0, markersize="22", color="black")
plt.plot(x[6], y[6] + err[6], marker="v", ls="", color="black", ms="22")
plt.plot(x[6], y[6] - err[6], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L7 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[7], yerr=err[7], marker='$\u2667$', capsize=0, markersize="22", color="black")
plt.plot(x[7], y[7] + err[7], marker="v", ls="", color="black", ms="22")
plt.plot(x[7], y[7] - err[7], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L8 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[8], yerr=err[8], marker='$\u2622$', capsize=0, markersize="22", color="black")
plt.plot(x[8], y[8] + err[8], marker="v", ls="", color="black", ms="22")
plt.plot(x[8], y[8] - err[8], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L9 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[9], yerr=err[9], marker='$\u26c2$', capsize=0, markersize="22", color="black")
plt.plot(x[9], y[9] + err[9], marker="v", ls="", color="black", ms="22")
plt.plot(x[9], y[9] - err[9], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L10 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[10], yerr=err[10], marker='$\u263e$', capsize=0, markersize="22", color="black")
plt.plot(x[10], y[10] + err[10], marker="v", ls="", color="black", ms="22")
plt.plot(x[10], y[10] - err[10], marker="^", ls="", color="black", ms="22")
# PONTO LOG 1/L11 X GA CALLISTO (BLEN7M_20110730_054503_25_CANAL_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[11], yerr=err[11], marker='$\u2729$', capsize=0, markersize="22", color="pink")
# NÃO HÁ DESVIO PARA GA DE L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[12], yerr=err[12], marker='$\u25A1$', capsize=0, markersize="22", color="pink")
plt.plot(x[1], y[12] + err[12], marker="v", ls="", color="pink", ms="22")
plt.plot(x[1], y[12] - err[12], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L2 (COM DESVIO)

plt.errorbar(x[2], y[13], yerr=err[13], marker='$\u266B$', capsize=0, markersize="22", color="pink")
plt.plot(x[2], y[13] + err[13], marker="v", ls="", color="pink", ms="22")
plt.plot(x[2], y[13] - err[13], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L3 (COM DESVIO)

plt.errorbar(x[3], y[14], yerr=err[14], marker='$\u2690$', capsize=0, markersize="22", color="pink")
plt.plot(x[3], y[14] + err[14], marker="v", ls="", color="pink", ms="22")
plt.plot(x[3], y[14] - err[14], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L4 (COM DESVIO)

plt.errorbar(x[4], y[15], yerr=err[15], marker='x', capsize=0, markersize="22", color="pink")
plt.plot(x[4], y[15] + err[15], marker="v", ls="", color="pink", ms="22")
plt.plot(x[4], y[15] - err[15], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L5 (COM DESVIO)

plt.errorbar(x[5], y[16], yerr=err[16], marker='$\u2693$', capsize=0, markersize="22", color="pink")
plt.plot(x[5], y[16] + err[16], marker="v", ls="", color="pink", ms="22")
plt.plot(x[5], y[16] - err[16], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[17], yerr=err[17], marker='$\u25CB$', capsize=0, markersize="22", color="pink")
plt.plot(x[6], y[17] + err[17], marker="v", ls="", color="pink", ms="22")
plt.plot(x[6], y[17] - err[17], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[18], yerr=err[18], marker='$\u2667$', capsize=0, markersize="22", color="pink")
plt.plot(x[7], y[18] + err[18], marker="v", ls="", color="pink", ms="22")
plt.plot(x[7], y[18] - err[18], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[19], yerr=err[19], marker='$\u2622$', capsize=0, markersize="22", color="pink")
plt.plot(x[8], y[19] + err[19], marker="v", ls="", color="pink", ms="22")
plt.plot(x[8], y[19] - err[19], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[20], yerr=err[20], marker='$\u26c2$', capsize=0, markersize="22", color="pink")
plt.plot(x[9], y[20] + err[20], marker="v", ls="", color="pink", ms="22")
plt.plot(x[9], y[20] - err[20], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[21], yerr=err[21], marker='$\u263e$', capsize=0, markersize="22", color="pink")
plt.plot(x[10], y[21] + err[21], marker="v", ls="", color="pink", ms="22")
plt.plot(x[10], y[21] - err[21], marker="^", ls="", color="pink", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_060002_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[22], yerr=err[22], marker='$\u2729$', capsize=0, markersize="22", color="red")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[23], yerr=err[23], marker='$\u25A1$', capsize=0, markersize="22", color="red")
plt.plot(x[1], y[23] + err[23], marker="v", ls="", color="red", ms="22")
plt.plot(x[1], y[23] - err[23], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L2 (COM DESVIO)

plt.errorbar(x[2], y[24], yerr=err[24], marker='$\u266B$', capsize=0, markersize="22", color="red")
plt.plot(x[2], y[24] + err[24], marker="v", ls="", color="red", ms="22")
plt.plot(x[2], y[24] - err[24], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L3 (COM DESVIO)

plt.errorbar(x[3], y[25], yerr=err[25], marker='$\u2690$', capsize=0, markersize="22", color="red")
plt.plot(x[3], y[25] + err[25], marker="v", ls="", color="red", ms="22")
plt.plot(x[3], y[25] - err[25], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L4 (COM DESVIO)

plt.errorbar(x[4], y[26], yerr=err[26], marker='x', capsize=0, markersize="22", color="red")
plt.plot(x[4], y[26] + err[26], marker="v", ls="", color="red", ms="22")
plt.plot(x[4], y[26] - err[26], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L5 (COM DESVIO)

plt.errorbar(x[5], y[27], yerr=err[27], marker='$\u2693$', capsize=0, markersize="22", color="red")
plt.plot(x[5], y[27] + err[27], marker="v", ls="", color="red", ms="22")
plt.plot(x[5], y[27] - err[27], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[28], yerr=err[28], marker='$\u25CB$', capsize=0, markersize="22", color="red")
plt.plot(x[6], y[28] + err[28], marker="v", ls="", color="red", ms="22")
plt.plot(x[6], y[28] - err[28], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[29], yerr=err[29], marker='$\u2667$', capsize=0, markersize="22", color="red")
plt.plot(x[7], y[29] + err[29], marker="v", ls="", color="red", ms="22")
plt.plot(x[7], y[29] - err[29], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[30], yerr=err[30], marker='$\u2622$', capsize=0, markersize="22", color="red")
plt.plot(x[8], y[30] + err[30], marker="v", ls="", color="red", ms="22")
plt.plot(x[8], y[30] - err[30], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[31], yerr=err[31], marker='$\u26c2$', capsize=0, markersize="22", color="red")
plt.plot(x[9], y[31] + err[31], marker="v", ls="", color="red", ms="22")
plt.plot(x[9], y[31] - err[31], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[32], yerr=err[32], marker='$\u263e$', capsize=0, markersize="22", color="red")
plt.plot(x[10], y[32] + err[32], marker="v", ls="", color="red", ms="22")
plt.plot(x[10], y[32] - err[32], marker="^", ls="", color="red", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_061502_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[33], yerr=err[33], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:silver")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[34], yerr=err[34], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[1], y[34] + err[34], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[1], y[34] - err[34], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L2 (COM DESVIO)


plt.errorbar(x[2], y[35], yerr=err[35], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[2], y[35] + err[35], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[2], y[35] - err[35], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L3 (COM DESVIO)


plt.errorbar(x[3], y[36], yerr=err[36], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[3], y[36] + err[36], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[3], y[36] - err[36], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L4 (COM DESVIO)


plt.errorbar(x[4], y[37], yerr=err[37], marker='x', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[4], y[37] + err[37], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[4], y[37] - err[37], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L5 (COM DESVIO)


plt.errorbar(x[5], y[38], yerr=err[38], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[5], y[38] + err[38], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[5], y[38] - err[38], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[39], yerr=err[39], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[6], y[39] + err[39], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[6], y[39] - err[39], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[40], yerr=err[40], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[7], y[40] + err[40], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[7], y[40] - err[40], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[41], yerr=err[41], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[8], y[41] + err[41], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[8], y[41] - err[41], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[42], yerr=err[42], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[9], y[42] + err[42], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[9], y[42] - err[42], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[43], yerr=err[43], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:silver")
plt.plot(x[10], y[43] + err[43], marker="v", ls="", color="xkcd:silver", ms="22")
plt.plot(x[10], y[43] - err[43], marker="^", ls="", color="xkcd:silver", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_063002_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[44], yerr=err[44], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:royal blue")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[45], yerr=err[45], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[1], y[45] + err[45], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[1], y[45] - err[45], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L2 (COM DESVIO)


plt.errorbar(x[2], y[46], yerr=err[46], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[2], y[46] + err[46], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[2], y[46] - err[46], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L3 (COM DESVIO)


plt.errorbar(x[3], y[47], yerr=err[47], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[3], y[47] + err[47], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[3], y[47] - err[47], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L4 (COM DESVIO)


plt.errorbar(x[4], y[48], yerr=err[48], marker='x', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[4], y[48] + err[48], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[4], y[48] - err[48], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L5 (COM DESVIO)


plt.errorbar(x[5], y[49], yerr=err[49], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[5], y[49] + err[49], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[5], y[49] - err[49], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[50], yerr=err[50], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[6], y[50] + err[50], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[6], y[50] - err[50], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[51], yerr=err[51], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[7], y[51] + err[51], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[7], y[51] - err[51], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[52], yerr=err[52], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[8], y[52] + err[52], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[8], y[52] - err[52], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[53], yerr=err[53], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[9], y[53] + err[53], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[9], y[53] - err[53], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[54], yerr=err[54], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:royal blue")
plt.plot(x[10], y[54] + err[54], marker="v", ls="", color="xkcd:royal blue", ms="22")
plt.plot(x[10], y[54] - err[54], marker="^", ls="", color="xkcd:royal blue", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_064502_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[55], yerr=err[55], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:green")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[56], yerr=err[56], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[1], y[56] + err[56], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[1], y[56] - err[56], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L2 (COM DESVIO)


plt.errorbar(x[2], y[57], yerr=err[57], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[2], y[57] + err[57], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[2], y[57] - err[57], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L3 (COM DESVIO)


plt.errorbar(x[3], y[58], yerr=err[58], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[3], y[58] + err[58], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[3], y[58] - err[58], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L4 (COM DESVIO)


plt.errorbar(x[4], y[59], yerr=err[59], marker='x', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[4], y[59] + err[59], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[4], y[59] - err[59], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L5 (COM DESVIO)


plt.errorbar(x[5], y[60], yerr=err[60], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[5], y[60] + err[60], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[5], y[60] - err[60], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[61], yerr=err[61], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[6], y[61] + err[61], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[6], y[61] - err[61], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[62], yerr=err[62], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[7], y[62] + err[62], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[7], y[62] - err[62], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[63], yerr=err[63], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[8], y[63] + err[63], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[8], y[63] - err[63], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[64], yerr=err[64], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[9], y[64] + err[64], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[9], y[64] - err[64], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[65], yerr=err[65], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:green")
plt.plot(x[10], y[65] + err[65], marker="v", ls="", color="xkcd:green", ms="22")
plt.plot(x[10], y[65] - err[65], marker="^", ls="", color="xkcd:green", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_100002_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[66], yerr=err[66], marker='$\u2729$', capsize=0, markersize="22", color="yellow")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[67], yerr=err[67], marker='$\u25A1$', capsize=0, markersize="22", color="yellow")
plt.plot(x[1], y[67] + err[67], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[1], y[67] - err[67], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L2 (COM DESVIO)


plt.errorbar(x[2], y[68], yerr=err[68], marker='$\u266B$', capsize=0, markersize="22", color="yellow")
plt.plot(x[2], y[68] + err[68], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[2], y[68] - err[68], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L3 (COM DESVIO)


plt.errorbar(x[3], y[69], yerr=err[69], marker='$\u2690$', capsize=0, markersize="22", color="yellow")
plt.plot(x[3], y[69] + err[69], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[3], y[69] - err[69], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L4 (COM DESVIO)


plt.errorbar(x[4], y[70], yerr=err[70], marker='x', capsize=0, markersize="22", color="yellow")
plt.plot(x[4], y[70] + err[70], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[4], y[70] - err[70], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L5 (COM DESVIO)


plt.errorbar(x[5], y[71], yerr=err[71], marker='$\u2693$', capsize=0, markersize="22", color="yellow")
plt.plot(x[5], y[71] + err[71], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[5], y[71] - err[71], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[72], yerr=err[72], marker='$\u25CB$', capsize=0, markersize="22", color="yellow")
plt.plot(x[6], y[72] + err[72], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[6], y[72] - err[72], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[73], yerr=err[73], marker='$\u2667$', capsize=0, markersize="22", color="yellow")
plt.plot(x[7], y[73] + err[73], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[7], y[73] - err[73], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[74], yerr=err[74], marker='$\u2622$', capsize=0, markersize="22", color="yellow")
plt.plot(x[8], y[74] + err[74], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[8], y[74] - err[74], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[75], yerr=err[75], marker='$\u26c2$', capsize=0, markersize="22", color="yellow")
plt.plot(x[9], y[75] + err[75], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[9], y[75] - err[75], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[76], yerr=err[76], marker='$\u263e$', capsize=0, markersize="22", color="yellow")
plt.plot(x[10], y[76] + err[76], marker="v", ls="", color="yellow", ms="22")
plt.plot(x[10], y[76] - err[76], marker="^", ls="", color="yellow", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_110003_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[77], yerr=err[77], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:purple")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L1 (SEM DESVIO)

plt.errorbar(x[1], y[78], yerr=err[78], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[1], y[78] + err[78], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[1], y[78] - err[78], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L2 (COM DESVIO)


plt.errorbar(x[2], y[79], yerr=err[79], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[2], y[79] + err[79], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[2], y[79] - err[79], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L3 (COM DESVIO)


plt.errorbar(x[3], y[80], yerr=err[80], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[3], y[80] + err[80], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[3], y[80] - err[80], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L4 (COM DESVIO)


plt.errorbar(x[4], y[81], yerr=err[81], marker='x', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[4], y[81] + err[81], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[4], y[81] - err[81], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L5 (COM DESVIO)


plt.errorbar(x[5], y[82], yerr=err[82], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[5], y[82] + err[82], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[5], y[82] - err[82], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L6 (COM DESVIO)

plt.errorbar(x[6], y[83], yerr=err[83], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[6], y[83] + err[83], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[6], y[83] - err[83], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L7 (COM DESVIO)

plt.errorbar(x[7], y[84], yerr=err[84], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[7], y[84] + err[84], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[7], y[84] - err[84], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L8 (COM DESVIO)

plt.errorbar(x[8], y[85], yerr=err[85], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[8], y[85] + err[85], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[8], y[85] - err[85], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L9 (COM DESVIO)

plt.errorbar(x[9], y[86], yerr=err[86], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[9], y[86] + err[86], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[9], y[86] - err[86], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L10 (COM DESVIO)

plt.errorbar(x[10], y[87], yerr=err[87], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:purple")
plt.plot(x[10], y[87] + err[87], marker="v", ls="", color="xkcd:purple", ms="22")
plt.plot(x[10], y[87] - err[87], marker="^", ls="", color="xkcd:purple", ms="22")
# PONTO LOG 1/L2 X GA CALLISTO (BLEN7M_20110730_114500_25_canal_167) L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[88], yerr=err[88], marker='$\u2729$', capsize=0, markersize="22", color="orange")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A5_Chua-Chaos_Y1 - L1 (SEM DESVIO)

plt.errorbar(x[1], y[89], yerr=err[89], marker='$\u25A1$', capsize=0, markersize="22", color="orange")
plt.plot(x[1], y[89] + err[89], marker="v", ls="", color="orange", ms="22")
plt.plot(x[1], y[89] - err[89], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L2 X GA A5_Chua-Chaos_Y1 - L2 (COM DESVIO)


plt.errorbar(x[2], y[90], yerr=err[90], marker='$\u266B$', capsize=0, markersize="22", color="orange")
plt.plot(x[2], y[90] + err[90], marker="v", ls="", color="orange", ms="22")
plt.plot(x[2], y[90] - err[90], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L3 X GA A5_Chua-Chaos_Y1 - L3 (COM DESVIO)


plt.errorbar(x[3], y[91], yerr=err[91], marker='$\u2690$', capsize=0, markersize="22", color="orange")
plt.plot(x[3], y[91] + err[91], marker="v", ls="", color="orange", ms="22")
plt.plot(x[3], y[91] - err[91], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L4 X GA A5_Chua-Chaos_Y1 - L4 (COM DESVIO)


plt.errorbar(x[4], y[92], yerr=err[92], marker='x', capsize=0, markersize="22", color="orange")
plt.plot(x[4], y[92] + err[92], marker="v", ls="", color="orange", ms="22")
plt.plot(x[4], y[92] - err[92], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L5 X GA A5_Chua-Chaos_Y1 - L5 (COM DESVIO)


plt.errorbar(x[5], y[93], yerr=err[93], marker='$\u2693$', capsize=0, markersize="22", color="orange")
plt.plot(x[5], y[93] + err[93], marker="v", ls="", color="orange", ms="22")
plt.plot(x[5], y[93] - err[93], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L6 X GA A5_Chua-Chaos_Y1 - L6 (COM DESVIO)

plt.errorbar(x[6], y[94], yerr=err[94], marker='$\u25CB$', capsize=0, markersize="22", color="orange")
plt.plot(x[6], y[94] + err[94], marker="v", ls="", color="orange", ms="22")
plt.plot(x[6], y[94] - err[94], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L7 X GA A5_Chua-Chaos_Y1 - L7 (COM DESVIO)

plt.errorbar(x[7], y[95], yerr=err[95], marker='$\u2667$', capsize=0, markersize="22", color="orange")
plt.plot(x[7], y[95] + err[95], marker="v", ls="", color="orange", ms="22")
plt.plot(x[7], y[95] - err[95], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L8 X GA A5_Chua-Chaos_Y1 - L8 (COM DESVIO)

plt.errorbar(x[8], y[96], yerr=err[96], marker='$\u2622$', capsize=0, markersize="22", color="orange")
plt.plot(x[8], y[96] + err[96], marker="v", ls="", color="orange", ms="22")
plt.plot(x[8], y[96] - err[96], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L9 X GA A5_Chua-Chaos_Y1 - L9 (COM DESVIO)

plt.errorbar(x[9], y[97], yerr=err[97], marker='$\u26c2$', capsize=0, markersize="22", color="orange")
plt.plot(x[9], y[97] + err[97], marker="v", ls="", color="orange", ms="22")
plt.plot(x[9], y[97] - err[97], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L0 X GA A5_Chua-Chaos_Y1 - L10 (COM DESVIO)

plt.errorbar(x[10], y[98], yerr=err[98], marker='$\u263e$', capsize=0, markersize="22", color="orange")
plt.plot(x[10], y[98] + err[98], marker="v", ls="", color="orange", ms="22")
plt.plot(x[10], y[98] - err[98], marker="^", ls="", color="orange", ms="22")
# PONTO LOG 1/L11 X GA A5_Chua-Chaos_Y1 - L11 (COM DESVIO)

#####################
#####################

plt.errorbar(x[0], y[99], yerr=err[99], marker='$\u2729$', capsize=0, markersize="22", color="xkcd:khaki")
# NÃO HÁ DESVIO PARA L1
# PONTO LOG 1/L1 X GA A8_PModel - L1 (SEM DESVIO)

plt.errorbar(x[1], y[100], yerr=err[100], marker='$\u25A1$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[1], y[100] + err[100], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[1], y[100] - err[100], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L2 X GA A8_PModel - L2 (COM DESVIO)


plt.errorbar(x[2], y[101], yerr=err[101], marker='$\u266B$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[2], y[101] + err[101], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[2], y[101] - err[101], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L3 X GA A8_PModel - L3 (COM DESVIO)


plt.errorbar(x[3], y[102], yerr=err[102], marker='$\u2690$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[3], y[102] + err[102], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[3], y[102] - err[102], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L4 X GA A8_PModel - L4 (COM DESVIO)


plt.errorbar(x[4], y[103], yerr=err[103], marker='x', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[4], y[103] + err[103], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[4], y[103] - err[103], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L5 X GA A8_PModel - L5 (COM DESVIO)


plt.errorbar(x[5], y[104], yerr=err[104], marker='$\u2693$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[5], y[104] + err[104], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[5], y[104] - err[104], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L6 X GA A8_PModel - L6 (COM DESVIO)

plt.errorbar(x[6], y[105], yerr=err[105], marker='$\u25CB$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[6], y[105] + err[105], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[6], y[105] - err[105], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L7 X GA A8_PModel - L7 (COM DESVIO)

plt.errorbar(x[7], y[106], yerr=err[106], marker='$\u2667$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[7], y[106] + err[106], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[7], y[106] - err[106], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L8 X GA A8_PModel - L8 (COM DESVIO)

plt.errorbar(x[8], y[107], yerr=err[107], marker='$\u2622$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[8], y[107] + err[107], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[8], y[107] - err[107], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L9 X GA A8_PModel - L9 (COM DESVIO)

plt.errorbar(x[9], y[108], yerr=err[108], marker='$\u26c2$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[9], y[108] + err[108], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[9], y[108] - err[108], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L0 X GA A8_PModel - L10 (COM DESVIO)

plt.errorbar(x[10], y[109], yerr=err[109], marker='$\u263e$', capsize=0, markersize="22", color="xkcd:khaki")
plt.plot(x[10], y[109] + err[109], marker="v", ls="", color="xkcd:khaki", ms="22")
plt.plot(x[10], y[109] - err[109], marker="^", ls="", color="xkcd:khaki", ms="22")
# PONTO LOG 1/L11 X GA A8_PModel - L11 (COM DESVIO)

plt.plot(x[0:11], y[0:11], linestyle="solid", label="CA1", color="black")
plt.plot(x[0:11], y[11:22], linestyle="solid", label="CA2", color="pink")
plt.plot(x[0:11], y[22:33], linestyle="solid", label="CA3", color="red")
plt.plot(x[0:11], y[33:44], linestyle="solid", label="CA4", color="xkcd:silver")
plt.plot(x[0:11], y[44:55], linestyle="solid", label="CA5", color="xkcd:royal blue")
plt.plot(x[0:11], y[55:66], linestyle="solid", label="CA6", color="xkcd:green")
plt.plot(x[0:11], y[66:77], linestyle="solid", label="CA7", color="yellow")
plt.plot(x[0:11], y[77:88], linestyle="solid", label="CA8", color="xkcd:purple")
plt.plot(x[0:11], y[88:99], linestyle="solid", label="CHUA", color="orange")
plt.plot(x[0:11], y[99:110], linestyle="solid", label="PMODEL", color="xkcd:khaki")

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

CA1 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_054503_25 - Canal 167', color="black")
CA2 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_060002_25 - Canal_167', color="pink")
CA3 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_061502_25 - Canal_167', color="red")
CA4 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_063002_25 - Canal_167', color="xkcd:silver")
CA5 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_064502_25 - Canal_167', color="xkcd:royal blue")
CA6 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_100002_25 - Canal_167', color="xkcd:green")
CA7 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_110003_25 - Canal_167', color="yellow")
CA8 = mlines.Line2D([], [], linestyle="solid", label='BLEN7M_20110730_114500_25 - Canal_167', color="xkcd:purple")
CHUA = mlines.Line2D([], [], linestyle="solid", label='A5_Chua-Chaos_Y1', color="orange")
PMODEL = mlines.Line2D([], [], linestyle="solid", label='A8_PModel', color="xkcd:khaki")

L1 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2729$', ms="16", label='L1 = 3600')
L2 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u25A1$', ms="16", label='L2 = 900')
L3 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u266B$', ms="16", label='L3 = 400')
L4 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2690$', ms="16", label='L4 = 225')
L5 = mlines.Line2D([], [], linestyle="", color='black', marker='x', ms="18", label='L5 = 144')
L6 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2693$', ms="16", label='L6 = 100')
L7 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u25CB$', ms="16", label='L7 = 36')
L8 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2667$', ms="16", label='L8 = 25')
L9 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u2622$', ms="16", label='L9 = 16')
L10 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u26c2$', ms="16", label='L10 = 9')
L11 = mlines.Line2D([], [], linestyle="", color='black', marker='$\u263e$', ms="16", label='L11 = 4')

legend = plt.legend(loc='center',
                    handles=[CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CHUA, PMODEL, L1, L2,
                             L3, L4, L5, L6, L7, L8, L9, L10, L11], fontsize="18", title="Legenda\n")

plt.setp(legend.get_title(), fontsize='18')
plt.grid(False)
plt.axis('off')
plt.savefig('legend.pdf', format="pdf", figsize=(1600, 1600), dpi=120)
plt.show()
plt.close()
