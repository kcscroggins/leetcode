'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false. (EASY)

    Ex1. 
    Input: nums = [1, 2, 3, 3]

    Output: true

    Ex2:
    Input: nums = [1, 2, 3, 4]

    Output: false
'''

def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for num in nums:
            if num in duplicate:
                return True
            
            duplicate.add(num)
        
        return False


# Online Solution
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


'''
The first solution as one minor upside in that it will exit early once a duplicate is detected.
'''