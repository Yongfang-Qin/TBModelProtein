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
            target=hsp.query
            targetstart=hsp.query_start
            templatestart = hsp.sbjct_start
            match=hsp.match
            template=hsp.sbjct[0:75]
            templatestart=hsp.sbjct_start

            if similarity!=100:

                with open('../Data/T0860/T0860_target.pdb', 'r') as targetFile, \
                        open('../Data/T0860/5fld.pdb', 'r') as templateFile, \
                        open('../Data/T0860/results.pdb', 'w') as outputFile, \
                        open('../Data/T0860/results_init.pdb', 'w') as output_initFile:

                    for template_line in templateFile:
                        temp_output = template_line.split()
                        id = temp_output[0]
                        if id == 'ATOM':
                            outputFile.write('\t'.join(temp_output) + '\n')



