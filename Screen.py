class Screen:
    positionBlocks = [[0 for x in range(10)] for y in range(41)]

    def __init__(self, pygame, win):
        #set consts
        self.pygame = pygame
        self.win = win
        self.screenWidth, self.screenHeight = self.pygame.display.get_surface().get_size()
        #make array for detecting collision
        for i in range(41):
            for i2 in range(10):
                self.positionBlocks[i][i2] = 0

    def draw(self):
        self.test = 0

    def addBlock(self, activeBlock):
        blockArray = activeBlock.activeBlock.position
        counting = 0
        print(blockArray)
        for i in range(len(blockArray)):
            for i2 in range(len(blockArray[i])):
                if blockArray[i][i2] != 0:
                    yTemp = int(activeBlock.tiles[counting].y / 10)
                    xTemp = int(activeBlock.tiles[counting].x / 10)
                    self.positionBlocks[yTemp][xTemp] = activeBlock.activeBlock.color
                    counting += 1


    def detectingCollision(self, activeBlock):
        tempHeight = activeBlock.activeBlock.height - 10

        if activeBlock.y == self.screenHeight - tempHeight:
            self.addBlock(activeBlock)
            return "Bottom reached"

        for i in range(4):
            if self.positionBlocks[int(activeBlock.tiles[i].y / 10)][int(activeBlock.tiles[i].x / 10)] != 0:
                return "Set back"

        return False

    def drawBottom(self):
        for i in range(len(self.positionBlocks)):
            for i2 in range(len(self.positionBlocks[i])):
                if self.positionBlocks[i][i2] != 0:
                    self.pygame.draw.rect(self.win, self.positionBlocks[i][i2], (i2 * 10, (i - 1) * 10, 10, 10))

