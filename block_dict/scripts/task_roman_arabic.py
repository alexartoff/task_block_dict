#!/usr/bin/env python


A2R = {
    '1': 'I',
    '4': 'IV',
    '5': 'V',
    '9': 'IX',
    '10': 'X',
    '40': 'XL',
    '50': 'L',
    '90': 'XC',
    '100': 'C',
    '400': 'CD',
    '500': 'D',
    '900': 'CM',
    '1000': 'M'
}


def to_roman(arabic):
    if arabic == 0:
        return ''
    d_length = len(str(arabic))
    d_lst, res_str = [], ''
    for i, d in enumerate(str(arabic)):
        d_lst.append(f'{d}{"0" * (d_length - i - 1)}')
    for d in d_lst:
        if d in A2R:
            res_str += f'{A2R[d]}'
        elif int(d[0]) < 4:
            res_str += f'{A2R["1" + d[1:]] * int(d[0])}'
        elif int(d[0]) > 5 and int(d[0]) < 9:
            res_str += f'{A2R["5" + d[1:]]}{A2R["1" + d[1:]] * (int(d[0]) - 5)}'
    return res_str


def reverce_dict(dct):
    reversed_dict = {}
    for key, val in dct.items():
        reversed_dict[val] = key
    return reversed_dict


def is_rule_1_pass(lst):
    ''' tail: 0..3 symbols I '''
    cnt, tmp = 0, lst[:]
    while cnt < 4:
        if tmp[-1] == '1':
            tmp.pop(-1)
            cnt += 1
        else:
            break
    else:
        return 0
    return 1


def is_rule_2_pass(lst):
    ''' sequence '''
    # TODO - make rule
    if lst == 'VX':
        return 0
    return 1


def make_calc(rom_str):
    lst, result = [], 0
    cplst = list(rom_str).copy()
    r2a = reverce_dict(A2R)
    if len(cplst) == 1 and cplst[0] in r2a:
        result = int(r2a[cplst[0]])
        return result
    while cplst:
        if len(cplst) >= 2 and (cplst[0] + cplst[1]) in r2a:
            lst.append(cplst[0] + cplst[1])
            cplst.pop(0)
            cplst.pop(0)
        elif cplst[0] in r2a:
            lst.append(cplst[0])
            cplst.pop(0)
    for item in lst:
        result += int(r2a[item])
    return result


def to_arabic(roman):
    if roman == '':
        return 0
    rules_pass = is_rule_1_pass(roman) * is_rule_2_pass(roman)
    if rules_pass:
        res = make_calc(roman)
        return res
    return False


def main():
    number = 44
    number_rome = 'V'
    if number == to_arabic(to_roman(number)):
        print('a_Correct')
    if number_rome == to_roman(to_arabic(number_rome)):
        print('r_Correct')


if __name__ == "__main__":
    main()
