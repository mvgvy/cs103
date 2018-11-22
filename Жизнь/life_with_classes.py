import pygame
from pygame.locals import *
import random
from copy import deepcopy
from typing import List, Tuple


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()


class Cell:

    def __init__(self, row: int, col: int, state=False):
        self.state = state
        self.row = row
        self.col = col

    def is_alive(self) -> bool:
        return self.state


class CellList:

    def __init__(self, nrows:int, ncols:int, randomize=False):
        self.nrows = nrows
        self.ncols = ncols
        self.grid = []
        if randomize:
            for j in range(ncols):
                for i in range(nrows):
                    self.grid.append(Cell(i, j, random.randint(0, 1)))
        else:
            for i in range(nrows):
                for j in range(ncols):
                    self.grid.append(Cell(i, j, 0))

    def get_neighbours(self, cell: Cell) -> List[Cell]:
        neighbours = []
        x, y = cell.row, cell.col
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i in range(0, self.nrows) and j in range(0, self.ncols) and (i != x or j != y):
                    neighbours.append(self.grid[i][j])
        return neighbours

    def update(self):
        new_grid = copy.deepcopy(self.grid)
        for cell in self:
            neighbours = self.get_neighbours(cell)
            neighbours = sum(i.is_alive() for i in neighbours)
            if cell.is_alive():
                if neighbours == 2:
                    pass
                elif neighbours == 3:
                    new_grid[cell.row][cell.col].state = 1
                else:
                    new_grid[cell.row][cell.col].state = 0
        return self

    @classmethod
    def from_file(cls, filename: str) -> List:
        grid = []
        file = open(filename).read()
        row = 0
        col = 0
        for line in file:
            row = []
            for item in line:
                if item == '0':
                    row.append(Cell(row, col, False))
                else:
                    row.append(Cell(row, col, True))
                ncol = col
                col += 1
            col = 0
            row += 1
        grid.append(row)
        nrow = row

        return CellList(nrow, ncol, openFile=True, cell_list=grid)

    def __iter__(self):
        self.i, self.j = 0, 0
        return self

    def __next__(self):
        if self.i < self.nrows:
            cell = self.grid[self.i][self.j]
            self.j += 1
            if self.j == self.ncols:
                self.i += 1
                self.j = 0
            return cell
        else:
            raise StopIteration

    def __str__(self) -> str:
        str = ''
        for i in range(self.nrows):
            for j in range(self.ncols):
                if seld.grid[i][j].state is True:
                    str += '1'
                else:
                    str += '0'
            str += '\n'
        return str
