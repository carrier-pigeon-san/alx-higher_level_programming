#!/usr/bin/python3
"""This module contains the function find_peak() that finds the peak in a list
of unsorted integers"""


def find_peak(list_of_integers):
    """This function finds the peak in a list of unsorted intgers"""
    if len(list_of_integers) == 0:
        return
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    mid = int(len(list_of_integers) / 2)
    if list_of_integers[mid - 1] >= list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
