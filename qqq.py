import pygame

border = [0][0]


def sprite_rect(screen, cell):
    left = cell[1][0]
    top = cell[1][1]
    pygame.draw.rect(screen, (0, 0, 0),
                     ((left + border, top + border),
                      (border * 8, border * 3)),
                     border // 3)


class Entity:
    def __init__(self):
        pass

    def move(self):
        pass

    def chance(self):
        pass


class Enemy(Entity):
    pass


class Soldier(Entity):
    pass


class Menu:
    def __init__(self, w, h, le, t):
        self.wsize = border * 10
        self.hsize = border * 10
        self.width = w
        self.height = h
        self.left = le
        self.top = t
        self.color = (0, 100, 255)
        self.border = border // 3
        self.data = [[
            (0,
             (le + i * self.wsize, t + j * self.hsize)
             ) for i in range(self.width)] for j in range(self.height)]

    def render(self, screen):
        x = self.left - self.wsize
        y = self.top - self.hsize
        for i in range(self.width):
            x += self.wsize
            for j in range(self.height):
                y += self.hsize
                pygame.draw.rect(screen,
                                 self.color,
                                 ((x, y), (self.wsize, self.hsize)),
                                 self.border)
            y = self.top - self.hsize


class Table(Menu):
    pass


class Desk(Menu):
    def __init__(self, w, h, le, t):
        super(Desk, self).__init__(w, h, le, t)


wsize = border * 10
hsize = border * 10
width = 300
height = 500
left = [1][0]
top = [0][0]
border = border // 3
data = [[
    (0,
        (left + i * wsize, top + j * hsize)
        ) for i in range(width)] for j in range(height)]

