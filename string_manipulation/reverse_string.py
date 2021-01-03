from typing import List


def reverse_list_string_using_swap(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_list_string(s: List[str]) -> None:
    s.reverse()


def reverse_string1(s: str) -> str:
    s = s[::-1]
    return s


def reverse_string2(s: str) -> str:
    # can't re-define error raise
    # this way vaild in big O(1) space complexity
    s[:] = s[::-1]
    return s


def test_case():
    case1 = ['h', 'e', 'l', 'l', 'o']
    case2 = ['H', 'a', 'n', 'n', 'h']

    reverse_list_string_using_swap(case1)
    print(case1)

    reverse_list_string(case2)
    print(case2)


    case3 = 'hello'
    case4 = 'Hannah'

    case3 = reverse_string1(case3)
    print(case3)

    # reverse_string2(case4)
    # print(case4)



