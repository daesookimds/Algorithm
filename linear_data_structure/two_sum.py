from typing import List

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def test_case():
    case_nums = [2, 7, 11, 15]
    case_target = 9

    result = two_sum_brute_force(case_nums, case_target)
    print(result)

    test = 0
    for n in result:
        test += case_nums[n]

    print(test)