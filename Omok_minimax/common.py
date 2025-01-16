import numpy as np

def end1(board):
    # 보드의 가로, 세로, 대각선을 모두 확인하여 종료 조건을 확인
    for i in range(19):
        for j in range(19):
            # 가로 확인
            if j + 5 <= 19:
                if np.all(board[i, j:j+5] == 1):
                    print('END')
                    return True
            # 세로 확인
            if i + 5 <= 19:
                if np.all(board[i:i+5, j] == 1):
                    print('END')
                    return True
            # 대각선 확인 (오른쪽 아래 방향)
            if i + 5 <= 19 and j + 5 <= 19:
                if np.all(np.diag(board[i:i+5, j:j+5]) == 1):
                    print('END')
                    return True
            # 대각선 확인 (왼쪽 아래 방향)
            if i + 5 <= 19 and j - 5 >= -1:
                if np.all(np.diag(np.fliplr(board[i:i+5, j-4:j+1])) == 1):
                    print('END')
                    return True
    return False

def end2(board):
    # 보드의 가로, 세로, 대각선을 모두 확인하여 종료 조건을 확인
    for i in range(19):
        for j in range(19):
            # 가로 확인
            if j + 5 <= 19:
                if np.all(board[i, j:j+5] == 2):
                    print('END')
                    return True
            # 세로 확인
            if i + 5 <= 19:
                if np.all(board[i:i+5, j] == 2):
                    print('END')
                    return True
            # 대각선 확인 (오른쪽 아래 방향)
            if i + 5 <= 19 and j + 5 <= 19:
                if np.all(np.diag(board[i:i+5, j:j+5]) == 2):
                    print('END')
                    return True
            # 대각선 확인 (왼쪽 아래 방향)
            if i + 5 <= 19 and j - 5 >= -1:
                if np.all(np.diag(np.fliplr(board[i:i+5, j-4:j+1])) == 2):
                    print('END')
                    return True
    return False


def print_board(board):
    print('    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S')
    for idx,i in enumerate(board, 1):
        print(str(20-idx).rjust(2), end=" ")
        for j in i:
            print(str(j).rjust(2), end=" ")
        print()