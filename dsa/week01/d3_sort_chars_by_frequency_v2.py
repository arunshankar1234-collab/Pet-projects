# LeetCode 451. Sort Characters By Frequency (Medium), v2: buckets
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
    # Big O(n) time complexity. Big O(n) space complexity
    def frequencySort(self, s: str) -> str:
        counts = dict()
        for character in s:
            counts[character] = counts.get(character, 0) + 1
        
        max_count = max(counts.values())
        buckets = [[] for _ in range(max_count + 1)]
        for letter, count in counts.items():
            buckets[count].append(letter)
        
        pieces = []
        for count in range(len(buckets) - 1, 0, -1):
            for letter in buckets[count]: 
                pieces.append(letter * count)
        return "".join(pieces)


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
