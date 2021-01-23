class Interrogator:
    def __init__(self, questions):
        self.questions = questions

    def __iter__(self):
        return self.questions.__iter__()


class Primes:
    def __init__(self):
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            current = self.current
            square_root = int(current ** 0.5)
            is_prime = True
            if square_root >= 2:
                for i in range(2, square_root + 1):
                    if current % i == 0:
                        is_prime = False
                        break
            self.current += 1
            if is_prime:
                return current


if __name__ == '__main__':
    qq = ["what?", "when?", "where?", "why?"]
    it = Interrogator(qq)

    for q in it:
        print(q)
    # infinite sequence
    # [print(p) for p in Primes() if p <= 100]
    # finite
    import itertools

    # Using the takewhile function to produce a finite sequence
    print([p for p in itertools.takewhile(lambda x: x < 100, Primes())])

    players = ['White', 'Black']
    turns = itertools.cycle(players)
    # 10 turns
    countdown = itertools.count(10, -1)
    print([turn for turn in itertools.takewhile(lambda x: next(countdown) > 0, turns)])
