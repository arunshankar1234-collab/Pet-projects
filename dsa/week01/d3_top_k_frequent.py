# LeetCode 347. Top K Frequent Elements (Medium)
# Given a list of integers nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
# Example 1: nums = [1, 1, 1, 2, 2, 3], k = 2  -> [1, 2]   (1 appears 3x, 2 appears 2x)
# Example 2: nums = [1],                k = 1  -> [1]
#
# Constraints: 1 <= len(nums) <= 10^5; -10^4 <= nums[i] <= 10^4;
# k is in the range [1, number of distinct elements]; the answer is unique.
# Follow-up: can you do better than O(n log n)?

from typing import List


class Solution:
    # Time: O(n), Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        # buckets[c] will store a list of numbers that appeared c times
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, count in counts.items():
            buckets[count].append(number)
        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for number in buckets[count]:
                result.append(number)
                if len(result) == k:
                    return result
        return result
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 5, 5, 5, 6], 1, [5]),
        ([-1, -1, 2, 2, 2, 3], 2, [-1, 2]),
        ([7, 8, 9], 3, [7, 8, 9]),
    ]
    for nums, k, expected in tests:
        got = sol.topKFrequent(nums, k)
        ok = got is not None and sorted(got) == expected
        print("PASS" if ok else "FAIL", nums, k, "->", got)
