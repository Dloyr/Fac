#!/usr/bin/python3

def decompresse(number_list):
    full_number = []

    for index in range(len(number_list)):
        number, value = number_list[index]
        for index_b in range(number):
            full_number.append(value)
    return full_number

print(decompresse([[4, 1], [1, 2], [6, 3], [3, 1], [3, 2]]))