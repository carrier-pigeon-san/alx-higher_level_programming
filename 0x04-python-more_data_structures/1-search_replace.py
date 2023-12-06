#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return my_list
    new_list = []
    for i in my_list:
        if i is search:
            new_list += [replace]
        else:
            new_list += [i]
    return new_list
