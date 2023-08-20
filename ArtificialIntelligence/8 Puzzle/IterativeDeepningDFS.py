import numpy as np
import time


def isSolvable(start, goal):
    start_inversions = start.NumberOfInversions()
    goal_inversions = goal.NumberOfInversions()
    return start_inversions % 2 == goal_inversions % 2


class Puzzle:
    def __init__(self, parent_row, parent_col, empty_row, empty_col, integers):
        self.integers = np.zeros((3, 3), dtype=int)
        self.parentRow = parent_row
        self.parentCol = parent_col
        self.emptyRow = empty_row
        self.emptyCol = empty_col
        for i in range(3):
            for j in range(3):
                self.integers[i][j] = integers[i][j]

    def NumberOfInversions(self):
        # An inversion is when a number precedes another number with a lower value. We count the number of inversions in
        # the start state and the goal state. If the parity (odd or even) of the number of inversions is the same for
        # both states, then it is possible to reach the goal state from the start state.

        inversions = 0
        oneD = self.integers.flatten()
        for i in range(len(oneD)):
            for j in range(i + 1, len(oneD)):
                if oneD[i] > oneD[j] and oneD[j]!=0:
                    inversions += 1
        return inversions

    def printMatrix(self):
        print("+-------+")
        for i in range(3):
            print(f'| {self.integers[i][0]} {self.integers[i][1]} {self.integers[i][2]} |')
        print("+-------+")

    def move(self, row, col, newRow, newCol):
        p = Puzzle(row, col, newRow, newCol, self.integers)
        q = p.integers[newRow][newCol]
        p.integers[newRow][newCol] = p.integers[row][col]
        p.integers[row][col] = q
        return p

    def getMoves(self):
        moves = []
        row, col = self.emptyRow, self.emptyCol

        if row > 0 and (row - 1 != self.parentRow or col != self.parentCol):
            moves.append(self.move(row, col, row - 1, col))  # check up
        if col < 2 and (row != self.parentRow or col + 1 != self.parentCol):
            moves.append(self.move(row, col, row, col + 1))  # check right
        if row < 2 and (row + 1 != self.parentRow or col != self.parentCol):
            moves.append(self.move(row, col, row + 1, col))  # check down
        if col > 0 and (row != self.parentRow or col - 1 != self.parentCol):
            moves.append(self.move(row, col, row, col - 1))  # check left

        return moves


def depthLimitedSearch(puzzle, goal, limit):
    if np.array_equal(puzzle.integers, goal.integers):
        return puzzle

    if limit <= 0:
        return None

    for move in puzzle.getMoves():
        d = depthLimitedSearch(move, goal, limit - 1)
        if d is not None:
            return d

    return None


def IDDFS(start, goal):
    depth = 0
    while True:
        d = depthLimitedSearch(start, goal, depth)
        if d is not None:
            return d, depth
        depth += 1


def isSolvable(start, goal):
    start_inversions = start.NumberOfInversions()
    goal_inversions = goal.NumberOfInversions()
    return start_inversions % 2 == goal_inversions % 2


def main():
    arr = np.array([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    e2 = np.array([[1, 5, 3], [2, 7, 4], [6, 0, 8]])
    # unsolvableStart = np.array([[1, 2, 3], [4, 5, 6], [8, 7, 0]])
    start = Puzzle(-1, -1, 2, 0, e2)
    start.printMatrix()
    arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    # unsolvableGoal = np.array([[1, 2, 3], [4, 5, 6], [8, 0, 7]])
    goal = Puzzle(-1, -1, 2, 2, arr2)

    if not isSolvable(start, goal):
        print("Puzzle is not solvable")
    else:
        stime = time.time()
        end, d = IDDFS(start, goal)
        etime = time.time()
        print("Time Spent:", etime - stime, "seconds")
        end.printMatrix()
        print("Depth", d)


main()
