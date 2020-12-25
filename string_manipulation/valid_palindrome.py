import re
import timeit
import collections
from typing import Deque


def is_palindrome_using_list(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # recognize valid palindrome
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome_using_deque(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def is_palindrome_using_slicing(s: str) -> bool:
    s = s.lower()
    # remove unnecessary char using regex
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


def add_timer(func):
    start = timeit.default_timer()
    result = func
    end = timeit.default_timer()

    return result, start - end


def test_case():
    case1 = 'A man, a plan, a canal: Panama'
    case2 = 'race a car'

    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_list(case1))))
    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_list(case2))))

    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_deque(case1))))
    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_deque(case2))))

    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_slicing(case1))))
    print('(결과 , 실행시간) : {}'.format(add_timer(is_palindrome_using_slicing(case2))))
