# LeetCode 49. Group Anagrams (Medium), version 2
# Same problem, but build the key by COUNTING letters instead of sorting,
# so the time is O(n * k) instead of O(n * k log k).
#
# Given a list of strings strs, group the anagrams together.
# You can return the groups in any order, and the words in each group in any order.
#
# Example 1: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#            -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example 2: strs = [""]   -> [[""]]
# Example 3: strs = ["a"]  -> [["a"]]
#
# Constraints: 1 <= len(strs) <= 10^4; 0 <= len(strs[i]) <= 100;
# lowercase English letters only.

from typing import List


class Solution:
    # Big O(n.k) time complexity, Big O(n) 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for word in strs:
            key = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                key[index] += 1
            groups.setdefault(tuple(key), []).append(word)
        return list(groups.values())

def normalise(groups):
    # Sort words inside each group, then sort the groups, so order doesn't matter.
    if groups is None:
        return None
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ab", "ba", "abc", "cab", "x"], [["ab", "ba"], ["abc", "cab"], ["x"]]),
        (["aab", "abb"], [["aab"], ["abb"]]),
    ]
    for strs, expected in tests:
        got = sol.groupAnagrams(strs)
        print("PASS" if normalise(got) == normalise(expected) else "FAIL", strs, "->", got)
