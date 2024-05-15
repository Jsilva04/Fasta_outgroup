import sys

def fasta_outgroup(fastafile):
    with open(fastafile) as file:
        lines = []
        for line in file.readlines():
            line = line.rstrip("\n")
            if line.startswith(">"):
                words = line.split()
                species_name = "_".join(words[1:3])
                line = ">" + species_name
            lines.append(line)


    for line in lines:
        print(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_sn_to_og.py {example.fasta}")
    else:
        fasta_outgroup(sys.argv[1])