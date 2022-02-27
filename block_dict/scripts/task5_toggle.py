#!/usr/bin/env python


def toggle(flg, st):
    if flg in st:
        st.discard(flg)
    else:
        st.add(flg)


def toggled(flg, st):
    new_st = st.copy()
    toggle(flg, new_st)
    return new_st


def main():
    print(toggle('r', {'-', 'r', 'w', 'e'}))
    print(toggled('r', {'-', 'r', 'w', 'e'}))


if __name__ == "__main__":
    main()
