import pygame
import random


class Board:
    def __init__(self):
        # Grid is what is currently placed on the board and is not necessarily correct.
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Fixed grid is the initial numbers that are on the board and never changes unless the board is randomized.
        self.fixed_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Solved grid is the solution to the current board.
        self.solved_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # The draw board function prints the board to the screen.
    def draw_board(self):
        # Gap is the space between each square on the board.
        gap = x // 3
        # Current gap is gap that is currently being used and is needed because the gap changes.
        current_gap = gap

        # If the cursor is on the square it highlights the square.
        if self.cursor_position():
            # Records the position of the cursor into the following variables.
            x_gap, y_gap, x_gap_interval, y_gap_interval, x_pos, y_pos = self.cursor_position()

            # Prints the highlighted square onto the screen.
            pygame.draw.rect(screen, "lime", (x_gap, y_gap, x_gap_interval, y_gap_interval))

        # Prints the vertical lines between each 3x3 square on the board.
        for line in range(1, 4):
            pygame.draw.line(screen, "black", (current_gap, 0), (current_gap, y), 10)
            # Changes the current gap by a single gap to make the next vertical line to the right.
            current_gap += gap

        # Changes the gap and current gap to a new value
        gap = x // 9
        current_gap = gap

        # Prints the vertical lines between each square on the board.
        for line in range(1, 10):
            pygame.draw.line(screen, "black", (current_gap, 0), (current_gap, y), 5)
            # Changes the current gap by a single gap to make the next vertical line to the right.
            current_gap += gap

        # Changes the gap and current gap to a new value
        gap = y // 3
        current_gap = gap

        # Prints the horizontal lines between each 3x3 square on the board.
        for line in range(1, 4):
            pygame.draw.line(screen, "black", (0, current_gap), (y, current_gap), 10)
            # Changes the current gap by a single gap to make the next horizontal line below the last one.
            current_gap += gap

        # Changes the gap and current gap to a new value.
        gap = y // 9
        current_gap = gap

        # Prints the horizontal lines between each square on the board.
        for line in range(1, 10):
            pygame.draw.line(screen, "black", (0, current_gap), (y, current_gap), 2)
            # Changes the current gap by a single gap to make the next horizontal line below the last one.
            current_gap += gap

        # Determines the x and y gap interval.
        x_gap_interval = x // 9
        y_gap_interval = y // 9

        # Determines the font used for the numbers on the board.
        text_font = pygame.font.SysFont("Arial", int(50))

        # Goes through each row on the board.
        for y_square in range(9):
            # Goes through each column on the board.
            for x_square in range(9):
                # Prints the number to the screen if the position on the board is not zero.
                if self.grid[y_square][x_square] != 0:
                    self.write_text(self.grid[y_square][x_square], text_font, "blue", ((x_square) * x_gap_interval) + (x_gap_interval / 2.5), ((y_square ) * y_gap_interval) + (y_gap_interval / 3))

    # The cursor position function determines the position of the mouse on the board.
    def cursor_position(self):
        x_gap = 0
        x_gap_interval = x // 9
        y_gap_interval = y // 9

        # Determines if the mouse is between the left and right hand side of the board.
        if (pygame.mouse.get_pos()[0] > 0) & (pygame.mouse.get_pos()[0] < x):

            # Determines if the mouse is between the top and bottom of the board.
            if (pygame.mouse.get_pos()[1] > 0) & (pygame.mouse.get_pos()[1] < y):
                y_gap = 0
                found_y = False

                for y_square in range(1, 11):

                    if (pygame.mouse.get_pos()[1] < y_gap) & (not found_y):
                        found_y = True
                        y_gap -= y_gap_interval

                    elif not found_y:
                        y_gap += y_gap_interval

                for x_square in range(1, 10):

                    if (pygame.mouse.get_pos()[0] > x_gap) & (pygame.mouse.get_pos()[0] < x_gap + x_gap_interval):

                        if (pygame.mouse.get_pos()[1] > y_gap) & (pygame.mouse.get_pos()[1] < y_gap + y_gap_interval):

                            y_pos = (y_gap // y_gap_interval)
                            x_pos = (x_gap // x_gap_interval)

                            return x_gap, y_gap, x_gap_interval, y_gap_interval, x_pos, y_pos

                    x_gap += x_gap_interval

                x_gap += x_gap_interval

        return False

    # The write text function prints text to the screen.
    def write_text(self, text, font, text_colour, width, height):
        writing = font.render(str(text), True, text_colour)
        screen.blit(writing, (width, height))

    # The place function places a number on the board.
    def place(self, value):
        # Checks if the cursor is on the board.
        if self.cursor_position():
            # Records the position of the cursor into the following variables.
            x_gap, y_gap, x_gap_interval, y_gap_interval, x_pos, y_pos = self.cursor_position()
            # Checks if the number being placed is not on the fixed grid.
            if self.fixed_grid[y_pos][x_pos] == 0:
                # Checks if the number is valid.
                if self.is_valid(y_pos, x_pos, value, self.grid):
                    self.grid[y_pos][x_pos] = value

    # The clear function clears the board by making every value in the grid zero.
    def clear(self):
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # The random function randomized the board.
    def random(self):
        remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(remaining)
        for i in range(len(remaining)):
            col = random.randint(1, 8)

            self.grid[i][col] = remaining[i]
            self.fixed_grid[i][col] = remaining[i]
            self.solved_grid[i][col] = remaining[i]
            self.solve()

    # The is valid function checks if the number being placed is valid on the specified board.
    def is_valid(self, row, col, val, board_grid):
        # Checks if the number is already placed and if so returns false.
        for i in range(9):
            if (board_grid[i][col] == val) or (board_grid[row][i] == val):
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        # Goes through each individual square in the 3x3 square and checks if the number is already used, resulting
        # in false being returned.
        for i in range(3):
            for j in range(3):
                if board_grid[box_row + i][box_col + j] == val:
                    return False

        return True

    # The solve function solves the current board.
    def solve(self):
        # Goes through each row.
        for row in range(9):
            # Goes through each column.
            for col in range(9):
                # Checks if the square is not solved.
                if self.solved_grid[row][col] == 0:
                    # Checks each value.
                    for val in range(1, 10):
                        # Checks if the value is valid.
                        if self.is_valid(row, col, val, self.solved_grid):
                            # Records the value to the square.
                            self.solved_grid[row][col] = val
                            # Checks if the value is in the final solution.
                            if self.solve():
                                return True
                            # Reverts the value back to 0 if it is incorrect.
                            self.solved_grid[row][col] = 0
                    return False
        return True

    # The show solution function makes the grid equal to the solved grid.
    def show_solution(self):
        self.grid = self.solved_grid



running = True
pygame.init()
x, y = 1000, 1000
screen = pygame.display.set_mode((x + 100, y))
pygame.init()
board = Board()

while running:
    screen.fill("cadetblue1")
    for event in pygame.event.get():

        # Detected is the program is quit.
        if event.type == pygame.QUIT:
            pygame.quit()

        # Detected if a key is pressed down.
        if event.type == pygame.KEYDOWN:

            # If the '1' key is pressed place 1 on a valid selected tile.
            if event.key == pygame.K_1:
                board.place(1)

            # If the '2' key is pressed place 2 on a valid selected tile.
            if event.key == pygame.K_2:
                board.place(2)

            # If the '3' key is pressed place 3 on a valid selected tile.
            if event.key == pygame.K_3:
                board.place(3)

            # If the '4' key is pressed place 4 on a valid selected tile.
            if event.key == pygame.K_4:
                board.place(4)

            # If the '5' key is pressed place 5 on a valid selected tile.
            if event.key == pygame.K_5:
                board.place(5)

            # If the '6' key is pressed place 6 on a valid selected tile.
            if event.key == pygame.K_6:
                board.place(6)

            # If the '7' key is pressed place 7 on a valid selected tile.
            if event.key == pygame.K_7:
                board.place(7)

            # If the '8' key is pressed place 8 on a valid selected tile.
            if event.key == pygame.K_8:
                board.place(8)

            # If the '9' key is pressed place 9 on a valid selected tile.
            if event.key == pygame.K_9:
                board.place(9)

            # If the backspace key is pressed place 0 on a valid selected tile.
            if event.key == pygame.K_BACKSPACE:
                board.place(0)

            # If the 'c' key is pressed clear the board.
            if event.key == pygame.K_c:
                board.clear()

            # If the 's' key is pressed solve the current board.
            if event.key == pygame.K_s:
                board.show_solution()

            # If the 'r' key is pressed clear and randomize the board.
            if event.key == pygame.K_r:
                board.clear()
                board.random()

    # Refreshes the screen.
    board.draw_board()
    pygame.display.flip()


pygame.quit()
