with open('../Data/T0860/results_init.pdb', 'r') as template, \
        open('../Data/T0860/target.pdb', 'w') as outputFile:
    for template_line in template:
        temp_output = template_line.split()
        id = temp_output[0]
        if id == 'ATOM':
            c = ' '
            if len(temp_output[3]) == 4:
                c = temp_output[3][0]
                temp_output[3] = ''.join([temp_output[3][1], temp_output[3][2], temp_output[3][3]])

            outputFile.write('%s%7i  %-3s%c%s  %4i    %8.3f%8.3f%8.3f  %4s %2s\n' \
                             % (temp_output[0], int(temp_output[1]), temp_output[2], c, temp_output[3],
                                int(temp_output[4]), float(temp_output[5])-.0003,
                                float(temp_output[6])-.0002, float(temp_output[7])-.0001, temp_output[9],
                                temp_output[10]))