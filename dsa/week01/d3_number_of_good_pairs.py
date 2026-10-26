# LeetCode 1512. Number of Good Pairs (Easy)
# Given a list of integers nums, return the number of good pairs.
# A pair (i, j) is good if nums[i] == nums[j] and i < j.
#
# Example 1: nums = [1, 2, 3, 1, 1, 3]  -> 4   ((0,3), (0,4), (3,4), (2,5))
# Example 2: nums = [1, 1, 1, 1]        -> 6   (every pair of indexes)
# Example 3: nums = [1, 2, 3]           -> 0
#
# Constraints: 1 <= len(nums) <= 100; 1 <= nums[i] <= 100.

from typing import List


class Solution:
    # Big O(n) time complexity, Big O(n) space complexity
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = dict()
        total_pairs = 0
        for num in nums:
            total_pairs += seen.get(num, 0)
            seen[num] = seen.get(num, 0) + 1
        return total_pairs


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
        ([5], 0),
        ([2, 2], 1),
        ([1, 1, 1, 2, 2, 3], 4),
    ]
    for nums, expected in tests:
        got = sol.numIdenticalPairs(nums)
        print("PASS" if got == expected else "FAIL", nums, "->", got)
