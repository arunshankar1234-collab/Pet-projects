# LeetCode 1636. Sort Array by Increasing Frequency (Easy)
# Given a list of integers nums, sort it so that values that appear fewer
# times come first. If two values appear the same number of times, put the
# LARGER value first. Return the sorted list.
#
# Example 1: nums = [1, 1, 2, 2, 2, 3]  -> [3, 1, 1, 2, 2, 2]
#            (3 appears once, 1 twice, 2 three times)
# Example 2: nums = [2, 3, 1, 3, 2]     -> [1, 3, 3, 2, 2]
#            (2 and 3 both appear twice, so the larger one, 3, goes first)
#
# Constraints: 1 <= len(nums) <= 100; -100 <= nums[i] <= 100.

from typing import List


class Solution:
    # Big O(n) to count, Big O(k log k) to sort if there are k distinct numbers, Big O(n.k) space
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = dict()
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        result = list(counts.items())
        sorted_list = sorted(result, key=lambda pair: (pair[1], -pair[0]))
        result = []
        for number, frequency in sorted_list:
            result.extend([number] * frequency)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
        ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
        ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
        ([7], [7]),
        ([4, 4, 4], [4, 4, 4]),
        ([1, 2, 3], [3, 2, 1]),
    ]
    for nums, expected in tests:
        got = sol.frequencySort(nums)
        print("PASS" if got == expected else "FAIL", nums, "->", got)
