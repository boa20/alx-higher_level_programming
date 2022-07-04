#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string
    new_string.pop('c')
    new_string.pop('C')
    return new_string

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun"))
