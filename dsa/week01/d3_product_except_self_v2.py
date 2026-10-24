# LeetCode 238. Product of Array Except Self (Medium), v2: follow-up
# Given a list of integers nums, return a list answer where answer[i] is the
# product of every element of nums except nums[i].
# You must not use division, and it must run in O(n) time.
#
# Follow-up (this version): use only O(1) extra space.
# The output list `answer` does NOT count as extra space; everything else does
# (so no left_products / right_products lists).
#
# Example 1: nums = [1, 2, 3, 4]       -> [24, 12, 8, 6]
# Example 2: nums = [-1, 1, 0, -3, 3]  -> [0, 0, 9, 0, 0]

from typing import List


class Solution:
    # Big O(n) time complexity. O(1) space complexity 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        product = 1
        for index, num in enumerate(nums):
            answers[index] = product 
            product *= num 
        
        product = 1
        for index in range(len(nums) - 1, -1, -1):
            answers[index] *= product
            product *= nums[index]

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
