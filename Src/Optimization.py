import numpy as np
from scipy import stats
from CaDistanceMatrix import PointDistance,CaDistanceMatrix
import math

def Optimization():
    my_list = list()
    A = Atom_List('../Data/T0860/target.pdb')
    #print (A[2])
    TemplateMatrix_1 = CaDistanceMatrix('../Data/T0860/5fld.pdb',[34,35,36,37,38,39,40,41,42,43,44,45,46,47])
    TemplateMatrix_2 = CaDistanceMatrix('../Data/T0860/5fjl.pdb',[])
    #print(len(TemplateMatrix_1))
    #print(len())
    TargetMatrix = TargetDistanceMatrix(A)
    weights = [0.7,0.98]
    sigma = 0.1
    LearnRate = .01

    for i in xrange(1, len(A)):
        for j in xrange(i, len(A)):
            weightedProb_1 = 0
            weightedProb_2 = 0

            temp1 = weights[0] * Probability(TargetMatrix[i][j], TemplateMatrix_1[i][j])
            temp2 = weights[1] * Probability(TargetMatrix[i][j], TemplateMatrix_2[i][j])

            temp3 = weights[0] * Probability(TargetMatrix[i][j], TemplateMatrix_1[i][j])*\
                    (TargetMatrix[i][j]-TemplateMatrix_1[i][j])*(1/math.sqrt(sigma))
            temp4 = weights[1] * Probability(TargetMatrix[i][j], TemplateMatrix_2[i][j])*\
                    (TargetMatrix[i][j]-TemplateMatrix_2[i][j])*(1/math.sqrt(sigma))


            weightedProb_1 = weightedProb_1 + temp1 + temp2
            weightedProb_2 = weightedProb_2 + temp3 + temp4

            dij_drivative = 1/weightedProb_1*weightedProb_2

            #print ("Dij: %f" %dij_drivative)
            if (TargetMatrix[i][j] == 0):
                d_x = 0
                x_new = A[j][0]
                y_new = A[j][1]
                z_new = A[j][2]


            else:
                d_x = dij_drivative*(A[i][0] - A[j][0])*(1/TargetMatrix[i][j])
                x_new = A[i][0] - LearnRate * dij_drivative * (A[i][0] - A[j][0]) * (1 / TargetMatrix[i][j])
                y_new = A[i][1] - LearnRate * dij_drivative * (A[i][1] - A[j][1]) * (1 / TargetMatrix[i][j])
                z_new = A[i][2] - LearnRate * dij_drivative * (A[i][2] - A[j][2]) * (1 / TargetMatrix[i][j])

            #print(A[j])


            my_list.append(A[j])
            #A[j][0] = x_new
            #A[j][1] = y_new
            #A[j][2] = z_new
            #print(A[j])


        break


    i = 0
    with open('../Data/T0860/final_output.pdb', 'w') as result, open('../Data/T0860/target.pdb','r') as template:
        for line in template:
            temp_output = line.split()
            c = ' '
            #print str(line)
            if temp_output[4] == '1':
                result.write(str(line))
            elif temp_output[4] != '1' and temp_output[2] == 'CA':
                result.write('%s%7i  %-3s%c%s  %4i    %8.3f%8.3f%8.3f  %4s %2s\n' \
                             % (temp_output[0], int(temp_output[1]), temp_output[2], c, temp_output[3],
                                int(temp_output[4]), float(my_list[i][0])+.13,
                                float(my_list[i][1])-.11, float(my_list[i][2])-.15, temp_output[8],
                                temp_output[9]))
                i += 1
            else:
                result.write(str(line))





def Probability(dis, dis_template):
    sigma = .9;
    var = float(sigma)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    numerator = math.exp(-(float(dis)-float(dis_template))**2/(2*var))
    #print('Prob: %f' % (numerator/denom))
    return numerator/denom


def Atom_List(FileName):

    A = []
    for line in open(FileName):
        coordinateList = line.split()
        id = coordinateList[0]
        if id == 'ATOM':
            type = coordinateList[2]
            if type == 'CA':
                #print([float(coordinateList[5]),coordinateList[6], coordinateList[7]])
                A.append([float(coordinateList[5]),float( coordinateList[6]), float(coordinateList[7])])

    return A


def TargetDistanceMatrix(Atom_List):

    sizePoints = len(Atom_List)
    distMatrix = np.zeros((sizePoints, sizePoints))
    for i, eachFir in enumerate(Atom_List):
        for j, eachSec in enumerate(Atom_List):
                distMatrix[i][j] = PointDistance(eachFir, eachSec)

    return distMatrix


def loss():
    i = 1


Optimization()

