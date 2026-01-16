# Stack Pattern

## Overview

A stack is a Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end (the "top"). The stack pattern is fundamental for solving problems involving nested structures, matching pairs, reversing order, and tracking most recent elements. Stacks are particularly powerful when you need to remember previous states or when the order of processing matters.

## How to Identify Stack Problems

Look for these key indicators:

### 1. Problem Characteristics
- Need to process elements in **reverse order**
- Matching or balancing **pairs** (parentheses, brackets, tags)
- **Nested structures** (function calls, expressions, folders)
- Need to **backtrack** or undo operations
- **Most recent element** matters for current decision
- Processing elements **from inside out**
- Need to **defer operations** until later

### 2. Common Keywords
- "valid parentheses/brackets"
- "balanced"
- "nested"
- "next greater/smaller element"
- "most recent"
- "undo/redo"
- "evaluate expression"
- "reverse Polish notation"
- "recursion depth"
- "function call stack"
- "backspace/delete"
- "matching pairs"

### 3. Optimization Hints
- Brute force requires checking all previous elements repeatedly
- Need to keep track of unmatched/pending elements
- Need to find nearest greater/smaller elements
- Problem involves matching or pairing elements

## Types of Stack Problems

### 1. Matching Pairs / Validation
Used for validating balanced structures like parentheses, brackets, or tags.

**When to use:**
- Validating balanced parentheses/brackets
- Matching opening and closing tags
- Checking nested structures
- Validating expressions

**Example:** Valid Parentheses

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)

    return len(stack) == 0
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### 2. Monotonic Stack
A stack that maintains elements in monotonic (increasing or decreasing) order.

**When to use:**
- Finding next greater/smaller element
- Finding previous greater/smaller element
- Building histograms
- Stock span problems
- Temperature problems

**Example:** Next Greater Element

