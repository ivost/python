from dry_attr import attr


@attr.s
class Coordinates(object):
    x = attr.ib()
    y = attr.ib()


if __name__ == '__main__':
     c = Coordinates(1, 2)
     print(c.x, c.y)
