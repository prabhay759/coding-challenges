# 🧠 Daily Coding Challenge – Day 01
**Date:** 2026-04-02 | **Topic:** Sliding Window | **Difficulty:** Medium | **Companies:** Google · Amazon · Microsoft

---

## Problem: Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring that contains no repeating characters.

### Examples

```
Input:  s = "abcabcbb"
Output: 3
// "abc" is the longest substring without repeating characters

Input:  s = "bbbbb"
Output: 1
// "b" is the only non-repeating substring

Input:  s = "pwwkew"
Output: 3
// "wke" is the answer; note "pwke" is a subsequence, not a substring
```

### Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces

---

## 💡 Hint
<details>
<summary>Click to reveal</summary>
Think about maintaining a window of valid (non-repeating) characters. What data structure lets you check for duplicates in O(1) and also lets you track *where* a character last appeared?
</details>

---

## 🧠 Approach

Use a **sliding window** with a hash map that stores the last seen index of each character. The left pointer `l` only ever moves forward — when a duplicate is found, jump `l` past the previous occurrence of that character. This avoids the O(n²) cost of shrinking the window one step at a time.

**Time Complexity:** `O(n)` — each character is visited at most twice  
**Space Complexity:** `O(min(n, 128))` — the map holds at most one entry per unique ASCII character

---

## ✅ Python Solution

```python
def length_of_longest_substring(s: str) -> int:
    # Maps each character to the index just after its last occurrence
    last_seen = {}
    max_len = 0
    l = 0  # left boundary of the current window

    for r, char in enumerate(s):
        # If char was seen inside the current window, shrink from the left
        if char in last_seen and last_seen[char] >= l:
            l = last_seen[char] + 1

        last_seen[char] = r
        max_len = max(max_len, r - l + 1)

    return max_len


# ── Tests ──────────────────────────────────────────────
if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb")    == 1
    assert length_of_longest_substring("pwwkew")   == 3
    assert length_of_longest_substring("")         == 0
    assert length_of_longest_substring(" ")        == 1
    print("All tests passed ✅")
```

---

## 🔥 Follow-up Challenge

Can you solve the variant where you are allowed **at most `k` distinct characters** in the substring? (LeetCode 340 — asked by Google)

---

## 📚 Key Takeaways
- Sliding window shines when you need the **longest/shortest subarray/substring** satisfying a condition
- Storing `last_seen index + 1` (not just a boolean) lets you jump the left pointer in O(1) instead of crawling
- Always ask: *does the window need to shrink by 1 or jump?* — jumping gives you O(n) vs O(n²)

---
*Day 01 of the Big Tech Interview Prep Series · [View all challenges](../README.md)*
