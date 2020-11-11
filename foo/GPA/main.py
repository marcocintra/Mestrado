import matplotlib.pyplot as plt
import sys
from GPA import GPA as ga
from mpl_toolkits.mplot3d import axes3d, Axes3D
import numpy as np
import timeit

def plot3D(g):
    fig = plt.figure()
    ax = plt.subplot(1,2,1, projection='3d')
    X = np.arange(0, len(g.mat), 1)
    Y = np.arange(0, len(g.mat[0]), 1)
    X, Y = np.meshgrid(X, Y)
    ax.plot_surface(X, Y, g.mat,rstride=1, cstride=1,cmap=plt.get_cmap('jet'),linewidth=0, antialiased=False, shade=False)

    #plt.imshow(g.mat, cmap=plt.get_cmap('gray'), origin='lower')
    
def invertY(m):
    mat = np.array([mat2[:] for mat2 in m])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[len(mat)-1-j,i] = m[j,i]
    return mat
    #
def plot_matrix2(g):
    plt.suptitle("Ga: "+str(g.Ga),fontsize=18)
    sbplt = plt.subplot(121)
    plt.title("Original Image")
    plt.contour(invertY(g.mat), cmap=plt.get_cmap('gray'), origin='lower')

    # plotting the asymmetric gradient field
    plt.subplot(122)
    plt.quiver(g.gradient_asymmetric_dy,g.gradient_asymmetric_dx, scale =1.0/0.03)
    plt.title("Asymmetric Gradient Field")
    #plt.title("C",fontsize=20)
    plt.show()

def plot_matrix(g):
    plt.suptitle("Ga: "+str(g.Ga),fontsize=18)
    plt.subplot(221)
    #plt.title("A",fontsize=20)
    plt.title("Original Image")
    plt.contour(invertY(g.mat), cmap=plt.get_cmap('gray'), origin='lower')

    #plt.gca().invert_yaxis()

    # plotting the asymmetric gradient field
    plt.subplot(223)
    plt.quiver(g.gradient_asymmetric_dy,g.gradient_asymmetric_dx, scale =1.0/0.06)
    print(np.array(g.gradient_dy))
    plt.xlim(-1,len(g.mat[0])+1)
    plt.ylim(-1,len(g.mat)+1)
    plt.title("Asymmetric Gradient Field")
    #plt.title("C",fontsize=20)

    # plotting the gradient field
    plt.subplot(222)
    plt.quiver(g.gradient_dy,g.gradient_dx, scale =1.0/0.06)
    plt.title("Gradient Field")
    plt.xlim(-1.,len(g.gradient_asymmetric_dy)+1)
    plt.ylim(-1.,len(g.gradient_asymmetric_dy)+1)
    #plt.title("B",fontsize=20)

    # plotting the triangulation
    if g.n_edges > 0:
        plt.subplot(224)
        plt.xlim(-1,len(g.mat[0])+1)
        plt.ylim(-1,len(g.mat)+1)
        plt.triplot(g.triangulation_points[:,0], g.triangulation_points[:,1], g.triangles.simplices.copy())
        plt.title("Triangulation")
        #plt.title("D",fontsize=20)

    plt.show()


if __name__ == "__main__":
    if('-h' in sys.argv) or ('--help' in sys.argv) or ((sys.argv[1] == "-l") and len(sys.argv) != 7) or ((sys.argv[1] != "-l") and (len(sys.argv) != 5)):
        print('================================')
        print('Syntax:')
        print('python main.py filename tol rad_tol ptol')
        print('python main.py -l filelist tol rad_tol ptol output')
        print('================================')
        print('')
        exit()
    if(sys.argv[1] != "-l" ):  
        fileName = sys.argv[1]
        tol = float(sys.argv[2])
        rad_tol = float(sys.argv[3])
        ptol = float(sys.argv[4])

        print("Reading "+fileName)
        inputMatrix = np.loadtxt(fileName)
        inputMatrix=inputMatrix.astype(np.float32)
        gaObject = ga(inputMatrix)
        gaObject.cx, gaObject.cy = len(inputMatrix[0])/2., len(inputMatrix)/2.
        gaObject.evaluate(tol,rad_tol,ptol)
        
        print(" Diversity ", gaObject.phaseDiversity)
        print(" Total asymmetric ", gaObject.totalAssimetric)
        print(" Total ", gaObject.totalVet)
        print(" Ga ",gaObject.Ga)
        
       # plot_matrix2(gaObject)
        #######################
        #######################
        #######################
        #######################
        #######################
    else:
        files = [line.rstrip() for line in open(sys.argv[2])]
        tol = float(sys.argv[3])
        rad_tol = float(sys.argv[4])
        ptol = float(sys.argv[5])
        gas = []        
        div = []
        total = []
        asy = []
        inputFiles = []

        for f in files:
            inputMatrix = np.loadtxt(f)
            inputMatrix=inputMatrix.astype(np.float32)
            gaObject = ga(inputMatrix)
            gaObject.cx, gaObject.cy = len(inputMatrix[0])/2., len(inputMatrix)/2.
            gaObject.evaluate(tol,rad_tol,ptol)
            print(f+" - Ga -",gaObject.Ga)
            gas.append(gaObject.Ga)
            div.append(gaObject.phaseDiversity)
            total.append(gaObject.totalVet)
            asy.append(gaObject.totalAssimetric)
            inputFiles.append(f)
        np.savetxt(sys.argv[5], np.array([inputFiles,gas,div,total,asy]).T, fmt="%s", header="Ga,Diversity,Total,Asymmetric", delimiter=',')
       
    plt.show()