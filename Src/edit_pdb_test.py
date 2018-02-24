with open('../Data/T0900_Target.pdb', 'r') as inputFile, open('../Data/updated_file.pdb', 'w') as outputFile:
    for line in inputFile:
        atom = line.split()

        if atom[2] == 'CA':
            atom[6],atom[7],atom[8], atom[9], atom[10] =  '   \t33.00', '44.00', '55.00', '101','23.0'
            outputFile.write('\t'.join(atom)+'\n')
        else:
            outputFile.write(line)

