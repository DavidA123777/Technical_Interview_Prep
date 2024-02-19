class Solution(object):
    def isPalindrome(self, s):
        # Two Pointers Solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # initialize one pointer to the first character of the string and the other to the last character of the string
        l, r = 0, len(s) -1
        
        # loop until the left pointer reaches the right pointer
        while(l < r):
            # keep incrementing the left pointer until it reaches an alphanumeric character
            while(s[l].isalnum() == False and l < r):
                l += 1
            # keep decrementing the right pointer until it reaches an alphanumeric character
            while(s[r].isalnum() == False and l < r):
                r -= 1
            # check if the two alphanumeric characters are equivalent when lowercase
            # if they are not equivalent then the string is not a palindrome and return false
            if (s[l].lower() != s[r].lower()):
                return False
            # if the two characters are equivalent continue the loop by incrementing left pointer and decrementing right pointer
            else:
                l+=1
                r-=1
        # if it passes through the loop without returning False then we must return True since the string is indeed a palindrome
        return True
            

        # Initial solution which uses O(n) time complexity and O(n) Space Complexity
        # # first convert all uppercase letters to lowercase .lower()
        # # loop through and remove all non-alnum characters check .alnum(char)
        # newStr = ""
        # # add each letter to this new string if it is alphanumeric
        # for char in s:
        #     if (char.isalnum()):
        #         newStr += char.lower()
        # # create another string to store the reverse of this string
        # # reversedStr = ""
        # # # loop through the alphanumeric string in reverse and concatenate it to the string

        # # for i in range(len(newStr)):
        # #     reversedStr += newStr[len(newStr) -1 -i]
        # # # If the two strings are equivalent then return True since they are palindromes
        # # # else return false because they are not equivalent forward and reverse
        # return newStr == newStr[::-1]
          
        # # Time Complexity O(n + m) = O(n) where n = len(s) and m = len(newStr)
        # # Space Complexity O(2n) = O(n) where n = newStr 
        

        """
        :type s: str
        :rtype: bool
        """
        
