import matplotlib.pyplot as plt


def represent_gc_ratio(string: str, step: int) -> None:
    """"
    Calculates the GC ratio for the given DNA sequence(string)
    for (step) number of windows, saves the resulting plot
    in a .png file.
    """
    def gc_count(string: str) -> int:
        raw_count = (string.count('G') + string.count('C')) / len(string)
        return round(raw_count * 100)

    distribution = []
    for chunk_start in range(0, len(string)-step + 1, step):
        chunk_end = chunk_start + step
        chunk = string[chunk_start:chunk_end]
        distribution.append(gc_count(chunk))

    genome_positions = [(window+1)
                        * step for window in range(len(distribution))
                        ]

    plt.plot(genome_positions, distribution)
    plt.title('GC-content distribution')
    plt.xlabel('Genome position')
    plt.ylabel('GC-content(%)')
    plt.savefig('GC_ratio.png')


if __name__ == '__main__':
    dna = ''
    with open('covid_dna.txt', 'r') as file:
        dna = file.read()

    represent_gc_ratio(dna, 100)
