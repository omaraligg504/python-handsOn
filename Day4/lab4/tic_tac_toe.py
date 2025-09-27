import random
import os

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.is_computer = False

    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                # ask for both row and column at once and minus 1 for 0-indexing
                raw_input = input(f"{self.name} ({self.symbol}), enter row and column (1-3 1-3): ")
                row, col = map(int, raw_input.split())
                row -= 1
                col -= 1
                # Validate input if out of bounds or position taken
                if row not in range(3) or col not in range(3):
                    print("Invalid position. Row and column must be between 1 and 3.")
                elif board.grid[row][col] != ' ':
                    print("Position already taken. Choose another one.")
                else:
                    return row, col
            #if user enters non-integer values
            except ValueError:
                print("Invalid input. Please enter two numbers separated by space, e.g. `2 3`.")
            #catch any other unexpected errors like entering too many values or less than two values and so on
            except Exception:
                print("Unexpected error. Try again.")


class ComputerPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.is_computer = True

    def make_move(self, board):
        # Randomly choose an available position # this function gets random elements from a list of all available positions random.choice
        available_positions = [(r, c) for r in range(3) for c in range(3) if board.grid[r][c] == ' ']
        row, col = random.choice(available_positions)
        print(f"{self.name} ({self.symbol}) chooses row {row + 1}, column {col + 1}")
        return row, col


class Board:
    # initialize a 3x3 grid with empty spaces
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    # display the current state of the board
    def display(self):
        print("\n")
        for i in range(3):
            # join the elements of each row with | in between
            print(" | ".join(self.grid[i]))
            # print a separator line between rows
            if i < 2:
                print("-" * 9)
        print("\n")

    def update(self, row, col, symbol):
        # place the player's symbol at the specified position
        self.grid[row][col] = symbol

    def check_winner(self):
        g = self.grid
        # Check rows
        for row in g:
            if row[0] == row[1] == row[2] != ' ':
                return True
        # Check columns
        for col in range(3):
            if g[0][col] == g[1][col] == g[2][col] != ' ':
                return True
        # Check diagonals
        if g[0][0] == g[1][1] == g[2][2] != ' ':
            return True
        if g[0][2] == g[1][1] == g[2][0] != ' ':
            return True
        return False

    def is_full(self):
        # Check if all cells are filled with symbols or not
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True



class Game:
    # initialize the game with two players and a board and the first player always starts first
    def __init__(self, player1, player2, mode):
        self.players = [player1, player2]
        self.board = Board()
        self.current_turn = 0
        self.mode = mode 
    # after eact round switch the turn to the other player
    def switch_turns(self):
        self.current_turn = 1 - self.current_turn
    # main game loop
    def play(self):
        while True:
            # show the current board state
            self.board.display()

            # see whose turn it is
            current_player = self.players[self.current_turn]

            # get the move from the current player and update the board
            row, col = current_player.make_move(self.board)
            self.board.update(row, col, current_player.symbol)

            # check for a win or a draw
            if self.board.check_winner():
                self.board.display()
                winner = current_player
                loser = self.players[1 - self.current_turn]

                # Handle messages depending on mode
                if hasattr(self, "mode") and self.mode == 2:  # Player vs Computer
                    if winner.is_computer:
                        print(f"Hard luck {loser.name}, you lost!")
                    else:
                        print(f"Congratulations {winner.name}, you win!")
                else:  # Two human players
                    print(f"Congratulations {winner.name}, you win!")
                    print(f"Hard luck next time {loser.name}")

                print("Game Over")
                break

            elif self.board.is_full():
                self.board.display()
                print("It's a draw")
                break

            else:
                self.switch_turns()



def main():
    print("Welcome to Tic-Tac-Toe")
    mode = input("Do you want to play with a friend (1) or vs computer (2)? ")
    # its all 
    if mode == '1':
        name1 = input("Enter name for Player 1 (X): ")
        name2 = input("Enter name for Player 2 (O): ")
        player1 = HumanPlayer(name1, 'X')
        player2 = HumanPlayer(name2, 'O')
    elif mode == '2':
        name1 = input("Enter your name (X): ")
        player1 = HumanPlayer(name1, 'X')
        player2 = ComputerPlayer("Computer", 'O')
    else:
        print("Invalid option. Please restart the game.")
        return
    game = Game(player1, player2,int(mode))
    game.play()


if __name__ == "__main__":
    main()
