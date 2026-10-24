# LeetCode 238. Product of Array Except Self (Medium)
# Given a list of integers nums, return a list answer where answer[i] is the
# product of every element of nums except nums[i].
# You must not use division, and it must run in O(n) time.
#
# Example 1: nums = [1, 2, 3, 4]       -> [24, 12, 8, 6]
# Example 2: nums = [-1, 1, 0, -3, 3]  -> [0, 0, 9, 0, 0]
#
# Constraints: 2 <= len(nums) <= 10^5; -30 <= nums[i] <= 30;
# every product fits in a 32-bit integer.
# Follow-up: can you do it with O(1) extra space? (the output list doesn't count)

from typing import List


class Solution:
    # BigO(n) time complexity, BigO(n) space complexity
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)

        product = 1
        for index, num in enumerate(nums):
            leftProducts[index] = product
            product *= num

        product = 1
        for index in range(len(nums) -1, -1, -1):
            rightProducts[index] = product
            product *= nums[index]

        answers = [1] * len(nums)
        for index in range(len(answers)):
            answers[index] = leftProducts[index] * rightProducts[index]
        return answers

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([0, 0, 5], [0, 0, 0]),
        ([5, 0, 2], [0, 10, 0]),
    ]
    for nums, expected in tests:
        got = sol.productExceptSelf(nums)
        print("PASS" if got == expected else "FAIL", nums, "->", got)
