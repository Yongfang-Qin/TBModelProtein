import numpy as np

# def optimization(initStructure, matrix):

Atomlist = []

for line in open('Data/T0900_Target.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        type = list[2]
        if type == 'CA':
            position = list[6:9]
            Atomlist.append(position)

for x in xrange(1, len(Atomlist)):
    for y in xrange(x, len(Atomlist)):
        i=i+1



