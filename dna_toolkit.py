from collections import Counter
# nucloetides set
nucleotides = ["A", "C", "G", "T"]

# validate dna sequence
def validate_sequence(dna_sequence):
    return dna_sequence if set(dna_sequence.upper()).issubset(nucleotides) else False


def count_nucleotides(dna_sequence):
    # count nucleotides
    return Counter(dna_sequence)