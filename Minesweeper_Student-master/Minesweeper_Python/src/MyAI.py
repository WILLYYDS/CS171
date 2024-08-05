from AI import AI
from Action import Action
import random

class MyAI(AI):

    def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
        self.rowDimension = rowDimension
        self.colDimension = colDimension
        self.totalMines = totalMines
        self.startX = startX
        self.startY = startY
        self.visited = set()  # Keep track of visited cells
        self.toVisit = [(startX, startY)]  # Start with the initial cell
        self.visited.add((startX, startY))
        self.flags = set()  # Use a set to store flagged positions
        self.board = [[-1 for _ in range(colDimension)] for _ in range(rowDimension)]  # Store board state
        self.remainingMines = totalMines

    def getAction(self, number: int) -> "Action Object":
        if self.toVisit:
            x, y = self.toVisit.pop(0)
        else:
            return Action(AI.Action.LEAVE)
        
        self.board[x][y] = number

        if number == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.rowDimension and 0 <= ny < self.colDimension and (nx, ny) not in self.visited:
                        self.toVisit.append((nx, ny))
                        self.visited.add((nx, ny))

        elif number == 1:
            self.analyzeAdjacentCells(x, y)

        if self.toVisit:
            next_x, next_y = self.toVisit[0]
            return Action(AI.Action.UNCOVER, next_x, next_y)
        else:
            return Action(AI.Action.LEAVE)

    def analyzeAdjacentCells(self, x, y):
        unrevealed = []
        flagged_count = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rowDimension and 0 <= ny < self.colDimension:
                    if self.board[nx][ny] == -1 and (nx, ny) not in self.visited:
                        unrevealed.append((nx, ny))
                    if (nx, ny) in self.flags:
                        flagged_count += 1

        if len(unrevealed) == 1 and flagged_count == 0 and self.remainingMines > 0:
            for ux, uy in unrevealed:
                self.flags.add((ux, uy))
                self.visited.add((ux, uy))
                self.remainingMines -= 1
                return Action(AI.Action.FLAG, ux, uy)

        if flagged_count == 1:
            for ux, uy in unrevealed:
                if (ux, uy) not in self.flags:
                    self.toVisit.append((ux, uy))
                    self.visited.add((ux, uy))
                    return Action(AI.Action.UNCOVER, ux, uy)