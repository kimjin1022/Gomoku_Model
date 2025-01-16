while True:
    try:
        print('=' * 59)
        location_r, location_c = list(input("상대방이 착수 한 곳을 입력해 주세요").split())
        if (location_r, location_c) == ('roll', 'back'):
            board = tmp_board
            print_board(board)
            continue
        tmp_board = copy.deepcopy(board)
        print('=' * 59)
        if board[19-int(location_r), ord(location_c)-65] != 0:
            print("해당 위치는 이미 착수 되었습니다.")
            continue
        board[19-int(location_r), ord(location_c)-65] = 2
        if end2(board):
            print("P2 WIN")
        
        output_r, output_c = ai_predict(board)
        board[output_r][output_c] = 1
        print_board(board)
        print('=' * 59)
        print(f"착수한 위치 : {19-output_r}행 {chr(output_c + 65)}열")
        if end1(board):
            print('P1 WIN')
            
    except ValueError: print("error, try again")
    except IndexError: print("error, try again")