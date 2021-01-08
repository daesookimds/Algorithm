from typing import List

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_some_in(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


def two_some_dict(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


def two_some_dict2(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


def two_some_pointer(nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right += 1
        else:
            return [left, right]
    # index has changed. so, it's not solution. just know the correct two sum value.





def test_case():
    case_nums = [2, 7, 11, 15]
    case_target = 9

    result = two_sum_brute_force(case_nums, case_target)
    print(result)

    test = 0
    for n in result:
        test += case_nums[n]
    print(test)

    result = two_some_in(case_nums, case_target)
    print(result)

    test = 0
    for n in result:
        test += case_nums[n]
    print(test)

    result = two_some_dict(case_nums, case_target)
    print(result)

    test = 0
    for n in result:
        test += case_nums[n]
    print(test)

    result = two_some_dict2(case_nums, case_target)
    print(result)

    test = 0
    for n in result:
        test += case_nums[n]
    print(test)

