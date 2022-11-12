from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from table_models import DnaNucleotide, RnaNucleotide, RnaCodon, AminoAcid

engine = create_engine('sqlite:///project_database.db')
Session = sessionmaker(engine)

def return_rna_from_dna(dna_nuke: str) -> str:
    """Given a single DNA nucleotide, connects to the database
        and fetches the corresponding mRNA nucleotide"""
    with Session() as session:
        result = (session.query(RnaNucleotide).join(DnaNucleotide).filter(DnaNucleotide.base_name == dna_nuke))
        return result[0].base_name


def return_acid_from_codon(triplet: str) -> str:
    """Given a codon, connects to the database and fetches the
        corresponding amino acid"""
    with Session() as session:
        result = (session.query(AminoAcid).join(RnaCodon).filter(RnaCodon.codon_name == triplet))
        return result[0].acid_name

def convert_dna_to_rna(dna_strand: str) -> str:
    """
    convert_dna_to_rna(dna_strand: str) -> str
    returns a string representing mRNA from DNA single strand input.
    """
    raw_m_rna = []
    for nucleotide in dna_strand:
        raw_m_rna.append(return_rna_from_dna(nucleotide))
    return ''.join(raw_m_rna)


def convert_rna_to_protein(m_rna: str) -> str:
    """
    convert_rna_to_protein(m_rna: str) -> str
    returns a string representing amino chain from single mRNA input
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
        raw_protein.append(return_acid_from_codon(str_triplet))
        current_triplet.clear()
        current_index += 1

    return ''.join(raw_protein)


if __name__ == '__main__':
    engine = create_engine('sqlite:///project_database.db')
    Session = sessionmaker(engine)

    with Session() as session:
        result = (session.query(RnaNucleotide)
            .join(DnaNucleotide)
            .filter(DnaNucleotide.base_name == 'T').all()
        )
        for row in result:
            print(row.base_name)
        
        result = (session.query(AminoAcid).join(RnaCodon).filter(RnaCodon.codon_name == 'GGG'))
        for row in result:
            print(row.acid_name, row.acid_full_name)
    
    test_dna_strand = 'GCTAACTAAC'
    test_m_rna = convert_dna_to_rna(test_dna_strand)
    print(f'{test_dna_strand} ---> {test_m_rna}')
    print(test_m_rna == 'GCUAACUAAC')

    test_rna = 'CCCGUCCUUGAUUGGCUUGAAGAGAAGUUU'
    test_protein = convert_rna_to_protein(test_rna)
    print(f'{test_rna} ---> {test_protein}')
    print(test_protein == 'PVLDWLEEKF')