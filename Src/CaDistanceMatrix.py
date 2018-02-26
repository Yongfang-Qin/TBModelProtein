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
                A.append([float(coordinateList[6]), float(coordinateList[7]), float(coordinateList[8])])

    sizePoints = len(A)
    #print len(A)
    distMatrix = np.zeros((147, 147))
    for i, eachFir in enumerate(A):
        for j, eachSec in enumerate(A):

        #    print(i)
         #   print(j)
            if i in GapPosition:
                distMatrix[i][j] = 0
            if j in GapPosition:
                distMatrix[i][j] = 0
            else:
                distMatrix[i][j] = PointDistance(eachFir, eachSec)

    return distMatrix


def PointDistance(pointFir, pointSec):
    new_array = [(pointFir[0]-pointSec[0])**2,(pointFir[1]-pointSec[1])**2, (pointFir[2]-pointSec[2])**2]

    dist = math.sqrt(new_array[0]+new_array[1]+new_array[2])
    #dist = np.linalg.norm(new_array)

    #pointFir = np.array(pointFir)
    #pointSec = np.array(pointSec)
    #diff = abs(pointFir - pointSec)
    #dist_a = math.sqrt(sum(diff * diff.T))

    #a = diff(dist,dist_a)

    return dist