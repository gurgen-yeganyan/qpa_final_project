"""
Creates a database used for DNA to mRNA transcription
and mRNA to protein translation.
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from table_models import DnaNucleotide, RnaNucleotide, RnaCodon, AminoAcid
from table_models import Base
from conversion_tables import transcription_table
from conversion_tables import translation_table


engine = create_engine('sqlite:///project_database.db', echo = True)
metadata_obj = MetaData()
Base.metadata.create_all(engine)
Session = sessionmaker(engine)

with Session() as session:
    for nuke in transcription_table:
        rna_nuke = RnaNucleotide(base_name=transcription_table[nuke])
        dna_nuke = DnaNucleotide(base_name=nuke, child_rna = rna_nuke)
        session.add(dna_nuke)
    session.commit()
    
    for acid in translation_table:
        name = acid
        full_name = translation_table[acid]['full_name']
        new_acid = AminoAcid(acid_name=name, acid_full_name=full_name)
        codons = translation_table[acid]['codons']
        for codon in codons:
            new_codon = RnaCodon(codon_name = codon, amino_acid = new_acid)
        session.add(new_codon)
    session.commit()


if __name__ == '__main__':
    with Session() as session:
        for nuke_test in session.query(DnaNucleotide).all():
            print(nuke_test)
        print('==' * 60)

        for codon_test in session.query(RnaCodon).all():
            print(codon_test)
        print('==' * 60)
        
        for acid_test in session.query(AminoAcid).all():
            print(acid_test)
