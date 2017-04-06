# coding=utf-8
"""
given an integer array, output all the unique pairs that sum up to a specific
value, k. pair_sum([1, 3, 2, 2], 4) returns 2 pairs [1, 3] and [2, 2]
"""
from nose.tools import assert_equal


def pair_sum(arr, val):
    """
    :param arr: integer array
    :param val: integer value
    :return: list of unique pairs from arr that sum to val
    """
    p = []
    # find compinations of pairs in arr
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == val:
                p.append([arr[i], arr[j]])
    if len(p) == 1:
        return len(p)
    else:
        for i in range(len(p)):
            p[i].sort()
        for i in range(len(p) - 1):
            matched = []
            for j in range(i + 1, len(p)):
                if p[i] == p[j]:
                    matched.append(j)
        # noinspection PyUnboundLocalVariable
        for i in matched:
            p.remove(p[i])
    return len(p)


class TestPair(object):
    """
    Test class
    """

    def test(self, sol):
        """
        runs a test on the function sol
        :param sol: function passed to the test class
        :return: 
        """
        assert_equal(
            sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        # print(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        # print(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print("All test cases passed")


t = TestPair()
t.test(pair_sum)
