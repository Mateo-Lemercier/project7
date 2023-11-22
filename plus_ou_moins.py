from random import randint
from math import floor, sqrt
input_start: str = "\n\n"
input_end: str = "\n> "





def StartGame():

    while True:

        range: list = AskRange("Give me a range of numbers I can choose from (example: 1, 100)")
        range_scale = range[1] - range[0]

        if 1 <= range_scale <= 19:
            guesses: int = 3
        
        else:
            guesses: int = 4 + floor(sqrt((range_scale)/10 - 2))

        AskGuess(range, guesses)

        if not AskReplay("Wanna replay ? (o/n)"):
            break





def AskGuess(range:list, guesses:int):
    
    number: int = randint(range[0], range[1])
    guesses_left: int = guesses
    end: bool = False

    while not end:
            
        if guesses_left == 1:
            try_part: str = " try left)"
        else:
            try_part: str = " tries left)"
        

        guess: int = AskInt("What's your guess ? (You have " + str(guesses_left) + try_part, range)
        guesses_left -= 1

        if guess == number:
            print(input_start + "You found my number in " + str(guesses - guesses_left) + " guesses !")
            return True
        
        elif guesses_left == 0:
            print(input_start + "You haven't found my number: It was " + str(number) + " !")
            return False
        
        if guess < number:
            compare_part: str = "bigger"
        
        else: # guess > number
            compare_part: str = "lower"
        
        print("My number is " + compare_part + " than " + str(guess))





def AskRange(question:str) -> list:
    global input_start, input_end

    while True:
        answer: str = input(input_start + question + input_end).replace(" ", "")
        find_index: int = answer.find(",")

        if answer == "":
            answer = "1,100"
            find_index = 1

        if find_index == -1:
            question = "There is no comma... Please, give me a valid range (example : 1, 100)"
            continue

        answer_part1: str = answer[:find_index]
        answer_part2: str = answer[find_index+1:]

        if not (answer_part1.isdecimal() and answer_part2.isdecimal()):
            question = "These aren't valid numbers... Please, give me a valid range (example : 1, 100)"
            continue
    
        min: int = int(answer_part1)
        max: int = int(answer_part2)

        if min >= max:
            question = "The minimum should be below the maximum... Please, give me a valid range (example : 1, 100)"
            continue    

        return [min, max]





def AskInt(question:str, range:list) -> int:
    global input_start, input_end

    while True:

        answer: str = input(input_start + question + input_end)

        if not answer.isdecimal():
            question = "That's not a number... Please, give me a valid guess"
            continue

        guess: int = int(answer)

        if guess < range[0] or guess > range[1]:
        # if not (range[0] <= guess <= range[1]):
            question ="This number isn't between " + str(range[0]) + " and " + str(range[1]) + "... Please, give me a valid guess"
            continue

        return guess





def AskReplay(question:str) -> bool:
    
    authorized = ["o", "n"]
    
    while True:

        answer: str = input(question + input_end)

        if answer not in authorized:
            question = "That's not what I asked..."
            continue

        return answer == authorized[0]





StartGame()