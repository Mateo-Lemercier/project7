from random import choice





def StartGame_MorpionLike(rows_count:int=3, columns_count:int=3):
    """
    Description
    """
    
    rows: list[list[list[int]]] = []
    columns: list[list[list[int]]] = []
    diagonals: list[list[list[int]]] = []

    
    for bigloop in range(rows_count):
        
        rows.append([])

        for _ in range(columns_count):

            rows[bigloop].append([0])
    

    for bigloop in range(columns_count):

        columns.append([])

        for smallloop in range(rows_count):

            columns[bigloop].append(rows[smallloop][bigloop])
    
    
    for bigloop in range():
        print





StartGame_MorpionLike()