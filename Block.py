from BlockI import BlockI
from BlockO import BlockO
from BlockT import BlockT
from BlockS import BlockS
from BlockJ import BlockJ
from BlockZ import BlockZ
from BlockL import BlockL
from Tile import Tile

class Block:
    x = 0
    y = 0
    speed = 10
    screenWidth = 0
    screenHeight = 0
    blockTypes = [BlockI(), BlockO(), BlockS(), BlockZ(), BlockT(), BlockL(), BlockJ()]
    tiles = []
    direction = "down"
    totalWidth = 0
    totalHeight = 0


    def __init__(self, win, random, pygame):
        self.pygame = pygame
        self.win = win
        self.random = random
        self.screenWidth, self.screenHeight = self.pygame.display.get_surface().get_size()

    def createNew(self):
        self.activeBlock = self.random.choice(self.blockTypes)

        self.x = (self.random.randrange(0, (self.screenWidth - self.activeBlock.width) / 10)) * 10
        self.y = 0
        self.activeBlock.stand = 0
        tempY = self.y
        tempX = self.x
        self.tiles.clear()
        counting = 1

        for i in range(len(self.activeBlock.position)):
            for i2 in range(len(self.activeBlock.position[i])):
                if self.activeBlock.position[i][i2] == 1:
                    if counting == 1:
                        tile1 = Tile()
                        tile1.x = tempX
                        tile1.y = tempY
                        self.tiles.append(tile1)
                    elif counting == 2:
                        tile2 = Tile()
                        tile2.x = tempX
                        tile2.y = tempY
                        self.tiles.append(tile2)
                    elif counting == 3:
                        tile3 = Tile()
                        tile3.x = tempX
                        tile3.y = tempY
                        self.tiles.append(tile3)
                    elif counting == 4:
                        tile4 = Tile()
                        tile4.x = tempX
                        tile4.y = tempY
                        self.tiles.append(tile4)
                    counting += 1
                tempX += 10
            tempX = self.x
            tempY += 10


    def move(self, direction="down"):
        self.direction = direction
        if self.direction == "down":
            self.y += self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].y += self.speed
        elif self.direction == "right" and self.x < self.screenWidth - self.activeBlock.width:
            self.x += self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].x += self.speed
        elif self.direction == "left" and self.x > 0:
            self.x -= self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].x -= self.speed

    def setBack(self, direction="down"):
        if direction == "right":
            self.x -= self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].x -= self.speed
        elif direction == "left":
            self.x += self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].x += self.speed
        else:
            self.y -= self.speed
            for i in range(len(self.tiles)):
                self.tiles[i].y -= self.speed

    def rotate(self):
        self.activeBlock.rotate()
        print(self.activeBlock.stand)

    def draw(self):
        self.win.fill((0, 0, 0))
        tempX = self.x
        tempY = self.y

        for i in range(len(self.activeBlock.position)):
            for i2 in range(len(self.activeBlock.position[i])):
                if self.activeBlock.position[i][i2] == 1:
                    self.pygame.draw.rect(self.win, self.activeBlock.color, (tempX, tempY, self.tiles[0].width, self.tiles[0].height))
                tempX += self.tiles[0].width
            tempX = self.x
            tempY += self.tiles[0].height

