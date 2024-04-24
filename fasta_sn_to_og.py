import sys

def fasta_outgroup(fastafile):
    with open(fastafile) as file:
        lines = []
        for line in file.readlines():
            line = line.rstrip("\n")
            if line.startswith(">"):
                words = line.split()
                species_name = line[1:]
                outgroup = words[-1]
                line = line.replace(species_name, outgroup)
            lines.append(line)

    with open(fastafile, 'w') as file:
        for line in lines:
            file.write(line + "\n")
        print(open(fastafile, 'r').read())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_sn_to_og.py {example.fasta}")
    else:
        fasta_outgroup(sys.argv[1])
import sys

def fasta_outgroup(fastafile):
    with open(fastafile) as file:
        lines = []
        for line in file.readlines():
            line = line.rstrip("\n")
            if line.startswith(">"):
                words = line.split()
                species_name = line[1:]
                outgroup = words[-1]
                line = line.replace(species_name, outgroup)
            lines.append(line)

    with open(fastafile, 'w') as file:
        for line in lines:
            file.write(line + "\n")
        print("File written with success!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_sn_to_og.py {example.fasta}")
    else:
        fasta_outgroup(sys.argv[1])
