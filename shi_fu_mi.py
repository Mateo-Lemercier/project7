from random import randint
input_start: str = "\n\n"
input_end: str = "\n> "
rockpaperscissors: list = ["r", "p", "s"]
possible_outcomes = [
    [2, 0, 1],
    [1, 2, 0],
    [0, 1, 2]
]
end_messages = [
    "You lost !",
    "You won...",
    "It's a tie..."
]





def StartGame():
    global input_start, input_end, possible_inputs, possible_outcomes
    
    while True:

        bot_play = randint(1, 3)
        user_play = AskPlay("What's your play ? (rock / r - paper / p - scissors / s)")

        print(input_start + ["Rock ! ", "Paper ! ", "Scissors ! "][bot_play-1] + end_messages[possible_outcomes[user_play-1][bot_play-1]])

        if not AskReplay("Wanna replay ? (o/n)"):
            break





def AskPlay(question:str):
    global input_start, input_end, rockpaperscissors

    while True:

        answer: str = input(input_start + question + input_end).lower().replace("rock", "r").replace("paper", "p").replace("scissors", "s")

        if answer not in rockpaperscissors:
            question = "That's not a valid play... (rock / r - paper / p - scissors / s)"
            continue
        
        return rockpaperscissors.index(answer)+1





def AskReplay(question:str) -> bool:
    
    authorized = ["o", "n"]
    
    while True:

        answer: str = input(question + input_end)

        if answer not in authorized:
            question = input_start + "That's not what I asked..."
            continue

        return answer == authorized[0]





StartGame()