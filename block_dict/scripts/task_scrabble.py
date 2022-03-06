#!/usr/bin/env python

from collections import Counter


def scrabble(charset, word):
    w = dict(Counter(word.lower()))
    ch = dict(Counter(charset.lower()))
    print(w, ch)
    if set(w.keys()).issubset(set(ch.keys())):
        for k in w:
            if w[k] > ch[k]:
                return False
        print(w.keys())
        return True
    return False


def main():
    print(scrabble('HahgdYyslghrupppp', 'hhhhhhappy'))


if __name__ == "__main__":
    main()
