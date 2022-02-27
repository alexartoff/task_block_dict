#!/usr/bin/env python


def diff_keys(dct_old, dct_new):
    output = dict()
    output['kept'] = set(dct_old) & set(dct_new)
    output['added'] = set(dct_new) - set(dct_old)
    output['removed'] = set(dct_old) - set(dct_new)
    return output


def main():
    print(diff_keys({'name': 'Bob', 'age': 42}, {}))
    print(diff_keys({'x': 100, 'y': 200, 'z': 105}, {'x': 100, 'y': 200, 'velocity': 2.5}))


if __name__ == "__main__":
    main()
