from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.table_models import DnaNucleotide, RnaNucleotide, RnaCodon, AminoAcid


engine = create_engine('sqlite:///project_database.db')
Session = sessionmaker(engine)


def transcription_query(dna_nuke: str) -> str:
    """Given a single DNA nucleotide, connects to the database
        and fetches the corresponding mRNA nucleotide"""
    with Session() as session:
        result = (
            session.query(RnaNucleotide)
            .join(DnaNucleotide)
            .filter(DnaNucleotide.base_name == dna_nuke)
        )
        return result[0].base_name


def translation_query(triplet: str) -> str:
    """Given a codon, connects to the database and fetches the
        corresponding amino acid"""
    with Session() as session:
        result = (
            session.query(AminoAcid)
            .join(RnaCodon)
            .filter(RnaCodon.codon_name == triplet)
        )
        return result[0].acid_name
