import pygame


class Cell:
   def __init__(self, value, row, col, screen, width, height, is_fixed=False):
       self.value = value  # The actual value in the cell
       self.row = row
       self.col = col
       self.screen = screen
       self.width = width
       self.height = height
       self.is_fixed = is_fixed  # Whether the cell is pre-filled and not editable
       self.sketched_value = 0  # Temporary value for pencil marks
       self.selected = False  # Indicates whether this cell is selected


   def set_sketched_value(self, value):
       self.sketched_value = value  # Set the user's input value


   def draw(self):
       # Example of drawing logic
       font = pygame.font.Font(None, 36)  # Use a default font
       rect = pygame.Rect(self.col * self.width, self.row * self.height, self.width, self.height)


       # Draw the cell background based on selection
       if self.selected:
           pygame.draw.rect(self.screen, (200, 200, 255), rect)  # Light blue for selected
       else:
           pygame.draw.rect(self.screen, (255, 255, 255), rect)  # White for unselected


       # Draw the cell value or sketched value
       if self.value != 0:  # Draw actual value if set
           text = font.render(str(self.value), True, (0, 0, 0))
           self.screen.blit(text, (self.col * self.width + 10, self.row * self.height + 10))
       elif self.sketched_value != 0:  # Draw sketched value if set
           text = font.render(str(self.sketched_value), True, (150, 150, 150))
           self.screen.blit(text, (self.col * self.width + 10, self.row * self.height + 10))


       # Draw the border for each individual cell
       pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Thin black border for each cell
