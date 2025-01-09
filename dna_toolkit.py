from collections import Counter
# nucloetides set
nucleotides = ["A", "C", "G", "T"]


'''
# validate dna sequence
def validate_sequence(dna_sequence):
    return dna_sequence if set(dna_sequence.upper()).issubset(nucleotides) else False


def count_nucleotides(dna_sequence):
    # count nucleotides
    return dict(Counter(dna_sequence))
'''

# validate dna sequence
def validate_sequence(dna_sequence):
    dna_sequence = dna_sequence.upper()
    for nucleotide in dna_sequence:
        if nucleotide not in nucleotides:
            return False
    return dna_sequence


def count_nucleotides(dna_sequence):
    # count nucleotides
    dna_seq_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in dna_sequence:
        dna_seq_dict[nucleotide] += 1
    return dna_seq_dict