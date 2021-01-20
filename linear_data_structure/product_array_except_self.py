from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
        print(1, i, p, out)

    p = 1

    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
        print(2, i, p, out)

    return out


def test_case():

    case = [1, 2, 3, 4]
    out = productExceptSelf(case)
    print(out)