#%%
import numpy as np
BOARD_SIZE = 3
ZERO_SYMBOL = 'X'
ONE_SYMBOL = 'O'
board = np.array([[0,0,0],[1,0,0,],[0,0,0]])
#%%
def draw_board(board_list):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(ONE_SYMBOL, end=" " ) if board_list[i][j] == 1 else print(ZERO_SYMBOL, end=" " )
        print("\n")

draw_board(board)

#%%
def get_board_after_move(board_list, index_i, index_j, value):
    board_list[index_i][index_j] = value
    return board_list
new_board = get_board_after_move(board, 1,1,1)
draw_board(new_board)

#%%

