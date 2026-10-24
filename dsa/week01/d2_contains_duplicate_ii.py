# LeetCode 219. Contains Duplicate II (Easy)
# Given a list of integers nums and an integer k, return True if there are two
# different indices i and j where nums[i] == nums[j] and abs(i - j) <= k.
# In other words: is some value repeated within k positions of itself?
#
# Example 1: nums = [1, 2, 3, 1],       k = 3  -> True   (indices 0 and 3, distance 3)
# Example 2: nums = [1, 0, 1, 1],       k = 1  -> True   (indices 2 and 3, distance 1)
# Example 3: nums = [1, 2, 3, 1, 2, 3], k = 2  -> False  (every repeat is 3 apart)
#
# Constraints: 1 <= len(nums) <= 10^5; -10^9 <= nums[i] <= 10^9; 0 <= k <= 10^5.

from typing import List


class Solution:
    # Big O(n) time complexity, O(n) space complexity
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for index, num in enumerate(nums):
            if num in seen and index - seen[num] <= k:
                    return True
            seen[num] = index
        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([1, 2, 3, 1, 1], 1, True),
        ([5], 0, False),
        ([7, 7], 0, False),
    ]
    for nums, k, expected in tests:
        got = sol.containsNearbyDuplicate(nums, k)
        print("PASS" if got == expected else "FAIL", nums, k, "->", got)
