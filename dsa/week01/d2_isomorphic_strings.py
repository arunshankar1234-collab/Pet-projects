# LeetCode 205. Isomorphic Strings (Easy)
# Two strings s and t are isomorphic if the letters in s can be replaced to get t.
# Every occurrence of a letter must be replaced with the same letter, and no two
# different letters may be replaced with the same letter. A letter may map to itself.
# Return True if s and t are isomorphic, else False.
#
# Example 1: s = "egg",   t = "add"    -> True   (e -> a, g -> d)
# Example 2: s = "foo",   t = "bar"    -> False  (o would have to become both a and r)
# Example 3: s = "paper", t = "title"  -> True   (p -> t, a -> i, e -> l, r -> e)
#
# Constraints: 1 <= len(s) <= 5 * 10^4; len(t) == len(s);
# s and t can contain any printable ASCII character.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = dict()
        for index in range(len(s)):
            letter = s[index]
            if letter not in mapping:
                if t[index] in mapping.values():
                    return False
                mapping[letter] = t[index]
            else:
                if mapping[letter] != t[index]:
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("ab", "aa", False),
        ("a", "a", True),
        ("13", "42", True),
    ]
    for s, t, expected in tests:
        got = sol.isIsomorphic(s, t)
        print("PASS" if got == expected else "FAIL", s, t, "->", got)
