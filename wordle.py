from generic_functions import *
from random import choice
import os





def Wordle_StartGame():
    """
    Starts a Worlde's game.
    """

    with open("wordle_words.txt", "r") as file:
        words = file.readlines()

    while True:

        print(Worlde_Play(words, 6))
        
        if not AskReplay():
            break





def Worlde_Play(words:list[str], tries_count:int) -> str:
    """
    Plays a Wordle's game.
    """
    
    word: list[str] = [letter for letter in choice(words)[:-1].upper()]
    tries: list[list[str]] = [["-", "-", "-", "-", "-"] for _ in range(6)]
    tries_style: list[list[str]] = [["", "", "", "", ""] for _ in range(6)]
    tries_letters: dict[str, int]
    
    print(Worlde_GameBoard(tries_count, tries, tries_style))

    for bigloop in range(tries_count):

        tries[bigloop] = Wordle_AskExistingWord(words)
        tries_letters = {}
        for letter in word:
            if letter not in tries_letters:
                tries_letters[letter] = 1
                continue
            tries_letters[letter] += 1

        for smallloop in range(len(word)):

            if tries[bigloop][smallloop] == word[smallloop]:

                tries_style[bigloop][smallloop] = "\033[1m\033[96m"
                tries_letters[tries[bigloop][smallloop]] -= 1

        for smallloop in range(len(word)):
            
            if tries[bigloop][smallloop] != word[smallloop]:
                
                if tries[bigloop][smallloop] in tries_letters:

                    if tries_letters[tries[bigloop][smallloop]]:

                        tries_style[bigloop][smallloop] = "\033[1m\033[93m"
                        tries_letters[tries[bigloop][smallloop]] -= 1
                        continue
                
                tries_style[bigloop][smallloop] = "\033[1m\033[91m"

        print(Worlde_GameBoard(tries_count, tries, tries_style))

        if tries[bigloop] == word:
            return "You found the word in " + str(bigloop+1) + " tries"
    
    return "You didn't find my word, it was \033[1m\033[4m\033[96m" + "".join(word) + "\033[0m"





def Worlde_GameBoard(tries_count:int, tries:list[list[str]], tries_style:list[list[str]]) -> str:
    """
    Returns a printable Worlde's gameboard as a string.
    """
    os.system("cls")

    gameboard: str = ""
    
    for bigloop in range(tries_count):

        for smallloop in range(5):

            gameboard += tries_style[bigloop][smallloop] + tries[bigloop][smallloop] + "\033[0m "
        
        gameboard += "\n"
    
    return gameboard[:-1]





def Wordle_AskExistingWord(words:list[str]) -> str:
    """
    Description
    """

    statement: str = ""
    answer: str
    word: str

    while True:

        if statement:

            answer = AskInput_str(statement, "on", 1, False)

            if answer == "o":
                
                words.append(word + "\n")
                with open("wordle_words.txt", "a") as file:
                    file.write(word + "\n")

                return [letter for letter in word]

        word = AskInput_str("", "abcdefghijklmnopqrstuvwxyz", 5, False).upper()

        if word + "\n" in words:
            return [letter for letter in word]
        
        statement = "I don't know this word, does it really exist ? (o/n) - Please don't lie"





if __name__ == "__main__":
    Wordle_StartGame()