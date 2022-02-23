#!/usr/bin/env python


from collections import defaultdict


def collect_indexes(itrbl):
    it = iter(itrbl)
    out = defaultdict(list)
    count = 0
    while True:
        try:
            out[next(it)].append(count)
            count += 1
        except StopIteration:
            break
    # print(len(it), next(it), next(it), next(it))
    # for i in it:
    #     out[i].append(it.index(i))

    return dict(out)


def main():
    print(collect_indexes([1, 2, 3, 1]))
    print(collect_indexes('hello'))


if __name__ == "__main__":
    main()
