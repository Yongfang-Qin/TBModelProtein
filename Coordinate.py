import numpy as np
from Bio.Blast import NCBIWWW

for line in open('TemplateBest.pdb'):
    list = line.split()
    id = list[0]
    if id == 'ATOM':
        type = list[2]
        if type == 'CA':
            id = list[1]
            residue = list[3]
            type_of_chain = list[4]
            atom_count = int(list[5])
            position = list[6:9]
            print(id)
            print(position)





