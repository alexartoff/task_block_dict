#!/usr/bin/env python


from collections import Counter


def all_unique(itrbl):
    dct = dict(Counter(itrbl))
    # st = set(Counter(itrbl))
    # print(st, len(st), len(dct), len(itrbl)) # all uniq items
    for val in dct.values():
        if val > 1:
            return False
    return True


def all_unique_t(iterable):
    items = list(iterable)
    return len(items) == len(set(items))


def main():
    print(all_unique([1, 2, 3, 1]))
    print(all_unique('hello'))
    print(all_unique([]))


if __name__ == "__main__":
    main()
