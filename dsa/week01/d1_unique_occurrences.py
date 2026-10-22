# LeetCode 1207. Unique Number of Occurrences (Easy)
# Given a list of integers arr, return True if the number of times each value
# appears is unique (no two values appear the same number of times), else False.
#
# Example 1: arr = [1, 2, 2, 1, 1, 3]  -> True   (1 appears 3 times, 2 twice, 3 once)
# Example 2: arr = [1, 2]              -> False  (1 and 2 both appear once)
#
# Constraints: 1 <= len(arr) <= 1000; -1000 <= arr[i] <= 1000.

from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for number in arr:
            count[number] = count.get(number, 0) + 1
        
        result = set()
        for key, value in count.items():
            if value in result:
                return False
            result.add(value)
        
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
        ([5], True),
        ([1, 1, 2, 2, 3], False),
    ]
    for arr, expected in tests:
        got = sol.uniqueOccurrences(arr)
        print("PASS" if got == expected else "FAIL", arr, "->", got)
