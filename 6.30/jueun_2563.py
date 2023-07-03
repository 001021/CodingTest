paper_num = int(input())
black_area = 0
board_size = 100

board = [[0] * board_size for _ in range(board_size)]

for _ in range(paper_num):
    left, bottom = map(int, input().split())
    right = left + 10
    top = bottom + 10
    for i in range(left, right):
        for j in range(bottom, top):
            board[i][j] = 1

for i in range(board_size):
    for j in range(board_size):
        black_area += board[i][j]

print(black_area)
