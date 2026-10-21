# LeetCode 242. Valid Anagram (Easy)
# Given two strings s and t, return True if t is an anagram of s, else False.
# An anagram uses exactly the same letters, the same number of times, in any order.
#
# Example 1: s = "anagram", t = "nagaram"  -> True
# Example 2: s = "rat",     t = "car"      -> False
#
# Constraints: 1 <= len(s), len(t) <= 5 * 10^4; lowercase English letters only.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = dict()
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        
        for letter in t:
            if letter not in counts:
                return False 
            counts[letter] = counts[letter] - 1
            if counts[letter] < 0:
                return False

        # for entry in counts:
        #     if counts[entry] != 0:
        #         return False
        return True

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("aacc", "ccac", False),
    ]
    for s, t, expected in tests:
        got = sol.isAnagram(s, t)
        print("PASS" if got == expected else "FAIL", s, t, "->", got)
