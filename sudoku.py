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

        # Fixed grid is what was placed initially for the current game.
        self.fixed_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Difficulty variable keeps track of the current difficulty.
        self.difficulty = "Sandbox"

        # The button colour variables determine the colour of the buttons.
        self.undo_button_colour = "azure3"
        self.solve_button_colour = "azure3"
        self.difficulty_button_colour = "azure3"

    # The draw board function prints the board to the screen.
    def draw_board(self):

        # Gap is the space between each square on the board.
        gap = x // 3
        # These variables are used to record the cursor position.
        x_gap, y_gap, x_gap_interval, y_gap_interval, x_pos, y_pos = 0, 0, 0, 0, 0, 0
        # Current gap is gap that is currently being used and is needed because the gap changes.
        current_gap = gap
        # Value is the number that has been highlighted.
        value = 0

        # If the cursor is on the square it highlights the square.
        if self.cursor_position():
            # Records the position of the cursor into the following variables.
            x_gap, y_gap, x_gap_interval, y_gap_interval, x_pos, y_pos = self.cursor_position()

            value = self.grid[y_pos - 2][x_pos - 1]

            # Prints the highlighted square onto the screen.
            pygame.draw.rect(screen, "beige", (x_gap + x_offset, y_offset, x_gap_interval, y))
            pygame.draw.rect(screen, "beige", (x_offset, y_gap + y_offset, x, y_gap_interval))

        # Determines the x and y gap interval.
        x_gap_interval = x // 9

        y_gap_interval = y // 9

        # Determines the font used for the numbers on the board.
        text_font = pygame.font.SysFont("Arial", int(50 * scale))

        # Determines which colour is used in the win screen to make a checkered pattern.
        win_next_colour = False

        # Goes through each row on the board.
        for y_square in range(9):
            # Goes through each column on the board.
            for x_square in range(9):
                # Prints the number to the screen if the position on the board is not zero.
                # Decides the colour of the square from whether it is in the fixed grid or not.
                if self.fixed_grid[y_square][x_square] != 0:
                    colour = "black"

                else:
                    colour = "blue"

                # If the user has completed a sudoku the tiles become green. It is in a checkered pattern.
                if (y_square == y_pos - 2) & (x_square == x_pos - 1):
                    pygame.draw.rect(screen, "cadetblue1", (
                        ((x_square * x_gap_interval) + x_offset), ((y_square * y_gap_interval) + y_offset),
                        (x_gap_interval), (y_gap_interval)))
                    if win_next_colour:
                        win_next_colour = False
                    else:
                        win_next_colour = True

                elif self.check_win():
                    if win_next_colour:
                        colour = "green"
                        win_next_colour = False
                    else:
                        colour = "green3"
                        win_next_colour = True

                    pygame.draw.rect(screen, colour, (
                        ((x_square * x_gap_interval) + x_offset), ((y_square * y_gap_interval) + y_offset),
                        (x_gap_interval), (y_gap_interval)))
                    colour = "black"

                elif (self.grid[y_square][x_square] == value) & (value != 0):
                    pygame.draw.rect(screen, "bisque2", (
                        ((x_square * x_gap_interval) + x_offset), ((y_square * y_gap_interval) + y_offset),
                        (x_gap_interval), (y_gap_interval)))

                if self.grid[y_square][x_square] != 0:
                    self.write_text(self.grid[y_square][x_square], text_font, colour,
                                    ((x_square + 1) * x_gap_interval) + (x_gap_interval / 2.5),
                                    ((y_square + 2) * y_gap_interval) + (y_gap_interval / 3))

        pygame.draw.line(screen, "black", (x_offset, y_offset), (x_offset, y + y_offset), 10)
        pygame.draw.line(screen, "black", (x_offset, y_offset), (x + x_offset, y_offset), 10)

        # Prints the vertical lines between each 3x3 square on the board.
        for line in range(1, 4):
            pygame.draw.line(screen, "black", (current_gap + x_offset, y_offset),
                             (current_gap + x_offset, y + y_offset), 10)
            # Changes the current gap by a single gap to make the next vertical line to the right.
            current_gap += gap

        # Changes the gap and current gap to a new value
        gap = x // 9
        current_gap = gap

        # Prints the vertical lines between each square on the board.
        for line in range(1, 10):
            pygame.draw.line(screen, "black", (current_gap + x_offset, y_offset),
                             (current_gap + x_offset, y + y_offset), 5)
            # Changes the current gap by a single gap to make the next vertical line to the right.
            current_gap += gap

        # Changes the gap and current gap to a new value
        gap = y // 3

        current_gap = gap

        # Prints the horizontal lines between each 3x3 square on the board.
        for line in range(1, 4):
            pygame.draw.line(screen, "black", (x_offset, current_gap + y_offset),
                             (x + x_offset, current_gap + y_offset), 10)
            # Changes the current gap by a single gap to make the next horizontal line below the last one.
            current_gap += gap

        # Changes the gap and current gap to a new value.
        gap = y // 9

        current_gap = gap

        # Prints the horizontal lines between each square on the board.
        for line in range(1, 10):
            pygame.draw.line(screen, "black", (x_offset, current_gap + y_offset),
                             (x + x_offset, current_gap + y_offset), 5)
            # Changes the current gap by a single gap to make the next horizontal line below the last one.
            current_gap += gap
        text_font = pygame.font.SysFont("Arial", int(35 * scale))
        self.write_text("Difficulty", text_font, "black", x_offset, y_offset * .60)
        self.write_text(self.difficulty, text_font, "black", x_offset, y_offset * .75)

        pygame.draw.rect(screen, self.undo_button_colour,
                         (x_offset - (x_offset * .1), y + (y_offset * 1.3), 85 * scale, 40 * scale))
        self.write_text("Clear", text_font, "black", x_offset, y + (y_offset * 1.3))

        pygame.draw.rect(screen, self.solve_button_colour,
                         (x_offset + (x / 5.5) - (x_offset * .1), y + (y_offset * 1.3), 90 * scale, 40 * scale))
        self.write_text("Solve", text_font, "black", x_offset + (x / 5.5), y + (y_offset * 1.3))

        pygame.draw.rect(screen, self.difficulty_button_colour,
                         (x_offset + (x * .77) - (x_offset * .1), y + (y_offset * 1.3), 230 * scale, 40 * scale))
        self.write_text("Change Difficulty", text_font, "black", x_offset + (x * .77), y + (y_offset * 1.3))

    # The cursor position function determines the position of the mouse on the board.
    def cursor_position(self):
        x_gap = x_offset

        x_gap_interval = x // 9
        y_gap_interval = y // 9

        if self.button_hover(x_offset - (x_offset * .1), y + (y_offset * 1.3),
                             (x_offset - (x_offset * .1)) + (85 * scale), y + (y_offset * 1.3) + (40 * scale),
                             self.clear):
            self.undo_button_colour = "azure4"

        else:
            self.undo_button_colour = "azure3"

        if self.button_hover(x_offset + (x / 5.5) - (x_offset * .1), y + (y_offset * 1.3),
                             (x_offset + (x / 5.5) - (x_offset * .1)) + (90 * scale),
                             (y + (y_offset * 1.3)) + (40 * scale), self.solve):
            self.solve_button_colour = "azure4"

        else:
            self.solve_button_colour = "azure3"

        if self.button_hover(x_offset + (x * .77) - (x_offset * .1), y + (y_offset * 1.3),
                             x_offset + (x * .77) - (x_offset * .1) + (230 * scale),
                             y + (y_offset * 1.3) + (40 * scale), self.change_difficulty):
            self.difficulty_button_colour = "azure4"

        else:
            self.difficulty_button_colour = "azure3"
        # Determines if the mouse is between the left and right hand side of the board.
        if (pygame.mouse.get_pos()[0] > x_offset) & (pygame.mouse.get_pos()[0] < (x + x_offset)):

            # Determines if the mouse is between the top and bottom of the board.
            if (pygame.mouse.get_pos()[1] > y_offset) & (pygame.mouse.get_pos()[1] < (y + y_offset)):
                y_gap = y_offset
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
                            y_pos = int(y_gap // y_gap_interval)
                            x_pos = int(x_gap // x_gap_interval)

                            return x_gap - x_offset, y_gap - y_offset, x_gap_interval, y_gap_interval, x_pos, y_pos

                    x_gap += x_gap_interval

                x_gap += x_gap_interval

        return False

    # The button hover function checks if the mouse is over the button, and if the mouse has been clicked.
    def button_hover(self, left, top, right, bottom, function):
        # Determines if the mouse is between the left and right hand side of the board.
        if (pygame.mouse.get_pos()[0] > left) & (pygame.mouse.get_pos()[0] < right):

            # Determines if the mouse is between the top and bottom of the board.
            if (pygame.mouse.get_pos()[1] > top) & (pygame.mouse.get_pos()[1] < bottom):
                if click:
                    function()
                return True

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
            y_pos -= 1

            if self.fixed_grid[y_pos - 1][x_pos - 1] == 0:
                # Checks if the number is valid.
                if (self.is_valid(y_pos - 1, x_pos - 1, value)) | (value == 0):
                    self.grid[y_pos - 1][x_pos - 1] = value

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

        self.fixed_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.difficulty = "Sandbox"

    # The random function randomized the board.
    def random(self):
        # Goes through each row.
        for row in range(9):
            # Goes through each column.
            for col in range(9):
                # Checks if the square is not solved.
                if self.grid[row][col] == 0:
                    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    random.shuffle(numbers)
                    # Checks each value.
                    for val in numbers:
                        # Checks if the value is valid.
                        if self.is_valid(row, col, val):
                            # Records the value to the square.
                            self.grid[row][col] = val
                            self.fixed_grid[row][col] = val
                            # Checks if the value is in the final solution.
                            if self.random():
                                return True
                            # Reverts the value back to 0 if it is incorrect.
                            self.grid[row][col] = 0
                            self.fixed_grid[row][col] = 0
                    return False
        return True

    # The new game function clears and randomizes the board.
    # Once randomized it takes away values from the board.
    def new_game(self, remaining):
        remaining = 81 - remaining
        self.clear()
        self.random()
        while remaining > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grid[row][col] != 0:
                self.grid[row][col] = 0
                self.fixed_grid[row][col] = 0
                remaining -= 1

    # The change difficulty changes the difficulty based on what the difficulty is currently.
    def change_difficulty(self):
        if self.difficulty == "Sandbox":
            self.new_game(40)
            self.set_difficulty("Easy")

        elif self.difficulty == "Easy":
            self.new_game(30)
            self.set_difficulty("Medium")

        elif self.difficulty == "Medium":
            self.new_game(20)
            self.set_difficulty("Hard")

        elif self.difficulty == "Hard":
            self.clear()
            self.set_difficulty("Sandbox")

    # The is valid function checks if the number being placed is valid on the specified board.
    def is_valid(self, row, col, val):
        # Checks if the number is already placed and if so returns false.
        for i in range(9):
            if (self.grid[i][col] == val) or (self.grid[row][i] == val):
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        # Goes through each individual square in the 3x3 square and checks if the number is already used, resulting
        # in false being returned.
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == val:
                    return False

        return True

    # The solve function solves the current board.
    def solve(self):
        # Goes through each row.
        for row in range(9):
            # Goes through each column.
            for col in range(9):
                # Checks if the square is not solved.
                if self.grid[row][col] == 0:
                    # Checks each value.
                    for val in range(1, 10):
                        # Checks if the value is valid.
                        if self.is_valid(row, col, val):
                            # Records the value to the square.
                            self.grid[row][col] = val
                            # Checks if the value is in the final solution.
                            if self.solve():
                                return True
                            # Reverts the value back to 0 if it is incorrect.
                            self.grid[row][col] = 0
                    return False
        return True

    # The show solution function makes the grid equal to the solved grid.
    def show_solution(self):
        self.solve()

    # The check win method checks if the current game has been won.
    def check_win(self):
        for col in range(0, 9):
            for row in range(0, 9):
                if self.grid[row][col] == 0:
                    return False

        return True

    # The set difficulty function sets the difficulty.
    def set_difficulty(self, mode):
        self.difficulty = mode


running = True
pygame.init()
scale = 1
x, y = 900, 900
x_offset = 100
y_offset = 200

pygame.display.set_caption("Sudoku")
pygame.init()
board = Board()
board_colour = "white"
info = pygame.display.Info()
width = info.current_w
height = info.current_h

# Changes the scale until the application can fit on the screen.
while (y + (y_offset * 2.5)) * scale >= height:
    scale -= .1
click = False
x *= scale
y *= scale
x_offset *= scale
y_offset *= scale
screen = pygame.display.set_mode((x + (x_offset * 2), y + (y_offset * 2)))
while running:
    click = False
    screen.fill(board_colour)
    for event in pygame.event.get():

        # Detected is the program is quit.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

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
                board.set_difficulty("Sandbox")

            # If the 's' key is pressed solve the current board.
            if event.key == pygame.K_s:
                board.show_solution()

            # If the 'e' key is pressed clear and randomize the board to easy difficulty.
            if event.key == pygame.K_e:
                board.new_game(40)
                board.set_difficulty("Easy")

            # If the 'm' key is pressed clear and randomize the board to medium difficulty.
            if event.key == pygame.K_m:
                board.new_game(30)
                board.set_difficulty("Medium")

            # If the 'h' key is pressed clear and randomize the board to hard difficulty.
            if event.key == pygame.K_h:
                board.new_game(20)
                board.set_difficulty("Hard")

            # If the 'q' key is pressed the application is exited.
            if event.key == pygame.K_q:
                running = False

    # Refreshes the screen.
    board.draw_board()
    pygame.display.flip()

pygame.quit()
