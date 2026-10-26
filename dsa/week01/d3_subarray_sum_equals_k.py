# LeetCode 560. Subarray Sum Equals K (Medium)
# Given a list of integers nums and an integer k, return how many subarrays
# add up to exactly k.
# A subarray is a CONTIGUOUS, non-empty run of the list: [2, 3] is a subarray
# of [1, 2, 3, 4], but [1, 3] is not (it skips 2).
#
# Example 1: nums = [1, 1, 1], k = 2  -> 2   ([1, 1] starting at index 0, and at index 1)
# Example 2: nums = [1, 2, 3], k = 3  -> 2   ([1, 2] and [3])
#
# Constraints: 1 <= len(nums) <= 2 * 10^4; -1000 <= nums[i] <= 1000;
# -10^7 <= k <= 10^7. Numbers can be negative or zero.

from typing import List


class Solution:
    # Brute force solution Big O(n^2) time complexity. O(1) space complexity
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for index in range(len(nums)):
            running_total = 0
            for j in range(index, len(nums)):
                running_total += nums[j]
                if running_total == k:
                    count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([3], 3, 1),
        ([1, 2, 1, 2, 1], 3, 4),
        ([1, -1, 0], 0, 3),
        ([0, 0, 0], 0, 6),
        ([-1, -1, 1], 0, 1),
        ([1, 2, 3], 7, 0),
    ]
    for nums, k, expected in tests:
        got = sol.subarraySum(nums, k)
        print("PASS" if got == expected else "FAIL", nums, k, "->", got)
