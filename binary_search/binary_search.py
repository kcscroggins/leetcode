'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
'''

# My Solution (Did not wrok - Time Exceeded Limit)

'''
Error 1: Loop condition creates infinite loop, should have used (<=)
Error 2: Needed parenthesis around the compute of middle_index (front_index + back_index) // 2
Error 3: I needed to make sure to exclude the middle after determining < or >.
'''

def search(self, nums: List[int], target: int) -> int:
        
        front_index = 0 
        back_index = len(nums) - 1

        while front_index != back_index:
            middle_index = front_index + back_index // 2
            middle_value = nums[middle_index]

            if middle_value == target:
                return middle_index
            
            elif middle_value < target:
                front_index = middle_index
                middle_index = front_index + back_index //2

            else:
                back_index = middle_index - 1
                    
        return -1

# Correct Solution

def search(self, nums: List[int], target: int) -> int:
    front_index = 0
    back_index = len(nums) - 1

    while front_index <= back_index:
        middle_index = (front_index + back_index) // 2
        middle_value = nums[middle_index]

        if middle_value == target:
            return middle_index
        elif middle_value < target:
            front_index = middle_index + 1
        else:
            back_index = middle_index - 1

    return -1

