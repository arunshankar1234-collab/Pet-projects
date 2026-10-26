# LeetCode 525. Contiguous Array (Medium)
# Given a list nums that contains only 0s and 1s, return the LENGTH of the
# longest contiguous subarray that has the same number of 0s and 1s.
# Return 0 if there is no such subarray.
#
# Example 1: nums = [0, 1]           -> 2   ([0, 1])
# Example 2: nums = [0, 1, 0]        -> 2   ([0, 1] or [1, 0])
# Example 3: nums = [0, 0, 1, 0, 0, 0, 1, 1] -> 6   ([1, 0, 0, 0, 1, 1])
#
# Constraints: 1 <= len(nums) <= 10^5; nums[i] is 0 or 1.

from typing import List


class Solution:
    # O(n) time complexity, O(n) space 
    def findMaxLength(self, nums: List[int]) -> int:
        running_total = 0
        prefix_sum = dict()
        largest = 0
        for index, num in enumerate(nums):
            if running_total not in prefix_sum:
                prefix_sum[running_total] = index
            num = -1 if num == 0 else 1
            target = running_total + num
            if target in prefix_sum:
                difference = (index - prefix_sum[target]) + 1
                largest = max(largest, difference)
            running_total += num
        return largest
            

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([0, 1], 2),
        ([0, 1, 0], 2),
        ([0, 0, 1, 0, 0, 0, 1, 1], 6),
        ([0], 0),
        ([1, 1, 1], 0),
        ([0, 0, 1, 1], 4),
        ([1, 0, 1, 1, 0, 0], 6),
        ([1, 1, 0, 1, 1], 2),
    ]
    for nums, expected in tests:
        got = sol.findMaxLength(nums)
        print("PASS" if got == expected else "FAIL", nums, "->", got)
