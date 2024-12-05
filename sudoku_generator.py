import random

class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.board = [[0] * row_length for _ in range(row_length)]  # 9x9 grid
        self.removed_cells = removed_cells

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        nums = random.sample(range(1, 10), 9)  # Random digits 1-9
        idx = 0
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums[idx]
                idx += 1

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row=0, col=0):
        if row == self.row_length and col == 0:
            return True  # Successfully filled the board

        if col >= self.row_length:  # Move to the next row if col exceeds bounds
            row += 1
            col = 0

        if row >= self.row_length:  # If we've filled all rows, return True
            return True

        if self.board[row][col] != 0:  # Skip cells that are already filled
            return self.fill_remaining(row, col + 1)

        for num in random.sample(range(1, 10), 9):  # Try numbers in random order
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True

                self.board[row][col] = 0  # Backtrack

        return False  # Trigger backtracking

    def remove_cells(self):
        attempts = self.removed_cells
        while attempts > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                attempts -= 1

    def fill_values(self):
        self.fill_diagonal()  # Fill diagonal boxes first
        self.fill_remaining()  # Then fill the rest of the board



def generate_sudoku(row_length, difficulty):
    sudoku_gen = SudokuGenerator(row_length, difficulty)
    sudoku_gen.fill_diagonal()
    sudoku_gen.fill_remaining()
    sudoku_gen.remove_cells()  # This will remove cells based on the difficulty value passed
    return sudoku_gen.get_board()

