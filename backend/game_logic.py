# I want to port over my C++ class to this Python file

class TicTacToe:
    def __init__(self): # this is the constructor
        self.reset()

    def reset(self):
        # Variables needed: board (2D array), current player, if game is still going, number of remaining pieces, a winner, and a set for the used up spots

        self.current_player = 'X'
        self.game_going = True
        self.remaining_pieces = 9
        self.winner = None
        self.used_spots = set()
        self.board = [ ['' for i in range(3)] for i in range(3) ] # 2d array initialized with empty string values

    def make_move(self, player, pos):
        # first need to check that the game is still going, and that we didn't put it into some bad position
        if not self.game_going or pos in self.used_spots:
            return

        self.used_spots.add(pos)

        row, col = divmod(pos - 1, 3) # div mod returns a pair of quotient, remainder. For our purposes, this formula would give us accurate row and col
        # position is a number between 1 through 9

        # board[row][col] = self.player
        self.board[row][col] = player

        if self.check_win(player):
            self.winner = player
            self.game_going = False

        else:
            self.remaining_pieces -= 1
            if self.remaining_pieces == 0:
                self.game_going = False

            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    def check_win(self, player):
        # checks if a player just won
        for i in range(3):
            if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i] and self.board[1][i] == player: # check cols
                return True

            if self.board[i][0] == self.board[i][1] and self.board[i][2] == self.board[i][1] and self.board[i][1] == player: # check rows
                return True
        
        return (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[0][0] == player) or (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and self.board[0][2] == player)

    def status(self):
        if self.winner:
            return self.winner + " wins!"

        elif not self.game_going: # there is no declared winner, but the game is over, meaning it's a draw
            return 'Draw!'

        return "Next player: " + self.current_player