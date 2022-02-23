#!/usr/bin/env python


from collections import Counter


def count_all(itrbl):
    return dict(Counter(itrbl))


def main():
    print(count_all([1, 2, 3, 1]))
    print(count_all('hello'))
    print(count_all('#' * 10))


if __name__ == "__main__":
    main()
