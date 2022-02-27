#!/usr/bin/env python


def apply_diff(st, dct):
    for key in dct.keys():
        if key == 'add':
            st.update(dct['add'])
        elif key == 'remove':
            st.difference_update(dct['remove'])
    # print(st)


def main():
    apply_diff({'a', 'b'}, {'add': {'c'}, 'remove': {'a'}})


if __name__ == "__main__":
    main()
