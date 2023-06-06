import pygame


def make_screen(n, queen_pos):
    # kích thước của giao diện
    X = 400
    Y = 400
    pygame.init()  # Khởi động pygame
    scrn_display = pygame.display
    scrn_display.set_caption("Result")
    size = scrn_display.set_mode([X, Y])

    window = True
    while window:
        for event in pygame.event.get():
            # Khi thoát khỏi cửa sổ, vòng lặp kết thúc
            if event.type == pygame.QUIT:
                window = False

        size.fill((210, 210, 210))
        # Vòng lặp này vẽ các ô vuông màu đen so le với nhau
        # Kết hợp với màu nền khi nãy, ta có một bàn cờ vua
        for i in range(n):
            for j in range(n):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(size, (0, 0, 0), pygame.Rect((X / n) * i, (Y / n) * j, X / n, Y / n))
        # Vẽ từng quân hậu đã lưu trong list
        for k in queen_pos:
            pygame.draw.circle(size, (255, 0, 0), ((queen_pos[k]+0.5) * (Y/n), (k+0.5) * (X/n)), X/n/3)
        # Cập nhật cửa sổ
        pygame.display.flip()

    pygame.quit()


# Vẽ bàn cờ. 1 chỉ vị trí quân hậu được đặt vào bàn cờ
def draw_board(n):
    for i in range(n):
        for j in range(n):
            if j == queen_pos[i]:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()


# Kiểm tra nếu vị trí đặt quân hậu là an toàn. Có 3 điều kiện được kiểm tra
# 1. Không nằm trên cùng cột của những con hậu đã được đặt (Điều kiện đầu)
# 2. Không nằm trên đường chéo của con hậu đã được đặt (2 điều kiện sau)
# (Không kiểm tra hàng bởi nó luôn khác nhau)
def possible(line, col):
    for i in range(line):
        if queen_pos[i] == col or col - line == queen_pos[i] - i or col + line == queen_pos[i] + i:
            return False
    return True


# Tạo phương án. Nếu vị trí hợp lệ, đặt con hậu ở hàng i cột j và tăng hàng i lên 1
# Khi i = số hàng - 1, vẽ bàn cờ & phương án
def gen(i, n):
    for j in range(n):
        if possible(i, j):
            queen_pos[i] = j
            if i == n - 1:
                print(queen_pos)
                draw_board(n)
                make_screen(n, queen_pos)
            gen(i+1, n)


n = abs(int(input("Nhap so n (tuong ung voi n quan hau tren ban co nxn): ")))
# Tạo list các quân hậu, với index chỉ số hàng (VD: 0 là hàng 1, 1 là hàng 2) và giá trị chỉ số cột
queen_pos = n * [0]
# Bắt đầu với hàng đầu tiên, tương ứng với quân hậu đầu tiên
# Mỗi quân hậu sẽ được đặt theo từng hàng từ trên xuống
gen(0, n)

