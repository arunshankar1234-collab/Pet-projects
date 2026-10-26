# LeetCode 560. Subarray Sum Equals K (Medium), v2: prefix sums + dict, O(n)
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
    # Big O(n) time complexity, Big O(n) space complexity.
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = dict()
        running_total = 0
        for index, num in enumerate(nums):
            prefix_sum[running_total] = prefix_sum.get(running_total, 0) + 1

            # Is there a sub array ending at index that sums to k?
            target = running_total + num - k
            if target in prefix_sum:
                count += prefix_sum[target]
            running_total += num
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
