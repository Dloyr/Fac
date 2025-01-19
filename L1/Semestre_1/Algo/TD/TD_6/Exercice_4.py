#!/usr/bin/python3

def compresse(full_number: list)-> list[tuple[int: any]]:
    compressed_list = []
    iteration = 1
    if full_number == []:
        return compressed_list

    for index in range(len(full_number) - 1):
        if full_number[index] == full_number[index + 1]:
            iteration += 1
        elif full_number[index] != full_number[index + 1]:
            compressed_list.append([iteration, full_number[-1]])
            iteration = 1

    print(compressed_list)

compresse([1,1,1,1,2,3,3,3,3,3,3,1,1,1,2,2,2])

