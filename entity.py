class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
        if self.x > 9:
            self.x = 9

        elif self.x < 0:
            self.x = 0

        if self.y > 9:
            self.y = 9

        elif self.y < 0:
            self.y = 0

    def get_pos(self):
        return self.x, self.y


class Tiger(Entity):
    def __init__(self, x, y):
        super(Tiger, self).__init__(x, y)


class Rabbit(Entity):
    def __init__(self, x, y):
        super(Rabbit, self).__init__(x, y)
        self.alive = True

    def dead(self):
        self.alive = False


class Enemy(Entity):
    def __init__(self, x, y):
        super(Enemy, self).__init__(x, y)

