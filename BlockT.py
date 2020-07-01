class BlockT:
    color = (128, 0, 128)
    position = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    height = 20
    width = 30
    stand = 0
    positions = [[[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                 [[1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                 [[0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]],
                 [[0, 1, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

    def rotate(self):
        if self.stand == 3:
            self.stand = 0
        else:
            self.stand += 1

        self.position = self.positions[self.stand]
        tempHeight = self.height
        self.height = self.width
        self.height = tempHeight