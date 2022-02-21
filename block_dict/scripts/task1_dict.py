#!/usr/bin/env python


def make_user(name, age):
    return {"name": name, "age": age}


def format_user(d):
    out = []
    for value in d.values():
        out.append(str(value))
    a, b = tuple(out)
    out = f'{a}, {b}'
    return out


def format_user_t(d):
    return f"{d['name']}, {d['age']}"


def main():
    user = make_user("Alex", 38)
    print(user)
    print(format_user(user))
    print(format_user_t(user))


if __name__ == "__main__":
    main()
