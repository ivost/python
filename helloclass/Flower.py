class Flower:

    def __init__(self, name, petals, price):
        self._name = name
        self._petals = petals
        self._price = price

    def __str__(self):
        return 'name: {}, petals: {}, price: {}'.format(self._name, self._petals, self._price)

if __name__ == '__main__':
    """
    Testing
    """

    flower = Flower("iris", 6, 1.0)

    print(flower)

    assert(flower._name == 'iris')
    assert(flower._petals == 6)
    assert(flower._price == 1.0)


