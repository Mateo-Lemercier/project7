import timeit

def loop_range():
    list_1 = ["a", "b", "c", "d", "e"]
    text = ""
    for loop in range(len(list_1)):
        text += list_1[loop]
    return text

def loop_list():
    list_1 = ["a", "b", "c", "d", "e"]
    text = ""
    for element_1 in list_1:
        text += element_1
    return text

time = timeit.timeit(loop_range, number=1000000)
print(f"Range : {time:.6f}")
time = timeit.timeit(loop_list, number=1000000)
print(f"List : {time:.6f}")