from typing import List
import collections

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


def test_case():
    case1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = group_anagrams(case1)
    print(result)