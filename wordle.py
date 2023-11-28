# Reset = \033[0m
# Bold = \033[1m

# Gray = \033[90m
# Red = \033[91m
# Green = \033[92m
# Yellow = \033[93m
# Blue = \033[94m
# Pink = \033[95m
# Cyan = \033[96m

from generic_functions import *
from random import choice
import os





def StartGame_Wordle():
    """
    Description
    """

    while True:

        print(Worlde_Play(6))
        
        if not AskReplay():
            break





def Worlde_Play(tries_count:int):
    """
    Description
    """

    word: list[str] = [letter for letter in choice(["MIAOU", "LIVRE", "PENDU"])]
    tries: list[list[str]] = [["-", "-", "-", "-", "-"] for _ in range(6)]
    tries_style: list[list[str]] = [["", "", "", "", ""] for _ in range(6)]
    index: int

    Worlde_Gameboard(tries_count, tries, tries_style)

    for bigloop in range(tries_count):

        tries[bigloop] = [letter for letter in AskInput("", "abcdefghijklmnopqrstuvwxyz", 5, False).upper()]
        
        for smallloop in range(5):
            
            index = "".join(word).find(tries[bigloop][smallloop])

            if index != -1:
                 
                print(tries[bigloop][index], word[index])
                if tries[bigloop][index] == word[index]:
                    tries_style[bigloop][smallloop] = "\033[1m\033[96m"
                    continue
                
                tries_style[bigloop][smallloop] = "\033[1m\033[93m"
                continue
            
            tries_style[bigloop][smallloop] = "\033[1m\033[91m"

        Worlde_Gameboard(tries_count, tries, tries_style)

        if tries[bigloop] == word:
            return "You found the word in " + str(bigloop+1) + " tries"
    
    return "You didn't find my word, it was " + "".join(word).capitalize()





def Worlde_Gameboard(tries_count:int, tries:list[list[str]], tries_style:list[list[str]]):
    """
    Description
    """
    os.system("cls")

    gameboard: str = ""
    
    for bigloop in range(tries_count):

        for smallloop in range(5):

            gameboard += tries_style[bigloop][smallloop] + tries[bigloop][smallloop] + "\033[0m "
        
        gameboard += "\n"
    
    gameboard = gameboard[:-2]

    print(gameboard)





if __name__ == "__main__":
    StartGame_Wordle()