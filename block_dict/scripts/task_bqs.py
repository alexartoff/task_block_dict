#!/usr/bin/env python


def build_query_string(dct):
    out = ''
    lst = sorted(dct, key=str)
    for item in lst:
        out += f"{item}={dct[item]}&"
    return out[:-1]


def main():
    print(build_query_string({'a': 10, 's': 'Wow', 'd': 3.2, 'z': '89',}))


if __name__ == "__main__":
    main()
