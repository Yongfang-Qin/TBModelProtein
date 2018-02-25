with open('../Data/1a40.pdb', 'r') as targetFile, open('../Data/1ixi.pdb', 'r') as templateFile, open('../Data/results.pdb', 'w') as outFile:
    # for line in inputFile:
    #     atom = line.split()
    #
    #     if atom[2] == 'CA':
    #         atom[6],atom[7],atom[8], atom[9], atom[10] =  '   \t33.00', '44.00', '55.00', '101','23.0'
    #         outputFile.write('\t'.join(atom)+'\n')
    #     else:
    #         outputFile.write(line)


    target_data = list()
    template_data = list()
    total_lenght = 0
    # getting data from target file
    for line in targetFile:
        out_data = line.split()
        if len(out_data) > 3 and out_data[0] == 'ATOM' and out_data[2] == 'CA':
            target_data.append(out_data)
            total_lenght += 1


    print(total_lenght)

    #getting data in template file
    for line in templateFile:
        out_data = line.split()
        if len(out_data) > 3 and out_data[0] == 'ATOM' and out_data[2] == 'CA':
            template_data.append(out_data)
    current_length = 0
    
    for line1, line2 in zip(target_data, template_data):
        if current_length < total_lenght:
            if line1[3] == line2[3]:
                outFile.write('\t'.join(line1)+'\n')
            else:
                outFile.write('Data dosen\'t match\n')
        current_length += 1
