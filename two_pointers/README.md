# Two Pointers Pattern

## Overview

The two pointers pattern is a technique that uses two pointers to iterate through a data structure, typically an array or linked list. By moving pointers strategically, we can solve problems in O(n) time and O(1) space that would otherwise require O(n²) time or O(n) extra space. The pattern is particularly effective for problems involving sorted arrays, palindromes, or finding pairs.

## How to Identify Two Pointers Problems

Look for these key indicators:

### 1. Problem Characteristics
- Working with **sorted arrays** or **linked lists**
- Need to find a **pair, triplet, or set** of elements
- Looking for elements that satisfy certain conditions
- Comparing elements from **different positions**
- Problems involving **palindromes**
- Need to remove/modify elements **in-place**

### 2. Common Keywords
- "sorted array"
- "pair/triplet that sums to target"
- "palindrome"
- "remove duplicates"
- "in-place"
- "two sum (with sorted array)"
- "reverse"
- "partition"
- "merge"
- "compare from both ends"

### 3. Optimization Hints
- Brute force would be O(n²) with nested loops
- Array is already sorted (or can be sorted)
- Need to avoid using extra space
- Need to process array from both ends

## Types of Two Pointers

### 1. Opposite Direction (Collision)
Pointers start at opposite ends and move toward each other.

**When to use:**
- Array is sorted
- Looking for pairs that sum to a target
- Checking palindromes
- Reversing an array

**Example:** Two Sum (sorted array)

```python
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return [-1, -1]
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### 2. Same Direction (Fast and Slow)
Both pointers move in the same direction at different speeds.

**When to use:**
- Removing duplicates in-place
- Partitioning arrays
- Moving elements to specific positions
- Finding cycle in linked list
- Finding middle of linked list

**Example:** Remove Duplicates from Sorted Array

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0  # Position for next unique element

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1  # Length of array without duplicates
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### 3. Fast and Slow (Cycle Detection)
Slow pointer moves one step, fast pointer moves two steps.

**When to use:**
- Detecting cycles in linked lists
- Finding middle of linked list
- Finding cycle start point

**Example:** Detect Cycle in Linked List

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

### 4. Sliding Window Variant
One pointer expands, the other contracts (similar to sliding window).

**When to use:**
- Finding subarrays with specific properties
- Can overlap with sliding window pattern

**Example:** Container With Most Water

```python
def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_water = width * min(height[left], height[right])
        max_water = max(max_water, current_water)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

## General Templates

### Template 1: Opposite Direction

```python
def opposite_pointers(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Process current positions
        if condition_met(arr[left], arr[right]):
            return result

        # Move pointers based on condition
        if should_move_left(arr[left], arr[right]):
            left += 1
        else:
            right -= 1

    return default_result
```

### Template 2: Same Direction (Fast/Slow)

```python
def same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        if condition_met(arr[fast]):
            # Process and move slow pointer
            arr[slow] = arr[fast]
            slow += 1

    return slow  # Often returns new length or slow position
```

### Template 3: Partition Pattern

```python
def partition(arr, condition):
    slow = 0  # Boundary for elements meeting condition

    for fast in range(len(arr)):
        if condition(arr[fast]):
            # Swap elements
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1

    return slow  # Partition point
```

## Common Patterns and Techniques

### 1. Palindrome Checking

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

### 2. Three Sum (Extension of Two Sum)

```python
def three_sum(arr):
    arr.sort()
    result = []

    for i in range(len(arr) - 2):
        # Skip duplicates for first number
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Two pointers for remaining elements
        left = i + 1
        right = len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

### 3. Partition Array (Dutch National Flag)

```python
def sort_colors(arr):
    """Sort array with 0s, 1s, and 2s"""
    left = 0  # Boundary for 0s
    right = len(arr) - 1  # Boundary for 2s
    current = 0

    while current <= right:
        if arr[current] == 0:
            arr[left], arr[current] = arr[current], arr[left]
            left += 1
            current += 1
        elif arr[current] == 2:
            arr[current], arr[right] = arr[right], arr[current]
            right -= 1
            # Don't increment current (need to check swapped element)
        else:
            current += 1
```

### 4. Merging Sorted Arrays

```python
def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result
```

### 5. Trapping Rain Water

```python
def trap_water(height):
    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water
```

## Decision Flow

When approaching a two pointers problem:

1. **Can the array be sorted?**
   - If yes and sorting doesn't break the problem → Sort it
   - If already sorted → Great!

2. **What are you comparing?**
   - Elements from opposite ends → Opposite direction pointers
   - Adjacent or nearby elements → Same direction pointers
   - Finding cycle or middle → Fast/slow pointers

3. **What's the movement strategy?**
   - Move based on comparison (sum too large/small)
   - Move based on condition (skip duplicates, partition)
   - Move at different speeds (cycle detection)

4. **Do you need to modify in-place?**
   - Yes → Use slow pointer to track write position
   - No → Can still use two pointers for reading

## Comparison: Two Pointers vs Sliding Window

| Aspect | Two Pointers | Sliding Window |
|--------|--------------|----------------|
| **Array State** | Often sorted | Can be unsorted |
| **Window Size** | Not a fixed window concept | Fixed or variable window |
| **Movement** | Can move either pointer independently | Right expands, left contracts |
| **Use Case** | Finding pairs, partitioning, palindromes | Contiguous subarrays/substrings |
| **Common Goal** | Compare/process two specific positions | Optimize over all subarrays |

**Note:** Some problems can use either pattern, and they can overlap!

## Complexity Analysis

- **Time Complexity:** Usually O(n) - each element visited at most once
  - With sorting: O(n log n) for sort + O(n) for two pointers = O(n log n)
- **Space Complexity:** Usually O(1) - only using pointer variables
  - Exception: If sorting in languages that use O(n) space for sort

## Common Pitfalls

1. **Infinite loops:** Make sure pointers always move in the while loop
2. **Array bounds:** Check `left < right` or `fast < len(arr)` to avoid index errors
3. **Off-by-one errors:** Be careful with `<` vs `<=` conditions
4. **Skipping elements:** When swapping in partition problems, be careful about incrementing
5. **Forgetting to handle remaining elements:** When merging, don't forget tail elements
6. **Duplicates:** Remember to skip duplicates in problems like 3Sum
7. **Edge cases:** Empty arrays, single element, all same elements

## Tips and Tricks

1. **Sorted array = strong hint** for two pointers
2. **When stuck, try sorting** the array first (if allowed)
3. **Draw it out:** Visualize pointer movements on paper
4. **For 3Sum/4Sum:** Fix one element, use two pointers for the rest
5. **In-place modification:** Slow pointer tracks write position, fast pointer reads
6. **Move the constraint:** In container problems, move the pointer that's limiting you

## Practice Problems

### Beginner
- Valid Palindrome (LeetCode 125)
- Two Sum II - Input Array Is Sorted (LeetCode 167)
- Remove Duplicates from Sorted Array (LeetCode 26)
- Reverse String (LeetCode 344)
- Move Zeroes (LeetCode 283)

### Intermediate
- 3Sum (LeetCode 15)
- Container With Most Water (LeetCode 11)
- Sort Colors (LeetCode 75)
- Remove Element (LeetCode 27)
- Linked List Cycle (LeetCode 141)

### Advanced
- Trapping Rain Water (LeetCode 42)
- 4Sum (LeetCode 18)
- Linked List Cycle II (LeetCode 142)
- Minimum Window Substring (LeetCode 76)
- Longest Mountain in Array (LeetCode 845)
