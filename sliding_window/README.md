# Sliding Window Pattern

## Overview

The sliding window pattern is a technique used to solve problems involving arrays, strings, or lists where you need to find a contiguous subarray or substring that satisfies certain conditions. Instead of using nested loops (which would be O(n²)), the sliding window technique optimizes the solution to O(n) by maintaining a "window" that slides through the data structure.

## How to Identify Sliding Window Problems

Look for these key indicators:

### 1. Problem Characteristics
- The problem involves a **contiguous sequence** (subarray, substring, etc.)
- You need to find or optimize something about this sequence:
  - Longest/shortest subarray/substring
  - Maximum/minimum sum
  - Contains specific elements
  - Meets certain criteria (e.g., all unique characters)

### 2. Common Keywords
- "contiguous"
- "subarray" or "substring"
- "window"
- "longest/shortest/maximum/minimum"
- "at most K" or "exactly K"
- "sum equals"
- "all unique"
- "consecutive"

### 3. Example Problem Patterns
- Find the longest substring with at most K distinct characters
- Find the maximum sum of a subarray of size K
- Find the smallest subarray with sum >= target
- Find all anagrams in a string
- Longest substring without repeating characters

## Types of Sliding Window

### 1. Fixed-Size Window
The window size is predetermined and constant.

**Example:** "Find maximum sum of any contiguous subarray of size K"

```python
def max_sum_fixed_window(arr, k):
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

**Time Complexity:** O(n)

### 2. Variable-Size Window
The window size changes dynamically based on conditions.

**Example:** "Find the smallest subarray with sum >= target"

```python
def min_subarray_sum(arr, target):
    min_length = float('inf')
    window_sum = 0
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        # Shrink window while condition is met
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```

**Time Complexity:** O(n)

## General Template

### Variable-Size Window Template

```python
def sliding_window(arr):
    left = 0
    # Initialize window state (sum, count, hashmap, etc.)
    state = {}
    result = initial_value

    for right in range(len(arr)):
        # 1. Expand window: add arr[right] to window state
        update_state_with(arr[right])

        # 2. Shrink window: while window is invalid
        while window_is_invalid(state):
            # Remove arr[left] from window state
            remove_from_state(arr[left])
            left += 1

        # 3. Update result when window is valid
        result = update_result(result, right - left + 1)

    return result
```

### Fixed-Size Window Template

```python
def fixed_window(arr, k):
    result = initial_value

    # Build initial window
    for i in range(k):
        update_state_with(arr[i])

    result = calculate_result()

    # Slide window
    for i in range(k, len(arr)):
        # Remove leftmost element
        remove_from_state(arr[i - k])
        # Add rightmost element
        update_state_with(arr[i])
        # Update result
        result = update_result(result)

    return result
```

## Common Patterns and Techniques

### 1. Using a HashMap/Dictionary
Track character/element frequencies within the window.

```python
from collections import defaultdict

def longest_substring_k_distinct(s, k):
    char_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

### 2. Using a Set
Track unique elements in the window.

```python
def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

### 3. Counter Pattern
Track if window matches target conditions.

```python
from collections import Counter

def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    window_count = Counter()

    for i in range(len(s)):
        # Add new character
        window_count[s[i]] += 1

        # Remove old character if window too large
        if i >= len(p):
            if window_count[s[i - len(p)]] == 1:
                del window_count[s[i - len(p)]]
            else:
                window_count[s[i - len(p)]] -= 1

        # Check if window matches
        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result
```

## Decision Flow

When approaching a sliding window problem:

1. **Identify the window type:**
   - Is the window size fixed? → Use fixed-size window
   - Does the window size vary? → Use variable-size window

2. **Determine window expansion:**
   - What do I add when expanding right?
   - How do I track window state? (sum, count, hashmap, set)

3. **Determine window contraction:**
   - When should I shrink the window? (invalid condition)
   - What do I remove when shrinking from left?

4. **Update result:**
   - When do I update the result? (every iteration, only when valid)
   - Am I looking for max or min?

## Complexity Analysis

- **Time Complexity:** O(n) - Each element is visited at most twice (once by right pointer, once by left pointer)
- **Space Complexity:** O(k) where k is the size of the additional data structure (hashmap, set, etc.)

## Common Pitfalls

1. **Off-by-one errors:** Window size is `right - left + 1`, not `right - left`
2. **Forgetting to update state:** Always update state when adding/removing elements
3. **Wrong shrinking condition:** Make sure the while loop condition correctly identifies invalid windows
4. **Edge cases:** Empty arrays, window size larger than array, negative numbers

## Practice Problems

- Longest Substring Without Repeating Characters (LeetCode 3)
- Minimum Window Substring (LeetCode 76)
- Longest Substring with At Most K Distinct Characters (LeetCode 340)
- Maximum Sum Subarray of Size K
- Find All Anagrams in a String (LeetCode 438)
- Longest Repeating Character Replacement (LeetCode 424)
- Permutation in String (LeetCode 567)
- Minimum Size Subarray Sum (LeetCode 209)
