"""
Tables needed for DNA -> mRNA transcription and mRNA -> protein translation.
"""

transcription_table = {
    'A': 'A',
    'T': 'U',
    'G': 'G',
    'C': 'C',
}

translation_table = {
    'F': {'full_name': 'Phenylalanine', 'codons': ['UUU', 'UUC'],},
    'L': {'full_name': 'Leucine', 'codons': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],},
    'S': {'full_name': 'Serine', 'codons': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],},
    'Y': {'full_name': 'Tyrosine', 'codons': ['UAU', 'UAC'],},
    '.': {'full_name': 'Stop codon', 'codons': ['UAA', 'UAG', 'UGA'],},
    'C': {'full_name': 'Cysteine', 'codons': ['UGU', 'UGC'],},
    'W': {'full_name': 'Tryptophan', 'codons': ['UGG'],},
    'P': {'full_name': 'Proline', 'codons': ['CCU', 'CCC', 'CCA', 'CCG'],},
    'H': {'full_name': 'Histidine', 'codons': ['CAU', 'CAC'],},
    'Q': {'full_name': 'Glutamine', 'codons': ['CAA', 'CAG'],},
    'R': {'full_name': 'Arginine', 'codons': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],},
    'I': {'full_name': 'Isoleucine', 'codons': ['AUU', 'AUC', 'AUA'],},
    'M': {'full_name': 'Methionine', 'codons': ['AUG'],},
    'T': {'full_name': 'Threonine', 'codons': ['ACU', 'ACC', 'ACA', 'ACG'],},
    'N': {'full_name': 'Asparagine', 'codons': ['AAU', 'AAC'],},
    'K': {'full_name': 'Lysine', 'codons': ['AAA', 'AAG'],},
    'V': {'full_name': 'Valine', 'codons': ['GUU', 'GUC', 'GUA', 'GUG'],},
    'A': {'full_name': 'Alanine', 'codons': ['GCU', 'GCC', 'GCA', 'GCG'],},
    'D': {'full_name': 'Aspartic acid', 'codons': ['GAU', 'GAC'],},
    'E': {'full_name': 'Glutamic acid', 'codons': ['GAA', 'GAG'],},
    'G': {'full_name': 'Glycine', 'codons': ['GGU', 'GGC', 'GGA', 'GGG'],},
}