import pygame

# Hằng số màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_chessboard(screen, board_size):
    square_size = screen.get_width() // board_size
    for row in range(board_size):
        for col in range(board_size):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

def draw_knight(screen, x, y, board_size):
    square_size = screen.get_width() // board_size
    pygame.draw.circle(screen, GREEN, (x * square_size + square_size // 2, y * square_size + square_size // 2), square_size // 3)

def draw_path(screen, path, board_size):
    square_size = screen.get_width() // board_size
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        pygame.draw.line(screen, RED, (x1 * square_size + square_size // 2, y1 * square_size + square_size // 2),
                         (x2 * square_size + square_size // 2, y2 * square_size + square_size // 2), 4)

def display_knight_tour(board_size, knight_path):
    pygame.init()

    # Kích thước màn hình
    screen_size = 600
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Knight's Tour")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        draw_chessboard(screen, board_size)
        draw_path(screen, knight_path, board_size)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Sử dụng giải thuật mã đi tuần để tìm đường đi
def solve_knight_tour(board_size):
    # Khởi tạo bàn cờ và danh sách đường đi của con mã
    board = [[0] * board_size for _ in range(board_size)]
    knight_path = []

    # Các bước di chuyển của con mã
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Hàm kiểm tra ô trên bàn cờ có hợp lệ để di chuyển tới hay không
    def is_valid_move(x, y):
        return 0 <= x < board_size and 0 <= y < board_size and board[x][y] == 0

    # Hàm đệ quy để thực hiện mã đi tuần
    def knight_tour(x, y, move_number):
        # Đánh dấu ô hiện tại là đã đi qua
        board[x][y] = move_number
        # Thêm tọa độ ô hiện tại vào danh sách đường đi
        knight_path.append((x, y))

        # Kiểm tra nếu đã đi hết các ô trên bàn cờ
        if move_number == board_size * board_size:
            return True

        # Thử từng bước di chuyển tiếp theo
        for i in range(len(move_x)):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if is_valid_move(next_x, next_y):
                if knight_tour(next_x, next_y, move_number + 1):
                    return True

        # Không tìm được đường đi hợp lệ từ ô hiện tại, quay lui
        board[x][y] = 0
        knight_path.pop()
        return False

    # Bắt đầu từ ô (0, 0)
    start_x = 0
    start_y = 0
    knight_tour(start_x, start_y, 1)

    return knight_path


# Kích thước bàn cờ nhập từ bàn phím
board_size = int(input("Nhập kích thước bàn cờ: "))

# Giải thuật mã đi tuần để tìm đường đi
knight_path = solve_knight_tour(board_size)

# Hiển thị đường đi của con mã trên màn hình
display_knight_tour(board_size, knight_path)
