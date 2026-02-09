import pygame
import random

sw, sh = 500, 500
ms = 5
fs = 72

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

colors = [YELLOW, MAGENTA, ORANGE, WHITE, BLUE, LIGHTBLUE, DARKBLUE]

pygame.init()
bg_i = pygame.transform.scale(pygame.image.load("background.png"), (sw, sh))
font = pygame.font.SysFont("Times New Roman", fs)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_c, y_c):
        self.rect.x = max(min(self.rect.x + x_c, sw - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_c, sh - self.rect.height), 0)

screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

def create_sprite():
    s = Sprite(random.choice(colors), 20, 30)
    s.rect.x = random.randint(0, sw - s.rect.width)
    s.rect.y = random.randint(0, sh - s.rect.height)
    all_sprites.add(s)
    return s

sprite1 = create_sprite()
sprite2 = create_sprite()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False

    keys = pygame.key.get_pressed()
    x_c = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * ms
    y_c = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * ms
    sprite1.move(x_c, y_c)

    if sprite1.rect.colliderect(sprite2.rect):
        all_sprites.remove(sprite1, sprite2)
        sprite1 = create_sprite()
        sprite2 = create_sprite()

    screen.blit(bg_i, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)

pygame.quit()