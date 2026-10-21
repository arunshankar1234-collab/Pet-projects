# LeetCode 771. Jewels and Stones (Easy)
# jewels is a string of the stone types that are jewels; stones is the string of
# stones you have. Return how many of your stones are jewels.
# Letters are case-sensitive: "a" and "A" are different types.
#
# Example 1: jewels = "aA", stones = "aAAbbbb"  -> 3
# Example 2: jewels = "z",  stones = "ZZ"       -> 0
#
# Constraints: 1 <= len(jewels), len(stones) <= 50; jewels has no repeated letters.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)

        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count

        # One-line alternative:
        # return sum(1 for stone in stones if stone in jewels_set)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("abc", "aabbccd", 6),
    ]
    for jewels, stones, expected in tests:
        got = sol.numJewelsInStones(jewels, stones)
        print("PASS" if got == expected else "FAIL", jewels, stones, "->", got)
