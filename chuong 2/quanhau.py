import pygame

# Kích thước cửa sổ và bàn cờ
WIDTH = 800
HEIGHT = 800
BOARD_SIZE = 8

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens")

# Hàm vẽ bàn cờ
def draw_chessboard():
    square_size = WIDTH // BOARD_SIZE

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

# Hàm vẽ con hậu
def draw_queens(queens):
    square_size = WIDTH // BOARD_SIZE

    for row, col in enumerate(queens):
        x = col * square_size + square_size // 2
        y = row * square_size + square_size // 2
        pygame.draw.circle(screen, RED, (x, y), square_size // 3)

# Giải bài toán N-Queens
def solve_n_queens(n):
    queens = [-1] * n
    solutions = []

    def is_safe(row, col):
        for i in range(row):
            if queens[i] == col or queens[i] - i == col - row or queens[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(queens[:])
        else:
            for col in range(n):
                if is_safe(row, col):
                    queens[row] = col
                    backtrack(row + 1)

    backtrack(0)
    return solutions

# Hiển thị đường đi của con hậu
def display_queens_path(board_size, queens):
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_chessboard()
        draw_queens(queens)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Nhập kích thước bàn cờ từ người dùng
board_size = int(input("Nhập kích thước bàn cờ (số con hậu): "))

# Giải bài toán N-Queens
solutions = solve_n_queens(board_size)

# Hiển thị đường đi của con hậu
for queens in solutions:
    display_queens_path(board_size, queens)

