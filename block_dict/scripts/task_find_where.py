#!/usr/bin/env python


books = [
    {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
    {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
    {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
    {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
    {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
    ]


def find_where(lst, dct):
    for item in lst:
        if set(dct.values()).issubset(set(item.values())):
            return item
    return None


def main():
    print(find_where(books, {}))


if __name__ == "__main__":
    main()
