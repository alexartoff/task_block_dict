#!/usr/bin/env python


dct_change = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna):
    out = ''
    for item in dna:
        for key in dct_change.keys():
            if item == key:
                out += dct_change[key]
    return out


def to_rna_t(dna):
    return ''.join(map(dct_change.get, dna))


def main():
    print(to_rna('ACGTGGTCTTAA'))


if __name__ == "__main__":
    main()
