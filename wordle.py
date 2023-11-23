from random import choice





def StartGame():

    word: str = choice(["MIAOU", "LIVRE", "PENDU"])

    while True:

        gameboard: str = ""

        for loop in range(6):

            gameboard += "- - - - -\n"
        
        print(gameboard)
        break





StartGame()