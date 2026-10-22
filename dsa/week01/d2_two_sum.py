# LeetCode 1. Two Sum (Easy)
# Given a list of integers nums and an integer target, return the indices of
# the two numbers that add up to target.
# Each input has exactly one answer, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1: nums = [2, 7, 11, 15], target = 9  -> [0, 1]   (2 + 7 = 9)
# Example 2: nums = [3, 2, 4],      target = 6  -> [1, 2]   (2 + 4 = 6)
# Example 3: nums = [3, 3],         target = 6  -> [0, 1]
#
# Constraints: 2 <= len(nums) <= 10^4; -10^9 <= nums[i], target <= 10^9;
# exactly one valid answer exists.

from typing import List


class Solution:
    # Time O(n), space O(n): one pass, dict of value -> index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums): # O(n) scan
            needed = target - num 
            if needed in seen: # O(1) lookup
                return [seen[needed], index]
            seen[num] = index
            
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]
    for nums, target, expected in tests:
        got = sol.twoSum(nums, target)
        ok = got is not None and sorted(got) == expected
        print("PASS" if ok else "FAIL", nums, target, "->", got)
