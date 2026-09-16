my_list = [64, 25, 12, 22, 11]

def swap(input_list, index1, index2):
    temp = input_list[index1]
    input_list[index1] = input_list[index2]
    input_list[index2] = temp
    return input_list
lowest_index = 0
for i in range(len(my_list)):
    if my_list[i] < my_list[lowest_index]:
        lowest_index = i

        