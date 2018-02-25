with open('../Data/T0860/T0860_target.pdb', 'r') as targetFile, \
        open('../Data/T0860/results.pdb', 'r') as templateFile, \
        open('../Data/T0860/results_init.pdb', 'w') as outputFile:

    i = 0
    for template_line in templateFile:
        i = i + 1
        temp_output = template_line.split()


        outputFile.write('\t'.join(temp_output) + '\n')





