# LeetCode 383. Ransom Note (Easy)
# Return True if ransomNote can be built using the letters of magazine, else False.
# Each letter in magazine can be used only once.
#
# Example 1: ransomNote = "a",  magazine = "b"    -> False
# Example 2: ransomNote = "aa", magazine = "ab"   -> False
# Example 3: ransomNote = "aa", magazine = "aab"  -> True
#
# Constraints: 1 <= len(ransomNote), len(magazine) <= 10^5; lowercase English letters only.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        supply = dict()
        for letter in magazine:
            supply[letter] = supply.get(letter, 0) + 1
        
        for letter in ransomNote:
            if letter not in supply:
                return False 
            supply[letter] -= 1
            if supply[letter] < 0:
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("abc", "cbaxyz", True),
        ("abc", "ab", False)
    ]
    for note, magazine, expected in tests:
        got = sol.canConstruct(note, magazine)
        print("PASS" if got == expected else "FAIL", note, magazine, "->", got)
