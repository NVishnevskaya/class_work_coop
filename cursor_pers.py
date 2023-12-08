import os
import sys
import pygame
import random

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        # image = image.convert_alpha()
        pass
    return image


class Cursor(pygame.sprite.Sprite):
    image = load_image("cursor.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Cursor.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


all_sprites = pygame.sprite.Group()
running = True
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
cur = Cursor(all_sprites)
pygame.mouse.set_visible(not pygame.mouse.get_visible())
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
            cur.update_pos(*event.pos)
            screen.fill("black")
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
