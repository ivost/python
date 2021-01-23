class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last


if __name__ == '__main__':
    p = Person("Ivo", "Stoyanov")
    print(p.first_name, p.last_name)
    print(p.full_name)
    p.full_name = "John Doe"
    print(p.full_name)
