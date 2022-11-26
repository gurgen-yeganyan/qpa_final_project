from data.db import create_database, transcription_query, translation_query


def convert_dna_to_rna(dna_strand: str) -> str:
    """
    convert_dna_to_rna(dna_strand: str) -> str
    returns a string representing mRNA from DNA single strand input.
    """
    raw_m_rna = []
    for nucleotide in dna_strand:
        raw_m_rna.append(transcription_query(nucleotide))
    return ''.join(raw_m_rna)


def convert_rna_to_protein(m_rna: str) -> str:
    """
    convert_rna_to_protein(m_rna: str) -> str
    returns a string representing amino acid chain from single mRNA input
    """
    raw_protein = []
    current_index = 0
    current_triplet = []

    while current_index < len(m_rna):
        current_triplet.append(m_rna[current_index])
        if (current_index+1) % 3:
            current_index += 1
            continue
        str_triplet = ''.join(current_triplet)
        raw_protein.append(translation_query(str_triplet))
        current_triplet.clear()
        current_index += 1

    return ''.join(raw_protein)


if __name__ == '__main__':
    create_database()
