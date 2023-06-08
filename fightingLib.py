import random
import pygame
import math


# Create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.punchCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True
        self.sprite = None
        self.movey = 0
        self.movex = 0
        self.isPunch = False
        self.right = False
        self.left = False
        self.flipped = True

        self.health = 100
        self.maxHealth = 100

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.movex = -self.vel
            self.left = True
            self.right = False
            if not self.flipped:
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.flipped = True
        elif keys[pygame.K_RIGHT]:
            self.movex = self.vel
            self.right = True
            self.left = False
            if self.flipped:
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.flipped = False
        else:
            self.movex = 0

    def jump(self, isJump):
        keys = pygame.key.get_pressed()
        # Make him jump
        if not isJump:
            if keys[pygame.K_UP]:
                self.isJump = True
        else:
            if self.jumpCount >= -10:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.jumpCount = 10
                self.isJump = False

    def update(self, screen):
        self.x += self.movex
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        if self.y > 500:
            self.y = 500
            self.movey = 0
        if self.x < 0:
            self.x = 0
        if self.x > 800 - self.width:
            self.x = 800 - self.width

    def punch(self, screen, punchSprite, sprite):
        keys = pygame.key.get_pressed()
        # Make him jump
        if not self.isPunch:
            if keys[pygame.K_p]:
                self.isPunch = True
        else:
            if self.punchCount >= -10:
                self.sprite = pygame.image.load(punchSprite)
                self.sprite = pygame.transform.scale(self.sprite, (128, 128))
                if self.flipped:
                    self.sprite = pygame.transform.flip(self.sprite, True, False)

                self.punchCount -= 1
            else:
                self.punchCount = 10
                self.isPunch = False
                self.sprite = pygame.image.load(sprite)
                self.sprite = pygame.transform.scale(self.sprite, (128, 128))

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))


# Create a class for an enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.right = None
        self.left = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True
        self.sprite = None
        self.movey = 0
        self.movex = 0
        self.flipped = True
        self.isPunch = False
        self.punchCount = 10
        self.isJump = False
        self.jumpCount = 10

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def update(self, screen):
        self.x += self.movex
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        if self.y > 500:
            self.y = 500
            self.movey = 0
        if self.x < 0:
            self.x = 0
        if self.x > 800 - self.width:
            self.x = 800 - self.width

    def movement(self):
        randomNumber = random.randint(1, 2)
        if randomNumber == 1:
            self.movex = -self.vel
            self.left = True
            self.right = False
            if not self.flipped:
                self.sprite = pygame.transform.flip(self.sprite, True, False)
                self.flipped = True
        elif randomNumber == 2:
            self.movex = self.vel
            self.right = True
            self.left = False
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.flipped = False
        else:
            self.movex = 0

    def punch(self, screen, punchSprite, sprite):
        keys = pygame.key.get_pressed()
        # Make him punch
        temp = random.randint(1, 100)
        if not self.isPunch:
            if temp == 1:
                self.isPunch = True
        else:
            if self.punchCount >= -10:
                self.sprite = pygame.image.load(punchSprite)
                self.sprite = pygame.transform.scale(self.sprite, (128, 128))
                if self.flipped:
                    self.sprite = pygame.transform.flip(self.sprite, True, False)

                self.punchCount -= 1
            else:
                self.punchCount = 10
                self.isPunch = False
                self.sprite = pygame.image.load(sprite)
                self.sprite = pygame.transform.scale(self.sprite, (128, 128))

    def knocked(self):
        knockCount = 5
        if knockCount >= -5:
            if self.right == True:
                self.x = self.x + 20
            else:
                self.x = self.x - 20
            knockCount -= 1
        else:
            knockCount = 5


# Create a class for a projectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), self.radius)


# Create a class for the health bars
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, maxHealth):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.color = (255, 0, 0)

    def draw(self, screen, health):
        if health < 0:
            health = 0
        self.health = health
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.y, self.width * (self.health / self.maxHealth), self.height))

    def update(self, screen):
        self.draw(screen, self.health)
