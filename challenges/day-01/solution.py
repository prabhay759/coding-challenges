"""
Problem:  Longest Substring Without Repeating Characters
Topic:    Sliding Window
Difficulty: Medium
Companies: Google · Amazon · Microsoft
Date:     2026-04-03
"""

# ──────────────────────────────────────────────
# APPROACH: Sliding Window + Hash Map
#
# Keep a window [l, r] of non-repeating characters.
# Store the last seen index of each character.
# When a duplicate is found inside the window,
# jump the left pointer past its previous occurrence.
# Track the max window size throughout.
#
# Time:  O(n)  — each character visited at most twice
# Space: O(1)  — at most 128 unique ASCII characters
# ──────────────────────────────────────────────

def length_of_longest_substring(s: str) -> int:
    last_seen = {}   # char -> last index it was seen
    max_len = 0
    l = 0            # left boundary of the window

    for r, char in enumerate(s):
        # If char is inside the current window, shrink from the left
        if char in last_seen and last_seen[char] >= l:
            l = last_seen[char] + 1

        last_seen[char] = r
        max_len = max(max_len, r - l + 1)

    return max_len


# ──────────────────────────────────────────────
# TESTS
# ──────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),   # "abc"
        ("bbbbb",    1),   # "b"
        ("pwwkew",   3),   # "wke"
        ("",         0),   # empty string
        (" ",        1),   # single space
        ("dvdf",     3),   # "vdf"
        ("anviaj",   5),   # "nviaj"
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        status = "✅" if result == expected else "❌"
        print(f"{status}  input={repr(s):<12} expected={expected}  got={result}")
