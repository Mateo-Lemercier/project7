from generic_functions import *
from random import choice
import os

pieces: list[str] = ["-", "X", "O"]





def MorpionLike_StartGame(rows_count:int=3, columns_count:int=3, winning_count:int=3):
    """
    Starts a MorpionLike game.
    """

    board: list[list[int]]
    color_board: list[list[str]]
    empty_board: list[list[int]]
    
    while True:

        board = [[0 for _ in range(columns_count)] for _ in range(rows_count)]
        color_board = [["" for _ in range(columns_count)] for _ in range(rows_count)]
        empty_board = [[r, c] for r in range(rows_count) for c in range(columns_count)]

        print(MorpionLike_Play(board, color_board, empty_board, rows_count, columns_count, winning_count))

        if not AskReplay():
            break





def MorpionLike_Play(board:list[list[int]], color_board:list[list[str]], empty_board:list[list[int]], rows_count:int=3, columns_count:int=3, winning_count:int=3) -> str:
    """
    Plays a MorpionLike game.
    """

    user_row: int
    user_column: int
    bot_row: int
    bot_column: int

    while True:

        user_row, user_column = MorpionLike_AskNotAlreadyPlayed(board, color_board, empty_board, rows_count, columns_count)
        board[user_row][user_column] = 1
        empty_board.remove([user_row, user_column])

        if MorpionLike_CheckVictory(board, color_board, user_row, user_column, 1, rows_count, columns_count, winning_count):
            print(MorpionLike_GameBoard(board, color_board, rows_count, columns_count))
            return "Player won !"
        
        bot_row, bot_column = MorpionLike_BotPlay(empty_board)
        board[bot_row][bot_column] = 2
        empty_board.remove([bot_row, bot_column])

        if MorpionLike_CheckVictory(board, color_board, bot_row, bot_column, 2, rows_count, columns_count, winning_count):
            print(MorpionLike_GameBoard(board, color_board, rows_count, columns_count))
            return "Bot won !"





def MorpionLike_GameBoard(board:list[list[int]], color_board:list[list[str]], rows_count:int, columns_count:int) -> str:
    """
    Returns a printable MorpionLike game's gameboard as a string.
    """
    os.system("cls")
    global pieces

    gameboard: str = ""

    for bigloop in range(rows_count):

        for smallloop in range(columns_count):

            gameboard += color_board[bigloop][smallloop] + pieces[board[bigloop][smallloop]] + "\033[0m "
        
        gameboard += "\n"
    
    return gameboard





def MorpionLike_CheckVictory(board:list[list[int]], color_board:list[list[str]], player_row:int, player_column:int, player:int, rows_count:int, columns_count:int, winning_count:int) -> bool:
    """
    Checks if there's a victory arround the given move (player_row & player_column).
    """

    player_row_move: int
    player_column_move: int
    winning_streak: list
    moves: list[list[int]] = [[1, -1], [0, -1], [-1, -1], [-1, 0]]
    
    for row_move, column_move in moves:

        winning_streak = []
        player_row_move = player_row + (row_move * winning_count)
        player_column_move = player_column + (column_move * winning_count)
        
        for _ in range(2*winning_count - 1):
            
            player_row_move -= row_move
            player_column_move -= column_move

            if not (0 <= player_row_move < rows_count) or not (0 <= player_column_move < columns_count):
                continue

            if board[player_row_move][player_column_move] != player:
                winning_streak = []
                continue

            winning_streak.append([player_row_move, player_column_move])

            if len(winning_streak) == winning_count:
                break
        
        else: continue

        for row, column in winning_streak:
            color_board[row][column] = "\033[1m\033[9" + ["4", "1"][player-1] + "m"
        
        return True
        
    return False





def MorpionLike_AskNotAlreadyPlayed(board:list[list[int]], color_board:list[list[str]], empty_board:list[list[int]], rows_count:int, columns_count:int) -> list[int]:
    """
    Asks the user for the row and column he wants to play at.

    If the slot's already taken, it asks again.
    """

    user_row: int
    user_column: int
    statement: str = ""

    while True:

        print(MorpionLike_GameBoard(board, color_board, rows_count, columns_count))

        if statement:
            print(statement)
        
        user_row = AskInt_Range("1/2 : In which row would you like to play ?", 1, rows_count)-1
        user_column = AskInt_Range("2/2 : In which column would you like to play ?", 1, columns_count)-1

        if [user_row, user_column] in empty_board:
            return [user_row, user_column]

        statement = "Someone already played there ! Please play somewhere else..."





def MorpionLike_BotPlay(empty_board:list[list[int]]) -> list[int]:
    """
    For now, there's no algorithms so this function just get a random available row + column.
    """

    return choice(empty_board)





if __name__ == "__main__":
    MorpionLike_StartGame()