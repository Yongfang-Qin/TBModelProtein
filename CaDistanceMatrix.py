import numpy as np
from Bio.Blast import NCBIWWW
import numpy as np
import math


def CaDistanceMatrix(FileName, GapPosition):
    A = []
    for line in open(FileName):
        coordinateList = line.split()
        id = coordinateList[0]
        if id == 'ATOM':
            type = coordinateList[2]
            if type == 'CA':
                id = coordinateList[1]
                residue = coordinateList[3]
                type_of_chain = coordinateList[4]
                atom_count = int(coordinateList[5])
                A.append([float(coordinateList[6]), coordinateList(list[7]), coordinateList(list[8])])

    sizePoints = len(A)
    distMatrix = np.zeros((sizePoints, sizePoints))
    for i, eachFir in enumerate(A):
        for j, eachSec in enumerate(A):
            if i in GapPosition:
                distMatrix[i][j] = 0
            if j in GapPosition:
                distMatrix[i][j] = 0
            else:
                distMatrix[i][j] = PointDistance(eachFir, eachSec)

    return distMatrix


def PointDistance(pointFir, pointSec):

    dist = np.linalg.norm(pointFir - pointSec)

    pointFir = np.array(pointFir)
    pointSec = np.array(pointSec)
    diff = abs(pointFir - pointSec)
    dist_a = math.sqrt(sum(diff * diff.T))

    a = diff(dist,dist_a)

    return dist