import time
import tkinter
from tkinter import messagebox
import pygame
import fightingLib
from fightingLib import *
import json
import os

# Initialize pygame
pygame.init()

# Set up the clock
clock = pygame.time.Clock()

# Import the config file
with open("retroFighter.cfg", "r") as infile: optionsDict = json.loads(infile.read())
resolution = optionsDict['Resolution']
resolutionList = resolution.split('x')
optionWidth = resolutionList[0]
optionHeight = resolutionList[1]

# Import the character data
with open("characters.cfg", "r") as infile: characterDict = json.loads(infile.read())

# Create the screen
screen = pygame.display.set_mode((int(optionWidth), int(optionHeight)))

# Title and Icon
pygame.display.set_caption("Finn Fighter")
icon = pygame.image.load(characterDict['spritePath'])

# Initialise the player
player = Player(200, 300, 64, 64)
player.sprite = pygame.image.load(characterDict['spritePath'])
player.sprite = pygame.transform.scale(player.sprite, (128, 128))

# Initialise the second player
enemy = Enemy(400, 300, 64, 64)
enemy.sprite = pygame.image.load(characterDict['spritePath'])
enemy.sprite = pygame.transform.scale(enemy.sprite, (128, 128))

# Initialise the health bars
healthBar = HealthBar(10, 10, 200, 20, 250)
playerHealthBar = HealthBar(400, 10, 200, 20, 250)


# Draw the ground for the game
def ground():
    pygame.draw.rect(screen, (0, 255, 100), (0, 425, 800, 200))


# Draw the background
def background():
    bg = pygame.image.load("bg.jpg")
    screen.blit(bg, (0, 0))


# Create a text splash for if the user wins or loses
def resultText(result):
    if result == "win":
        tkinter.Tk().wm_withdraw()
        messagebox.showinfo("You Win!")
    else:
        tkinter.Tk().wm_withdraw()
        messagebox.showinfo("You Lose!")


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    background()

    # Draw the ground
    ground()

    # Draw the player
    player.draw(screen)

    # Start the movement
    player.movement()

    # Update the player
    player.update(screen)

    # Make the player jump
    player.jump(player.isJump)

    player.punch(screen, characterDict['punchSpritePath'], characterDict['spritePath'])
    enemy.health = healthBar.health
    healthBar.update(screen)

    player.health = playerHealthBar.health
    playerHealthBar.update(screen)

    # Draw the enemy
    enemy.draw(screen)

    # Update the enemy
    enemy.update(screen)

    # Make the enemy move
    enemy.movement()

    # Check if the punch is colliding with the enemy
    if player.isPunch:
        if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[
            2]:
            if player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
                enemy.health -= int(characterDict["attack"])
                healthBar.health -= int(characterDict["attack"])
                print("Enemy Hit")
                enemy.knocked()

    # Check if the enemy punch is colliding with the player
    if enemy.isPunch:
        if enemy.hitbox[0] + enemy.hitbox[2] > enemy.hitbox[0] and enemy.hitbox[0] < player.hitbox[0] + player.hitbox[
            2]:
            if enemy.hitbox[1] + enemy.hitbox[3] > enemy.hitbox[1]:
                player.health -= 1
                playerHealthBar.health -= 1
                print("Player Hit")

    # Update the enemy if its punching
    enemy.punch(screen, characterDict['punchSpritePath'], characterDict['spritePath'])

    # End the game if the player dies
    if player.health <= 0:
        resultText("not win")
        running = False
        pygame.quit()
        os.system("py menu.py")
        print("Player Died")

    # End the game if the enemy dies
    if enemy.health <= 0:
        resultText("win")
        running = False
        pygame.quit()
        os.system("py menu.py")
        print("You Win")

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(45)
