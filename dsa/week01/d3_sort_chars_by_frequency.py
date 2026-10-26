# LeetCode 451. Sort Characters By Frequency (Medium)
# Given a string s, sort it in decreasing order based on how often each
# character appears. Return the sorted string.
# If several answers are possible, return any of them.
#
# Example 1: s = "tree"   -> "eert"   ("eetr" is also correct)
# Example 2: s = "cccaaa" -> "aaaccc" ("cccaaa" is also correct, but "cacaca" is not:
#                                      the same characters must be together)
# Example 3: s = "Aabb"   -> "bbAa"   ("bbaA" is also correct; 'A' and 'a' are different)
#
# Constraints: 1 <= len(s) <= 5 * 10^5; s has English letters and digits.


class Solution:
    # Big O(n k log k) where n is the len(s) and k is the number of distinct letters in s, which is at most n. So, Big O (n log n)
    # Space complexity O(n)
    def frequencySort(self, s: str) -> str:
        counts = dict()
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        sorted_list = sorted(counts, key = counts.get, reverse = True)
        result = ""
        for letter in sorted_list:
            result = result + (letter * counts[letter])
        return result


def is_valid(s: str, got: str) -> bool:
    # Same characters, each group together, and groups in non-increasing count order
    if got is None or sorted(got) != sorted(s):
        return False
    runs = []
    for ch in got:
        if runs and runs[-1][0] == ch:
            runs[-1][1] += 1
        else:
            runs.append([ch, 1])
    if len(runs) != len(set(got)):
        return False
    return all(runs[i][1] >= runs[i + 1][1] for i in range(len(runs) - 1))


if __name__ == "__main__":
    sol = Solution()
    tests = ["tree", "cccaaa", "Aabb", "z", "abcabcaab", "112233334"]
    for s in tests:
        got = sol.frequencySort(s)
        print("PASS" if is_valid(s, got) else "FAIL", repr(s), "->", repr(got))
