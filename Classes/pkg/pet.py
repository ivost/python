class Pet():
    """
    A class to capture useful information regarding my pets, just incase
    I lose track of them.
    """

    owner = None

    @staticmethod
    def is_mine(pet):
        return "Ivo" in pet.owner

    def __init__(self, name, what, owner="Ivo"):
        self.name, self.what = name, what
        self.owner = owner

    def __str__(self):
        return self.name

    def info(self):
        s = f"{self.name} is {self.what} with owner: {self.owner}"
        return s


if __name__ == '__main__':
    dog = Pet("Fido", "dog", owner="Ivo")
    print(dog)
    print(Pet.is_mine(dog))
    cat = Pet("Kitty", "cat")
    print(cat)
    print(Pet.is_mine(cat))
    print(cat.__module__)
