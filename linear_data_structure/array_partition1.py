from typing import List

def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


def arrayPairSumEven(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


def arrayPairSumPythonStyle(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


def test_case():

    case = [1, 4, 3, 2]

    result1 = arrayPairSum(case)
    result2 = arrayPairSumEven(case)
    result3 = arrayPairSumPythonStyle(case)

    print(result1, result2, result3)


