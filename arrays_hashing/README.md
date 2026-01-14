# Arrays & Hashing Pattern

## Overview

Arrays and hashing are fundamental data structures used to solve a wide variety of problems. Arrays provide O(1) access by index, while hash tables (dictionaries/maps) provide O(1) average-case lookup, insertion, and deletion by key. Many problems that appear to require O(n²) brute force solutions can be optimized to O(n) time using hash tables to store and retrieve information efficiently.

## How to Identify Arrays & Hashing Problems

Look for these key indicators:

### 1. Problem Characteristics
- Need to **track frequency or count** of elements
- Need to **find pairs/groups** with specific properties
- Need **fast lookups** (checking if element exists)
- Need to **group or categorize** elements
- Need to **detect duplicates**
- Need to **map relationships** between elements
- Problems involving **anagrams or character patterns**

### 2. Common Keywords
- "frequency"
- "count"
- "duplicate"
- "unique"
- "anagram"
- "group"
- "two sum" (unsorted)
- "contains"
- "first occurrence"
- "most frequent"
- "k most/least"

### 3. Optimization Indicators
- Brute force requires nested loops O(n²)
- Need to check "have I seen this before?"
- Need to access elements by value, not just by index
- Array is unsorted and sorting would destroy important information

## When to Use What

### Use Arrays When:
- Need to maintain **order** or **index-based access**
- Working with **ranges** or **sequences**
- Need to **sort** the data
- Memory is extremely constrained (arrays are more space-efficient)
- Example: Prefix sums, range queries, sorting problems

### Use Hash Tables When:
- Need **O(1) lookups** by value
- Need to **count frequencies**
- Need to **detect duplicates quickly**
- Need to **group by a key**
- Order doesn't matter or can be reconstructed
- Example: Two sum, anagrams, frequency counting

### Use Both When:
- Need both fast lookups AND maintain some ordering
- Example: Top K frequent elements (hash for counting + array for sorting)

## Common Patterns

### 1. Frequency Counting

Track how many times each element appears.

```python
from collections import Counter

def count_frequencies(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Or use Counter
def count_frequencies_v2(arr):
    return Counter(arr)
```

**Use Cases:**
- Find most/least frequent elements
- Find elements appearing k times
- Character frequency in strings

**Example:** Valid Anagram

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

# Or manual approach
def is_anagram_v2(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

### 2. Lookup Table / Complement Pattern

Store elements in a hash table for O(1) lookup.

**Example:** Two Sum

```python
def two_sum(nums, target):
    seen = {}  # Map: value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return [-1, -1]
```

**Time:** O(n)
**Space:** O(n)

### 3. Grouping by Key

Group elements that share a common property.

**Example:** Group Anagrams

```python
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        # Sort string as key (all anagrams have same sorted form)
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())

# Alternative: Use character count as key
def group_anagrams_v2(strs):
    groups = defaultdict(list)

    for s in strs:
        # Count of each character (a-z)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Use tuple as key (lists aren't hashable)
        groups[tuple(count)].append(s)

    return list(groups.values())
```

### 4. Set for Uniqueness

Use a set to track unique elements or detect duplicates.

**Example:** Contains Duplicate

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Or simpler
def contains_duplicate_v2(nums):
    return len(nums) != len(set(nums))
```

### 5. Index Mapping

Map values to their indices for quick lookup.

**Example:** Two Sum (find indices)

```python
def two_sum_indices(nums, target):
    index_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], i]
        index_map[num] = i

    return []
```

### 6. Prefix/Running Computation

Store cumulative information for range queries.

**Example:** Subarray Sum Equals K

```python
def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}  # Handle subarrays starting from index 0

    for num in nums:
        prefix_sum += num

        # Check if there's a prefix that makes current sum = k
        if (prefix_sum - k) in sum_freq:
            count += sum_freq[prefix_sum - k]

        # Add current prefix sum to map
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1

    return count
```

**Time:** O(n)
**Space:** O(n)

### 7. Top K Elements

Combine hashing (for counting) with sorting or heap.

**Example:** Top K Frequent Elements

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    # Count frequencies
    freq = Counter(nums)

    # Use heap to get k most frequent
    return heapq.nlargest(k, freq.keys(), key=freq.get)

# Alternative: Bucket sort for O(n) time
def top_k_frequent_v2(nums, k):
    freq = Counter(nums)

    # Bucket[i] = list of elements with frequency i
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    # Collect k most frequent from highest frequency
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]

    return result
```

## General Templates

### Template 1: Frequency Counter

```python
from collections import defaultdict

def frequency_pattern(arr):
    freq = defaultdict(int)

    # Build frequency map
    for item in arr:
        freq[item] += 1

    # Process based on frequencies
    result = []
    for item, count in freq.items():
        if meets_condition(count):
            result.append(item)

    return result
```

### Template 2: Lookup/Complement Pattern

```python
def lookup_pattern(arr, target):
    seen = set()  # or dict if need to store additional info

    for item in arr:
        complement = calculate_complement(item, target)

        if complement in seen:
            return process_match(item, complement)

        seen.add(item)

    return default_result
```

### Template 3: Grouping Pattern

```python
from collections import defaultdict

def grouping_pattern(arr):
    groups = defaultdict(list)

    for item in arr:
        key = compute_key(item)
        groups[key].append(item)

    return process_groups(groups)
```

### Template 4: Prefix Sum with HashMap

```python
def prefix_sum_pattern(arr, target):
    prefix_sum = 0
    sum_map = {0: 1}  # or {0: -1} for index-based
    result = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        if (prefix_sum - target) in sum_map:
            result += sum_map[prefix_sum - target]

        sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1

    return result
```

