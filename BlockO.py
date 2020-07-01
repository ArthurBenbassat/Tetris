class BlockO:
    color = (255, 255, 0)
    position = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    height = 20
    width = 20
    stand = 0
    positions = [[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                 [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                 [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                 [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def rotate(self):
        if self.stand == 3:
            self.stand = 0
        else:
            self.stand += 1

        self.position = self.positions[self.stand]
        tempHeight = self.height
        self.height = self.width
        self.height = tempHeight