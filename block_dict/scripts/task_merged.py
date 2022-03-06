#!/usr/bin/env python


from collections import defaultdict


def merged_t(*dicts):
    aggregate = defaultdict(set)
    for source in dicts:
        for key, value in source.items():
            aggregate[key].add(value)
    return aggregate


def merged(*dct):
    out_dct = dict()
    for item in dct:
        out_dct.update(item)
    for k in out_dct:
        s = set()
        for i in dct:
            if k in i:
                s.add(i[k])
        out_dct[k] = s
    return out_dct


def main():
    merged({'a': 1, 'b': 2}, {'b': 10, 'c': 100})


if __name__ == "__main__":
    main()
