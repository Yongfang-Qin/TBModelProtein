from Bio.Blast import NCBIXML
from Bio import SeqIO


with open("../Data/T0860/T0860.fasta", "rU") as handle:
    for record in SeqIO.parse(handle,"fasta") :
        seq_len = len(record._seq)

result_handle = open('../Data/T0860/95SCU2B4015-Alignment.xml')
blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
    for alignment in blast_record.alignments:
        title = alignment.title
        length = alignment.length
        for hsp in alignment.hsps:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75])
            print(hsp.match[0:75])
            print(hsp.sbjct[0:75])

            identities=hsp.identities
            similarity=(100 * hsp.identities / seq_len)
            print(similarity)
            target=hsp.query
            targetstart=hsp.query_start
            templatestart = hsp.sbjct_start
            match=hsp.match
            template=hsp.sbjct[0:137]
            print(template)
            print(len(template))
            templatestart=hsp.sbjct_start

            if similarity!=100 and similarity > 70:

                with open('../Data/T0860/T0860_target.pdb', 'r') as targetFile, \
                        open('../Data/T0860/5fld.pdb', 'r') as templateFile, \
                        open('../Data/T0860/results.pdb','r') as outputFile, \
                        open('../Data/T0860/results_init.pdb', 'w') as output_initFile:

                    #for template_line in templateFile:
                    #   temp_output = template_line.split()
                    #   id = temp_output[0]
                    #  if id == 'ATOM':
                    #     outputFile.write('\t'.join(temp_output) + '\n')

                    i = 0
                    for template_line,line in zip(outputFile,targetFile):
                        out = template_line.split()
                        target = line.split()
                        i = int(target[5])
                        if template[i] != '-':
                            target[6]= out[6]
                            target[7]= out[7]
                            target[8] = out[8]
                            target[9] = out[9]
                            target[10] = out[10]
                            output_initFile.write('\t'.join(target) + '\n')
                        else:
                            target[6] = '0'
                            target[7] = '0'
                            target[8] = '0'
                            target[9] = '0'
                            target[10] = '0'
                            output_initFile.write('\t'.join(target) + '\n')




