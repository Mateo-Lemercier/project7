
def AskInt(question:str) -> int:
    """
    Description
    """

    statement: str = question
    answer: str

    while True:

        answer = input(statement + "\n> ")

        if (answer.isdecimal()): # Checking if the answer is an int
            return int(answer)
        
        statement = "\nPlease enter a valid number"
        





def AskInt_Minimum(question:str, minimum:int) -> int:
    """
    Description
    """

    statement: str = question
    value: int

    while True:

        value = AskInt(statement)

        if value >= minimum:
            return value
        
        statement = "\nPlease enter a number above or equal to " + str(minimum)





def AskInt_Maximum(question:str, maximum:int) -> int:
    """
    Description
    """

    statement: str = question
    value: int

    while True:

        value = AskInt(statement)

        if value <= maximum:
            return value
        
        statement = "\nPlease enter a number below or equal to " + str(maximum)





def AskInt_Range(question:str, minimum:int, maximum:int) -> int:
    """
    Description
    """

    statement: str = question
    value: int

    while True:

        value = AskInt(statement)

        if (minimum <= value <= maximum):
            return value
        
        statement = "\nPlease enter a number between " + str(minimum) + " and " + str(maximum)





def AskInput(question:str, authorized:list[str]) -> str:
    """
    Description
    """

    statement: str = question
    statement_wrong_answer: str = "\nPlease enter "
    for loop in range(len(authorized)-2): statement_wrong_answer += authorized[loop] + ", "
    statement_wrong_answer += str(authorized[-2]) + " or " + str(authorized[-1])
    answer: str

    while True:

        answer = input(statement + "\n> ")

        if answer in authorized:
            return answer

        statement = statement_wrong_answer





print(AskInput("askinput", ["a", "b", "c", "d"]))