#DNA Toolkit file


Ncleaotides = [ "A", "C", "G", "T" ]

#Check the sequence to make sure it is a DNA string
def vaildateSeq(dna_seq):
  tmpseq = dan_seq.upper()
  for nuc in tmpseq:
    if nuc in tempseq:
      if nuc not in Nucleotides:
        return False
  return tempseq
