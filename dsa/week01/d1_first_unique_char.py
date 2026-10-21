# LeetCode 387. First Unique Character in a String (Easy)
# Return the index of the first character in s that appears only once.
# If there is no such character, return -1.
#
# Example 1: s = "leetcode"      -> 0   ("l")
# Example 2: s = "loveleetcode"  -> 2   ("v")
# Example 3: s = "aabb"          -> -1
#
# Constraints: 1 <= len(s) <= 10^5; lowercase English letters only.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = dict()
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1

        for index in range(len(s)):
            letter = s[index]
            if counts[letter] == 1:
                return index

        return -1 

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("z", 0),
    ]
    for s, expected in tests:
        got = sol.firstUniqChar(s)
        print("PASS" if got == expected else "FAIL", s, "->", got)
