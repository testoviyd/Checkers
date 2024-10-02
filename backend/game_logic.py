class CheckersBoard:
    def __init__(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 != 0:
                    self.board[row][col] = 'B'  # Black pieces
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 != 0:
                    self.board[row][col] = 'R'  # Red pieces

    def display(self):
        for row in self.board:
            print(' '.join([piece if piece else '.' for piece in row]))
        print()

    def move_piece(self, from_x, from_y, to_x, to_y):
        if not self.is_valid_move(from_x, from_y, to_x, to_y):
            raise ValueError("Invalid move")

        self.board[to_x][to_y] = self.board[from_x][from_y]
        self.board[from_x][from_y] = ''

        # Handle captures, kinging, etc.

    def is_valid_move(self, from_x, from_y, to_x, to_y):
        # Implement move validation logic
        # Check bounds, piece ownership, move direction, captures, etc.
        return True  # Placeholder

    # Add more methods as needed
