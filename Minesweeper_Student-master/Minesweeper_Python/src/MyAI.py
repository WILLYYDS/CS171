from AI import AI
from Action import Action
import random

class MyAI( AI ):

    def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
        self.rowDimension = rowDimension
        self.colDimension = colDimension
        self.totalMines = totalMines
        self.startX = startX
        self.startY = startY
        self.visited = set()  # Keep track of visited cells
        self.toVisit = [(startX, startY)]  # Start with the initial cell
        self.visited.add((startX, startY))

    def getAction(self, number: int) -> "Action Object":
        if number == 0:
            # Expand to all adjacent cells if no mines are adjacent
            x, y = self.toVisit.pop(0)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rowDimension and 0 <= ny < self.colDimension and (nx, ny) not in self.visited:
                        self.toVisit.append((nx, ny))
                        self.visited.add((nx, ny))
            if self.toVisit:
                next_x, next_y = self.toVisit[0]
                return Action(AI.Action.UNCOVER, next_x, next_y)
        else:
            # No safe cells, randomly pick an unvisited cell
            while self.toVisit:
                next_x, next_y = self.toVisit.pop(0)
                if (next_x, next_y) not in self.visited:
                    self.visited.add((next_x, next_y))
                    return Action(AI.Action.UNCOVER, next_x, next_y)

        # If no moves are left, leave the game
        return Action(AI.Action.LEAVE)
