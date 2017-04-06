# coding=utf-8
"""
Interview Question - anagram check
"""

from nose.tools import assert_equal


class AnagramTest(object):
    """
    Anagram Test Class
    """

    @staticmethod
    def test(sol):
        """
        test cases for the anagram method
        :param sol: anagram method
        :return: nothing
        """
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("All test cases passed")


def anagram(s1, s2):
    """
    check if s1 and s2 are anagrams
    :param s1: a string
    :param s2: a string
    :return: if s1 and s2 are anagrams return True else return False
    """
    l1 = []
    l2 = []
    for s1_letter in s1:
        if s1_letter != " ":
            l1.append(s1_letter)
    for s2_letter in s2:
        if s2_letter != " ":
            l2.append(s2_letter)
    l1.sort()
    l2.sort()
    return l1 == l2

t = AnagramTest()
t.test(anagram)
