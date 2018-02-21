from Bio import SeqIO

for record in SeqIO.parse("Data/T0900_TargetSequence.fasta", "fasta"):
    target_sequence = record.seq

for record in SeqIO.parse("Data/5aot.fasta", "fasta"):
    template_sequence_1 = record.seq



