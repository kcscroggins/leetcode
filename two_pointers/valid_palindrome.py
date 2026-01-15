'''
Given a string s, return True if it is a palindrome, otherwise return False.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

'''

# My solution (Did not work)

'''
Error 1: Never refresh front_letter / back_letter after a successful match
Error 2: Moved the back_ptr in the wrong direction (Line 51)
Error 3: Loop condition is wrong for even length words (Line 40)
'''    

class Solution:
    def isPalindrome(self, s: str) -> bool:

        back_ptr = len(s) - 1
        front_ptr = 0
        front_letter = s[front_ptr]
        back_letter = s[back_ptr]

        while front_ptr != back_ptr:
            
            if front_letter.isalpha() or front_letter.isnumeric():

                if back_letter.isalpha() or back_letter.isnumeric():

                    if not front_letter.lower() == back_letter.lower():
                        return False
                    
                    else:
                        front_ptr +=1
                        back_ptr += 1

                else:
                    back_ptr -= 1
                    back_letter = s[back_ptr]
            else: 
                front_ptr += 1
                front_letter = s[front_ptr]
        
        return True    

# Fixed Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        back_ptr = len(s) - 1
        front_ptr = 0

        while front_ptr < back_ptr:
            front_letter = s[front_ptr]
            back_letter = s[back_ptr]

            if not (front_letter.isalpha() or front_letter.isnumeric()):
                front_ptr += 1
                continue

            if not (back_letter.isalpha() or back_letter.isnumeric()):
                back_ptr -= 1
                continue

            if front_letter.lower() != back_letter.lower():
                return False

            front_ptr += 1
            back_ptr -= 1

        return True

# NeetCode Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]



                

                    

                


