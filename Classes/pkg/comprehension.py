def games(names):
    return [f"{a} vs {b}" for a in names for b in names if a < b]


if __name__ == '__main__':
    names = ["Ivo", "Nina", "Victor"]
    print(games(names))

    # list
    print([a + b for a in [0, 1, 2, 3] for b in [4, 3, 2, 1]])
    # set
    print({a + b for a in [0, 1, 2, 3] for b in [4, 3, 2, 1]})
    # disctionary
    d = {k: len(k) for k in names}
    print(d)