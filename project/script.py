import sys

from data.db import transcription_query, translation_query
from gc_ratio.plotting import represent_gc_ratio


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


def cli_tool():
    def execute_command(command, input_str, file=False):
        if command == 'transcribe':
            print(convert_dna_to_rna(input_str))
        if command == 'translate':
            print(convert_rna_to_protein(input_str))
        if command == 'plot':
            plot_window = sys.argv[4] if file else sys.argv[3]
            represent_gc_ratio((input_str), int(plot_window))

    if sys.argv[1] == 'file':
        current_command = sys.argv[2]
        file_name = sys.argv[3]
        with open(f'data/inputs/{file_name}') as file:
            input_data = file.read()

        execute_command(current_command, input_data, file=True)
    else:
        current_command = sys.argv[1]
        input_data = sys.argv[2]

        execute_command(current_command, input_data)


if __name__ == '__main__':
    cli_tool()
