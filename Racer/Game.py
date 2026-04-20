import pygame
import sys
import random
from pygame.locals import *

# INIT
pygame.init()
pygame.mixer.init()

# GAME SETTINGS
FPS = 60
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

ROAD_LEFT = 40
ROAD_RIGHT = SCREEN_WIDTH - 40

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

game_over_text = font_big.render("Game Over", True, BLACK)

# DISPLAY
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# LOAD IMAGES
background = pygame.image.load("AnimatedStreet.png")
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")
coin_img = pygame.image.load("coin.png")

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

        # If enemy goes off screen → increase score and reset
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # Move left
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # Move right
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

# COIN CLASS
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(coin_img, (30, 30))
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Spawn coin at random position above screen
        self.rect.center = (
            random.randint(ROAD_LEFT, ROAD_RIGHT),
            random.randint(-600, -50)
        )

    def move(self):
        self.rect.move_ip(0, SPEED)

        # Reset if coin leaves screen
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

# CREATE OBJECTS
P1 = Player()
E1 = Enemy()
coin1 = Coin()
coin2 = Coin()

# GROUPS
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(coin1, coin2)

all_sprites = pygame.sprite.Group(P1, E1, coin1, coin2)

# EVENT: increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# GAME LOOP
running = True
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Increase speed every second
        if event.type == INC_SPEED:
            SPEED += 0.5

    # DRAW BACKGROUND
    DISPLAYSURF.blit(background, (0, 0))

    # DRAW SCORE (top-left)
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # DRAW COINS (top-right)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    coin_rect = coin_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    DISPLAYSURF.blit(coin_text, coin_rect)

    # MOVE & DRAW OBJECTS
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # CHECK COIN COLLISION
    collected = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected:
        COINS_COLLECTED += 1
        coin.reset_position()

    # CHECK ENEMY COLLISION
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()

        DISPLAYSURF.fill((255, 0, 0))
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()

        pygame.time.delay(2000)
        running = False

    pygame.display.update()
    FramePerSec.tick(FPS)

# EXIT
pygame.quit()
sys.exit()