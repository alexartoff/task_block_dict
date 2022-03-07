#!/usr/bin/env python


def gen_diff_t(data1, data2):
    keys = data1.keys() | data2.keys()  # https://youtu.be/vkUTX1hruF8?t=929
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = 'added'
        elif key not in data2:
            result[key] = 'deleted'
        elif data1[key] == data2[key]:
            result[key] = 'unchanged'
        else:
            result[key] = 'changed'
    return result


def gen_diff(first, second):
    out_dct, lst = dict(), list()
    lst.append(first)
    lst.append(second)
    for item in lst:
        out_dct.update(item)
    for k in out_dct:
        if k in first and k in second:
            if first[k] == second[k]:
                out_dct[k] = 'unchanged'
            else:
                out_dct[k] = 'changed'
        elif k in first and k not in second:
            out_dct[k] = 'deleted'
        elif k not in first and k in second:
            out_dct[k] = 'added'
    # print(out_dct)
    return out_dct


def main():
    gen_diff({'a': 1, 'b': 2}, {'b': 10, 'c': 100})


if __name__ == "__main__":
    main()
