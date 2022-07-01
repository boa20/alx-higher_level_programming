#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        return None
    elif (idx > len(my_list) - 1):
        return None
    else:
        return my_list[idx]

integers = [1, 2, 3, 4, 5]
print("Element at index {:d} is {}".format(5, element_at(integers, 5)))
print("Element at index {:d} is {}".format(-2, element_at(integers, -2)))
print("Element at index {:d} is {}".format(2, element_at(integers, 2)))
print("Element at index {:d} is {}".format(4, element_at(integers, 4)))
