# coding=utf-8
"""
Find the missing element
"""


def finder(arr1, arr2):
    """
    :param arr1: original array
    :param arr2: shuffled array with random element missing
    :return: missing element
    """
    a = set(arr1)
    b = set(arr2)
    return a.difference(b)
