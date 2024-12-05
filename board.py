import pygame
from cell import Cell
from sudoku_generator import generate_sudoku


class Board:
   def __init__(self, width, height, screen, board_data=None):
       self.width = width
       self.height = 600  # Fixed height for the Sudoku board
       self.screen = screen
       self.board = []
       self.initial_board = []  # To store the initial state of the board


       # If board_data is passed (pre-generated board)
       if board_data:
           self.board = [
               [Cell(board_data[row][col], row, col, screen, width // 9, self.height // 9) for col in range(9)]
               for row in range(9)
           ]
           self.initial_board = [row[:] for row in board_data]  # Store initial state
       else:
           self.board = [
               [Cell(0, row, col, screen, width // 9, self.height // 9) for col in range(9)]
               for row in range(9)
           ]
           self.initial_board = [[0 for _ in range(9)] for _ in range(9)]  # Default initial state


   def generate_board(self, difficulty):
       # Determine the number of cells to remove based on difficulty
       removed_cells = 20 if difficulty == 1 else 40 if difficulty == 2 else 50
       board_values = generate_sudoku(9, removed_cells)


       # Convert the generated board into Cell objects
       return [
           [Cell(board_values[row][col], row, col, self.screen, self.width / 9, self.height / 9, is_fixed=(board_values[row][col] != 0))
            for col in range(9)]
           for row in range(9)
       ]


   def reset(self):
       # Reset the board to its initial state
       self.board = [
           [Cell(self.initial_board[row][col], row, col, self.screen, self.width / 9, self.height / 9, is_fixed=(self.initial_board[row][col] != 0))
            for col in range(9)]
           for row in range(9)
       ]


   def draw(self):
       # Draw the cells first
       for row in range(9):
           for col in range(9):
               self.board[row][col].draw()


       # Draw the thick gridlines between the 3x3 subgrids
       for i in range(1, 9):
           # Calculate exact pixel positions
           vertical_pos = i * (self.width / 9)
           horizontal_pos = i * (self.height / 9)


           # Draw the vertical thick lines for 3x3 grid boundaries
           if i % 3 == 0:
               pygame.draw.line(self.screen, (0, 0, 0), (vertical_pos, 0), (vertical_pos, self.height), 4)
           else:  # Regular thin lines for the rest
               pygame.draw.line(self.screen, (0, 0, 0), (vertical_pos, 0), (vertical_pos, self.height), 1)


           # Draw the horizontal thick lines for 3x3 grid boundaries
           if i % 3 == 0:
               pygame.draw.line(self.screen, (0, 0, 0), (0, horizontal_pos), (self.width, horizontal_pos), 4)
           else:  # Regular thin lines for the rest
               pygame.draw.line(self.screen, (0, 0, 0), (0, horizontal_pos), (self.width, horizontal_pos), 1)


       # Draw the outer border of the whole board (thick)
       pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, self.width, self.height), 4)


   def is_completed(self):
       # Check if the board is completed (all cells are filled and correct)
       for row in self.board:
           for cell in row:
               if cell.value == 0 or not cell.is_correct():
                   return False
       return True
