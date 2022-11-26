"""
Create and access a database used for DNA to mRNA transcription
and mRNA to protein translation.
"""

from os import path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.table_models import DnaNucleotide, RnaNucleotide, RnaCodon, AminoAcid
from data.table_models import Base
from data.conversion_tables import transcription_table, translation_table


ENGINE = create_engine('sqlite:///project_database.db')
SESSION = sessionmaker(ENGINE)


def create_database() -> None:
    if path.isfile('project_database.db'):
        return

    Base.metadata.create_all(ENGINE)
    with SESSION() as session:
        for nuke in transcription_table:
            rna_nuke = RnaNucleotide(base_name=transcription_table[nuke])
            dna_nuke = DnaNucleotide(base_name=nuke, child_rna=rna_nuke)
            session.add(dna_nuke)
        session.commit()

        for acid in translation_table:
            full_name = translation_table[acid]['full_name']
            new_acid = AminoAcid(acid_name=acid, acid_full_name=full_name)
            codons = translation_table[acid]['codons']
            for codon in codons:
                new_codon = RnaCodon(codon_name=codon, amino_acid=new_acid)
            session.add(new_codon)
        session.commit()


def transcription_query(dna_nuke: str) -> str:
    """Given a single DNA nucleotide, connects to the database
        and fetches the corresponding mRNA nucleotide"""
    with SESSION() as session:
        result = (
            session.query(RnaNucleotide)
            .join(DnaNucleotide)
            .filter(DnaNucleotide.base_name == dna_nuke)
        )
        return result[0].base_name


def translation_query(triplet: str) -> str:
    """Given a codon, connects to the database and fetches the
        corresponding amino acid"""
    with SESSION() as session:
        result = (
            session.query(AminoAcid)
            .join(RnaCodon)
            .filter(RnaCodon.codon_name == triplet)
        )
        return result[0].acid_name