## Advanced Techniques

### 1. Rolling Hash (for string matching)

```python
def rabin_karp(text, pattern):
    """Find pattern in text using rolling hash"""
    if len(pattern) > len(text):
        return -1

    BASE = 256
    MOD = 101

    # Calculate hash of pattern
    pattern_hash = 0
    for char in pattern:
        pattern_hash = (pattern_hash * BASE + ord(char)) % MOD

    # Rolling hash for text
    text_hash = 0
    power = 1
    for i in range(len(pattern) - 1):
        power = (power * BASE) % MOD

    for i in range(len(pattern)):
        text_hash = (text_hash * BASE + ord(text[i])) % MOD

    # Check each window
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if text[i:i+len(pattern)] == pattern:
                return i

        if i < len(text) - len(pattern):
            text_hash = (text_hash - ord(text[i]) * power) % MOD
            text_hash = (text_hash * BASE + ord(text[i + len(pattern)])) % MOD
            text_hash = (text_hash + MOD) % MOD

    return -1
```

### 2. Monotonic Array with HashMap

```python
def longest_consecutive(nums):
    """Longest consecutive sequence"""
    if not nums:
        return 0

    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from sequence start
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length
```

### 3. Product Except Self (Array Technique)

```python
def product_except_self(nums):
    """O(n) time, O(1) extra space (output array doesn't count)"""
    n = len(nums)
    result = [1] * n

    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result
```

## Hash Function Strategies

### When to Use Different Keys:

1. **Sorted String** - For anagrams
   ```python
   key = ''.join(sorted(s))
   ```

2. **Character Count Tuple** - For anagrams (faster)
   ```python
   count = [0] * 26
   for c in s:
       count[ord(c) - ord('a')] += 1
   key = tuple(count)
   ```

3. **Prime Product** - For anagrams (can overflow)
   ```python
   primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
   key = 1
   for c in s:
       key *= primes[ord(c) - ord('a')]
   ```

4. **Coordinates/Tuples** - For 2D positions
   ```python
   key = (x, y)
   ```

5. **String Concatenation** - For multiple values
   ```python
   key = f"{val1}_{val2}_{val3}"
   ```

## Complexity Considerations

### Hash Table Operations:
- **Average Case:** O(1) for insert, delete, lookup
- **Worst Case:** O(n) when all elements hash to same bucket (rare)
- **Space:** O(n) to store n elements

### Common Time Complexities:
- Single pass with hash table: **O(n)**
- Hash table + sorting: **O(n log n)**
- Multiple hash tables: Still **O(n)** if constant number

### Space Optimization:
- Use set instead of dict when only checking existence
- Use array instead of hash table when keys are small integers (0 to k)
- In-place modifications when possible

## Common Pitfalls

1. **Hash collision handling:** Python handles this automatically, but be aware
2. **Mutable keys:** Lists and sets can't be dictionary keys; use tuples
3. **Default values:** Use `dict.get(key, default)` or `defaultdict`
4. **Modifying while iterating:** Don't modify dict while iterating over it
5. **Integer overflow:** When using mathematical hash functions
6. **Case sensitivity:** Remember to normalize strings when needed
7. **Off-by-one in arrays:** Check boundary conditions carefully

## Decision Flow

1. **Do I need to count something?** → Use hash table for frequency
2. **Do I need to find a complement/pair?** → Use hash set/dict for lookup
3. **Do I need to group items?** → Use hash table with computed key
4. **Is there a mathematical relationship?** → Consider prefix sums with hash
5. **Do I need ordering?** → Use array or combine hash + sort
6. **Is the key range small (0 to k)?** → Consider using array instead of hash

## Arrays vs Hash Tables: Quick Reference

| Operation | Array | Hash Table |
|-----------|-------|------------|
| Access by index | O(1) | N/A |
| Access by value | O(n) | O(1) avg |
| Insert at end | O(1) amortized | O(1) avg |
| Insert at position | O(n) | N/A |
| Delete | O(n) | O(1) avg |
| Search | O(n) unsorted, O(log n) sorted | O(1) avg |
| Memory | More efficient | More overhead |
| Ordering | Preserved | Not preserved |
| Duplicates | Allowed | Keys must be unique |

## Practice Problems

### Beginner
- Contains Duplicate (LeetCode 217)
- Valid Anagram (LeetCode 242)
- Two Sum (LeetCode 1)
- Majority Element (LeetCode 169)
- Single Number (LeetCode 136)

### Intermediate
- Group Anagrams (LeetCode 49)
- Top K Frequent Elements (LeetCode 347)
- Product of Array Except Self (LeetCode 238)
- Valid Sudoku (LeetCode 36)
- Subarray Sum Equals K (LeetCode 560)

### Advanced
- Longest Consecutive Sequence (LeetCode 128)
- First Missing Positive (LeetCode 41)
- Substring with Concatenation of All Words (LeetCode 30)
- Continuous Subarray Sum (LeetCode 523)
- Maximum Size Subarray Sum Equals k (LeetCode 325)

## Tips for Optimization

1. **Choose the right data structure:**
   - Set for existence checks
   - Dict for key-value mapping
   - Counter for frequency counting
   - defaultdict to avoid key existence checks

2. **One-pass vs two-pass:**
   - Sometimes two passes is clearer and still O(n)
   - One-pass can be trickier but sometimes necessary

3. **Space vs time trade-off:**
   - Hash tables trade space for time
   - Usually worth it to go from O(n²) to O(n)

4. **Python-specific:**
   - Use `collections.Counter`, `defaultdict`
   - Use `enumerate()` for index tracking
   - Use `dict.get()` for default values
   - Set operations: union `|`, intersection `&`, difference `-`
