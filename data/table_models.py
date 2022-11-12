from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class DnaNucleotide(Base):
    __tablename__ = 'dna_nucleotides'

    def __str__(self):
        return f'{self.nucleotide_id}: {self.base_name} ---> {self.child_rna}'

    nucleotide_id = Column(Integer, primary_key = True)
    base_name = Column(String(1))
    child_rna = relationship('RnaNucleotide', back_populates='parent_dna')
    rna_id = Column(Integer, ForeignKey('rna_nucleotides.nucleotide_id'))


class RnaNucleotide(Base):
    __tablename__ = 'rna_nucleotides'

    def __str__(self):
        return f'{self.nucleotide_id}: {self.base_name}'

    nucleotide_id = Column(Integer, primary_key = True)
    base_name = Column(String(1))
    parent_dna = relationship('DnaNucleotide', back_populates='child_rna')


class RnaCodon(Base):
    __tablename__ = 'rna_codons'

    def __str__(self):
        return f'{self.codon_id}: {self.codon_name} ---> {self.amino_acid}'
    
    codon_id = Column(Integer, primary_key=True)
    codon_name = Column(String(3))
    amino_acid = relationship('AminoAcid', back_populates='rna_codon')
    acid_id = Column(Integer, ForeignKey('amino_acids.acid_id'))


class AminoAcid(Base):
    __tablename__ = 'amino_acids'

    def __str__(self):
        return f'{self.acid_id}: {self.acid_name}({self.acid_full_name})'

    acid_id = Column(Integer, primary_key=True)
    acid_name = Column(String(1))
    acid_full_name = Column(String(30))
    rna_codon = relationship('RnaCodon', back_populates='amino_acid')