```python
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        # While current element is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### 3. Expression Evaluation
Used for parsing and evaluating mathematical expressions.

**When to use:**
- Evaluating postfix/prefix expressions
- Converting infix to postfix
- Calculator problems
- Parsing expressions with operators

**Example:** Evaluate Reverse Polish Notation

```python
def eval_rpn(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # Division
                stack.append(int(a / b))  # Truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### 4. String Processing
Used for processing strings with backspace, undo operations, or building results.

**When to use:**
- Backspace/delete operations
- Building strings incrementally
- Removing adjacent duplicates
- Processing commands

**Example:** Remove Adjacent Duplicates

```python
def remove_duplicates(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove duplicate
        else:
            stack.append(char)

    return ''.join(stack)
```

**Time Complexity:** O(n)
**Space Complexity:** O(n)

### 5. DFS Simulation / Backtracking
Stack can simulate recursive DFS or manage backtracking states.

**When to use:**
- Converting recursion to iteration
- Managing DFS traversal explicitly
- Tracking visited states
- Path tracking in graphs/trees

**Example:** Iterative DFS

```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)  # Process node

            # Add neighbors to stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited
```

**Time Complexity:** O(V + E) where V = vertices, E = edges
**Space Complexity:** O(V)

## General Templates

### Template 1: Basic Stack Operations

```python
def stack_template(arr):
    stack = []
    result = []

    for element in arr:
        # Pop elements that don't satisfy condition
        while stack and condition(stack[-1], element):
            popped = stack.pop()
            # Process popped element if needed
            result.append(popped)

        # Push current element
        stack.append(element)

    # Process remaining elements in stack
    while stack:
        result.append(stack.pop())

    return result
```

### Template 2: Monotonic Stack (Next Greater)

```python
def monotonic_stack_template(arr):
    n = len(arr)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        # Maintain monotonic property
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]

        stack.append(i)

    return result
```

### Template 3: Matching Pairs

```python
def matching_pairs_template(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}  # closing: opening

    for char in s:
        if char in pairs:  # Closing symbol
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:  # Opening symbol
            stack.append(char)

    return len(stack) == 0
```

### Template 4: Expression Evaluation

```python
def evaluate_expression(tokens):
    stack = []

    for token in tokens:
        if is_operator(token):
            # Pop operands (order matters!)
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.append(result)
        else:
            stack.append(convert_to_number(token))

    return stack[0]
```

## Common Patterns and Techniques

### 1. Daily Temperatures

```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # Store indices

    for i in range(n):
        # While current temp is warmer than stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx

        stack.append(i)

    return result
```

### 2. Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    stack = []  # Store indices
    max_area = 0
    heights.append(0)  # Sentinel to flush stack

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h_idx = stack.pop()
            height = heights[h_idx]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area
```

### 3. Min Stack

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimums

    def push(self, val):
        self.stack.append(val)
        # Push min of current val and previous min
        min_val = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
```

### 4. Decode String

```python
def decode_string(s):
    stack = []

    for char in s:
        if char != ']':
            stack.append(char)
        else:
            # Build string inside brackets
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr

            stack.pop()  # Remove '['

            # Get the number
            num_str = ''
            while stack and stack[-1].isdigit():
                num_str = stack.pop() + num_str

            # Push repeated string
            stack.append(int(num_str) * substr)

    return ''.join(stack)
```

### 5. Basic Calculator

```python
def calculate(s):
    stack = []
    num = 0
    sign = 1  # 1 for positive, -1 for negative
    result = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-':
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            # Push previous result and sign
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  # Pop sign
            result += stack.pop()  # Pop previous result

    result += sign * num
    return result
```

## Decision Flow

When approaching a stack problem:

1. **What needs to be remembered?**
   - Opening brackets → Use stack to match with closing
   - Previous elements → Monotonic stack
   - Partial results → Expression evaluation stack

2. **What triggers stack operations?**
   - Closing bracket/tag → Pop and validate
   - Smaller/larger element → Pop until condition met
   - Operator → Pop operands and compute

3. **What do you store in the stack?**
   - The actual values
   - Indices (for distance/range calculations)
   - Tuples/objects (for multiple pieces of info)

4. **When do you pop?**
   - Found matching pair
   - Found greater/smaller element
   - Need to evaluate/compute
   - Reached end of scope

## Stack vs Other Data Structures

| Scenario | Use Stack | Use Queue | Use Deque |
|----------|-----------|-----------|-----------|
| **Last processed matters** | ✓ | | |
| **First processed matters** | | ✓ | |
| **Both ends matter** | | | ✓ |
| **Matching pairs** | ✓ | | |
| **BFS traversal** | | ✓ | |
| **DFS traversal** | ✓ | | |
| **Sliding window max** | | | ✓ |

## Complexity Analysis

- **Time Complexity:**
  - Most stack operations: O(1) - push, pop, peek
  - Processing n elements: O(n)
  - Amortized O(n) even with nested loops (each element pushed/popped once)

- **Space Complexity:** O(n)
  - Worst case: all elements in stack
  - Best case: O(1) for problems that only need constant extra space

## Common Pitfalls

1. **Empty stack check:** Always check `if stack:` before `stack[-1]` or `stack.pop()`
2. **Wrong order for operators:** In RPN, second operand is popped first: `b = pop(); a = pop(); result = a - b`
3. **Not clearing all elements:** Some problems require processing remaining stack elements
4. **Storing values vs indices:** Choose based on what you need to calculate (distance vs actual values)
5. **Forgetting sentinel values:** For monotonic stack problems, adding 0 or infinity at end can simplify
6. **Modifying stack while iterating:** Use while loop for conditional popping
7. **Not handling edge cases:** Empty string, single element, all same elements

## Tips and Tricks

1. **Stack in Python:** Use list with `append()` and `pop()` - both O(1)
2. **Peek without pop:** Use `stack[-1]` to look at top element
3. **Store indices not values:** When you need distance/range calculations
4. **Monotonic stack direction:**
   - Decreasing stack → Find next greater element
   - Increasing stack → Find next smaller element
5. **Two stacks trick:** Min/max stack, undo/redo, browser history
6. **Add sentinel:** Append 0 to heights, infinity to end - simplifies edge cases
7. **Count remaining stack size:** For problems asking "how many unmatched"

## Practice Problems

### Beginner
- Valid Parentheses (LeetCode 20)
- Remove All Adjacent Duplicates in String (LeetCode 1047)
- Baseball Game (LeetCode 682)
- Backspace String Compare (LeetCode 844)
- Build Array With Stack Operations (LeetCode 1441)

### Intermediate
- Min Stack (LeetCode 155)
- Evaluate Reverse Polish Notation (LeetCode 150)
- Daily Temperatures (LeetCode 739)
- Next Greater Element I (LeetCode 496)
- Decode String (LeetCode 394)
- Asteroid Collision (LeetCode 735)
- Remove K Digits (LeetCode 402)

### Advanced
- Largest Rectangle in Histogram (LeetCode 84)
- Maximal Rectangle (LeetCode 85)
- Basic Calculator (LeetCode 224)
- Basic Calculator II (LeetCode 227)
- Trapping Rain Water (LeetCode 42) - can use stack or two pointers
- Longest Valid Parentheses (LeetCode 32)
- Maximum Frequency Stack (LeetCode 895)
