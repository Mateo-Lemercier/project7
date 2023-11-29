# import timeit

# def loop_range():
#     list_1 = ["a", "b", "c", "d", "e"]
#     list_2 = [1, 2, 3, 4, 5]
#     text = ""
#     for loop in range(len(list_1)):
#         text += list_1[loop] + str(list_2[loop])
#     return text

# def loop_list():
#     list_1 = ["a", "b", "c", "d", "e"]
#     list_2 = [1, 2, 3, 4, 5]
#     text = ""
#     for element_1, element_2 in list(zip(list_1, list_2)):
#         text += element_1 + str(element_2)
#     return text

# time = timeit.timeit(loop_range, number=1000000)
# print(f"Range : {time:.6f}")
# time = timeit.timeit(loop_list, number=1000000)
# print(f"List : {time:.6f}")

print("\033[4m" + "a" + "\033[0m")