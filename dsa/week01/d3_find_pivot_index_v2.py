# LeetCode 724. Find Pivot Index (Easy), v2: O(1) extra space
# Given a list of integers nums, return the pivot index: the index where the
# sum of all numbers strictly to its LEFT equals the sum of all numbers
# strictly to its RIGHT. The number at the pivot itself is in neither sum.
# If the pivot is at the very start, its left sum is 0 (and the same for the
# right sum at the very end).
# Return the LEFTMOST pivot index, or -1 if there is none.
#
# Example 1: nums = [1, 7, 3, 6, 5, 6]  -> 3   (left 1+7+3 = 11, right 5+6 = 11)
# Example 2: nums = [1, 2, 3]           -> -1
# Example 3: nums = [2, 1, -1]          -> 0   (left = 0, right 1 + -1 = 0)
#
# Constraints: 1 <= len(nums) <= 10^4; -1000 <= nums[i] <= 1000.

from typing import List


class Solution:
    # Big O(n) time, Big O(1) space
    def pivotIndex(self, nums: List[int]) -> int:
        runningTotal = 0
        total = sum(nums)
        for index, num in enumerate(nums):
            rightSums = total - (runningTotal + num)
            if rightSums == runningTotal:
                return index
            runningTotal += num
        return -1

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
        ([5], 0),
        ([1, -1, 4], 2),
        ([0, 0, 0], 0),
        ([-1, -1, 0, 1, 1, 0], 5),
    ]
    for nums, expected in tests:
        got = sol.pivotIndex(nums)
        print("PASS" if got == expected else "FAIL", nums, "->", got)
