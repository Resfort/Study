my_list = [64, 25, 12, 22, 11]

def swap(input_list, index1, index2):
    temp = input_list[index1]
    input_list[index1] = input_list[index2]
    input_list[index2] = temp