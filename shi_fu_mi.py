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
    global input_start, input_end, possible_outcomes, rockpaperscissors
    
    while True:

        bot_play = randint(1, 3)
        user_play = rockpaperscissors.index(AskInput(input_start + "What's your play ? (rock / r / paper / p / scissors / s)", ["rock", "r", "paper", "p", "scissors", "s"]).replace("rock", "r").replace("paper", "p").replace("scissors", "s"))+1

        print(input_start + ["Rock ! ", "Paper ! ", "Scissors ! "][bot_play-1] + end_messages[possible_outcomes[user_play-1][bot_play-1]])

        if AskInput("Wanna replay ? (o / n)", ["o", "n"]) != "o":
            break



def AskInput(question:str, authorized_inputs:list) -> str:
    global input_start, input_end
    
    while True:
        answer: str = input(question + input_end).lower()

        if answer in authorized_inputs:
            return answer
        
        question = input_start + "That's not what I asked... ("
        for authorized in authorized_inputs:
            question += authorized + " / "
        question = question[:-3] + ")"





StartGame()