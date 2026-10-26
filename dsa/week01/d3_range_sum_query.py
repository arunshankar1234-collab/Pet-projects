# LeetCode 303. Range Sum Query - Immutable (Easy)
# Build a class NumArray from a list of integers nums. It must answer many
# questions of the form sumRange(left, right): the sum of nums[left] through
# nums[right], both ends included. nums never changes after it's built.
#
# Example: nums = [-2, 0, 3, -5, 2, -1]
#   sumRange(0, 2) -> 1    (-2 + 0 + 3)
#   sumRange(2, 5) -> -1   (3 + -5 + 2 + -1)
#   sumRange(0, 5) -> -3   (the whole list)
#
# Constraints: 1 <= len(nums) <= 10^4; -10^5 <= nums[i] <= 10^5;
# 0 <= left <= right < len(nums); up to 10^4 calls to sumRange.
# Goal: each sumRange call should be O(1).

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # Big O(n) auxiliary space complexity, Big O(n)
        self.prefix_total = [0]
        running_total = 0
        for num in nums:
            running_total += num
            self.prefix_total.append(running_total)

    # Big O(1) time complexity
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_total[right + 1] - self.prefix_total[left]


if __name__ == "__main__":
    tests = [
        ([-2, 0, 3, -5, 2, -1], [((0, 2), 1), ((2, 5), -1), ((0, 5), -3)]),
        ([5], [((0, 0), 5)]),
        ([1, 2, 3, 4], [((1, 1), 2), ((0, 3), 10), ((1, 3), 9), ((3, 3), 4)]),
        ([0, -1, 0], [((0, 0), 0), ((1, 2), -1)]),
    ]
    for nums, queries in tests:
        num_array = NumArray(nums)
        for (left, right), expected in queries:
            got = num_array.sumRange(left, right)
            print("PASS" if got == expected else "FAIL", nums, (left, right), "->", got)
