import pygame, random
pygame.init()

from Block import Block
from Screen import Screen

win = pygame.display.set_mode((100, 400))
pygame.display.set_caption("Rain of blocks")

#pygame.key.set_repeat(0)

activeBlock = Block(win, random, pygame)
activeBlock.createNew()
screen = Screen(pygame, win)

running = True


while running:
    # speed of the game
    pygame.time.delay(100)
    key = "down"
    # check exit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            # check exit via space key
            if event.key == pygame.K_SPACE:
                running = False
                break

            # move the block
            if event.key == pygame.K_RIGHT:
                activeBlock.move("right")
                key = "right"
            elif event.key == pygame.K_LEFT:
                activeBlock.move("left")
                key = "left"
            elif event.key == pygame.K_DOWN:
                activeBlock.move("down")
                key = "down"
            elif event.key == pygame.K_UP:
                activeBlock.rotate()

    activeBlock.move()

    # check if we need to create a new block
    if screen.detectingCollision(activeBlock) == "Bottom reached":
        screen.addBlock(activeBlock)
        activeBlock.createNew()

    # check if we need to create a new block
    elif screen.detectingCollision(activeBlock) == "Set back":
        activeBlock.setBack(key)
        if key == "down":
            screen.addBlock(activeBlock)
            activeBlock.createNew()

    activeBlock.draw()
    screen.drawBottom()


    pygame.display.update()