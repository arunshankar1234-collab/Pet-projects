# LeetCode 974. Subarray Sums Divisible by K (Medium)
# Given a list of integers nums and an integer k, return how many non-empty
# contiguous subarrays have a sum that is divisible by k (sum % k == 0).
#
# Example 1: nums = [4, 5, 0, -2, -3, 1], k = 5  -> 7
#   ([4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3],
#    [-2, -3])
# Example 2: nums = [5], k = 9  -> 0
#
# Constraints: 1 <= len(nums) <= 3 * 10^4; -10^4 <= nums[i] <= 10^4;
# 2 <= k <= 10^4. Numbers can be negative.

from typing import List


class Solution:
    # O(n) time complexity, O(k) space
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_total = 0
        remainder = dict()
        count = 0
        for index, num in enumerate(nums):
            rem = running_total % k
            remainder[rem] = remainder.get(rem, 0) + 1
            # Is there a sub-array ending at index whose sum is divisible by k?
            target = (running_total + num) % k
            if target in remainder:
                count += remainder[target]
            running_total += num
        return count


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([4, 5, 0, -2, -3, 1], 5, 7),
        ([5], 9, 0),
        ([5], 5, 1),
        ([1, 2, 3], 3, 3),
        ([0, 0], 2, 3),
        ([-1, 2, 9], 2, 2),
        ([2, -2, 2, -4], 6, 2),
    ]
    for nums, k, expected in tests:
        got = sol.subarraysDivByK(nums, k)
        print("PASS" if got == expected else "FAIL", nums, k, "->", got)
