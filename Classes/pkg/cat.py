from pkg.pet import Pet


class Cat(Pet):

    def __init__(self, name):
        # self.name, self.what = name, "Cat"
        super().__init__(name, "Cat")


if __name__ == '__main__':
    cat = Cat("Kitty")
    print(cat, "is mine:", Pet.is_mine(cat))
