from random import choice

input_start: str = "\n\n\n"
input_end: str = "\n> "
num_to_text: list = ["-", "X", "O"]

rows: list = [[[0], [0], [0]],
              [[0], [0], [0]],
              [[0], [0], [0]]]

columns: list = []
for loop in range(len(rows)):
    columns.append([])
    for smallloop in range(len(rows[loop])):
        columns[loop].append(rows[smallloop][loop])

diagonals:list = [[], []]
for loop in range(len(rows[0])):
    diagonals[0].append(rows[loop][loop])
    diagonals[1].append(rows[loop][len(rows[0])-loop-1])





def StartGame():

    row: list
    slot: list
    winner: bool
    gameboard: str

    while True:

        gameboard = ""

        for row in rows:

            for slot in row:

                gameboard += num_to_text[slot[0]] + " "
            
            gameboard += "\n"
        
        print(input_start + gameboard)
        winner = CheckVictory()

        if winner:
            print("The Winner is the " + ["player", "robot"][winner-1] + " !")
            pass
        
        elif CheckTie():
            print("It's a tie !")

        else:
            
            AskPlay("What's your play, player ? (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)")
            winner = CheckVictory()
            
            if not winner:
                BotPlay()
            
            continue
        
        if not AskReplay():
            break
        
        for row in rows:
            for slot in row:
                slot[0] = 0





def AskPlay(question:str):
    global input_start, input_end, rows

    answer: str
    play: int
    play_row: int
    play_column: int
    
    while True:

        answer = input(question + input_end).lower()

        if answer not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            question = input_start + "That's not a valid play... (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)"
            continue
        
        play = int(answer)-1
        play_row = 1 - (play//3 - 1)
        play_column = play%3

        if rows[play_row][play_column][0] != 0:
            question = input_start + "That's not a valid play... (1=bottomleft - 2=bottom - 3=bottomright - 4=left - 5=middle - 6=right - 7=topleft - 8=top - 9=topright)"
            continue
        
        rows[play_row][play_column][0] = 1
        break





def BotPlay():
    global rows, columns, diagonals
    
    tocheck = [rows, columns, diagonals]

    for var in tocheck:

        for line in var:

            if line.count([2]) == 2:

                for slot in line:
                    
                    if slot[0] == 0:
                        
                        slot[0] = 2
                        return
            
            elif line.count([1]) == 2:

                for slot in line:
                    
                    if slot[0] == 0:
                        
                        slot[0] = 2
                        return
    
    playables: list = []

    for row in rows:

        for slot in row:

            if slot[0] == 0:
                playables.append(slot)
    
    if playables:
        
        choice(playables)[0] = 2
        return
    
    return





def CheckVictory() -> bool:
    global rows, columns, diagonals
    
    tocheck = [rows, columns, diagonals]

    for var in tocheck:

        for line in var:

            for loop in range(1,3):

                if line == [[loop], [loop], [loop]]:
                    return loop
    
    return False





def CheckTie() -> bool:
    global rows

    for row in rows:
        if [0] in row:
            return False
    
    return True





def AskReplay() -> bool:
    
    question: str = "Wanna replay ? (o/n)"
    authorized = ["o", "n"]
    
    while True:

        answer: str = input(question + input_end)

        if answer not in authorized:
            question = "That's not what I asked..."
            continue

        return answer == authorized[0]





StartGame()