import numpy as np
from scipy import stats
from CaDistanceMatrix import PointDistance
import math

def Optimization():

    A = Atom_List('T0900_Target.pdb')
    TemplateMatrix_1 = []
    TemplateMatrix_2 = []
    TargetMatrix = []
    weights = []
    sigma = 0.1
    LearnRate = 0.01

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
            d_x = dij_drivative*(A[i][0] - A[j][0])*(1/TargetMatrix[i][j])

            x_new = A[i][0]-LearnRate*dij_drivative*(A[i][0] - A[j][0])*(1/TargetMatrix[i][j])
            y_new = A[i][1]-LearnRate*dij_drivative*(A[i][1] - A[j][1])*(1/TargetMatrix[i][j])
            z_new = A[i][2]-LearnRate*dij_drivative*(A[i][2] - A[j][2])*(1/TargetMatrix[i][j])

            A[i][0] = x_new
            A[i][1] = y_new
            A[i][2] = z_new
                


def Probability(dis, dis_template):
    sigma = 0.1;
    prob = stats.norm.pdf(dis, dis_template, sigma)
    return prob


def Atom_List(FileName):

    A = []
    for line in open(FileName):
        coordinateList = line.split()
        id = coordinateList[0]
        if id == 'ATOM':
            type = coordinateList[2]
            if type == 'CA':
                A.append([float(coordinateList[6]), coordinateList(list[7]), coordinateList(list[8])])

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


