# imports
import random
from dna_toolkit import *

# generate random dna stride
rnd_dna_str = ''.join(random.choices(nucleotides, k=50))

# validate sequence
valid_dna_sequence = validate_sequence(rnd_dna_str)
print('valid dna sequence: ',valid_dna_sequence)

# count nucleotides
nucleotide_dict = count_nucleotides(valid_dna_sequence)
print('nucleotide dict: ',nucleotide_dict)
print('nucleotide values: ',*nucleotide_dict.values())