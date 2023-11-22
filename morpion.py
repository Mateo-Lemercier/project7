input_start: str = "\n\n\n"
input_end: str = "\n> "
num_to_text: list = ["-", "X", "O"]
player: int = 2

rows: list = [[[0], [0], [0]],
              [[0], [0], [0]],
              [[0], [0], [0]]]

columns: list = [[rows[0][0], rows[1][0], rows[2][0]],
                 [rows[0][1], rows[1][1], rows[2][1]],
                 [rows[0][2], rows[1][2], rows[2][2]]]

diagonals: list = [[rows[0][0], rows[1][1], rows[2][2]],
                   [rows[0][2], rows[1][1], rows[2][0]]]





def StartGame():
    global player

    row: list
    slot: list

    while True:

        gameboard: str = ""

        for row in rows:

            for slot in row:

                gameboard += num_to_text[slot[0]] + " "
            
            gameboard += "\n"
        
        print(input_start + gameboard)

        if CheckVictory():
            print("The Winner is Player " + str(player) + " !")
        
        elif CheckTie():
            print("It's a tie !")

        else:
            player = 3 - player
            AskPlay("What's your play, Player " + str(player) + " ? (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)")
            continue
        
        if not AskReplay("Wanna replay ? (o/n)"):
            break
        
        player = 2
        for row in rows:
            for slot in row:
                slot[0] = 0





def AskPlay(question:str):
    global input_start, input_end, rows, player
    
    while True:

        answer: str = input(question + input_end).lower()

        if answer not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            question = input_start + "That's not a valid play... (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)"
            continue
        
        play: int = int(answer)-1
        play_row: int = 1 - (play//3 - 1)
        play_column: int = play%3

        if rows[play_row][play_column][0] != 0:
            question = input_start + "That's not a valid play... (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)"
            continue
        
        rows[play_row][play_column][0] = player
        break





def CheckVictory() -> bool:
    global rows, columns, diagonals, player
    
    tocheck = [rows, columns, diagonals]

    for var in tocheck:

        for line in var:

            if line == [[player], [player], [player]]:
                return True
    
    return False





def CheckTie() -> bool:
    global rows

    for row in rows:
        if [0] in row:
            return False
    
    return True





def AskReplay(question:str) -> bool:
    
    authorized = ["o", "n"]
    
    while True:

        answer: str = input(question + input_end)

        if answer not in authorized:
            question = "That's not what I asked..."
            continue

        return answer == authorized[0]





StartGame()