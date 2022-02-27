#!/usr/bin/env python


from collections import Counter


def to_rna(dna):
    out = ''
    dct_change = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for item in dna:
        for key in dct_change.keys():
            if item == key:
                out += dct_change[key]
    return out


def main():
    print(to_rna('ACGTGGTCTTAA'))


if __name__ == "__main__":
    main()
