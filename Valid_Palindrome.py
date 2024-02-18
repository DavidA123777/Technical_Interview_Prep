class Solution(object):
    def isPalindrome(self, s):
        # first convert all uppercase letters to lowercase .lower()
        # loop through and remove all non-alnum characters check .alnum(char)
        s = s.lower()
        newStr = ""
        # add each letter to this new string if it is alphanumeric
        for char in s:
            if (char.isalnum()):
                newStr += char
        if (newStr == newStr[::-1]):
            return True
        else:
            return False
                
        # slower method
        # # create another string to store the reverse of this string
        # reversedStr = ""
        # # loop through the alphanumeric string in reverse and concatenate it to the string

        # for i in range(len(newStr)):
        #     reversedStr += newStr[len(newStr) -1 -i]
        # # If the two strings are equivalent then return True since they are palindromes
        # # else return false because they are not equivalent forward and reverse
        # if (newStr == reversedStr):
        #     return True
        # else:
        #     return False

        # 
        # Time Complexity O(n + m) = O(n) where n = len(s) and m = len(newStr)
        # Space Complexity O(2n) = O(n) where n = newStr 


        """
        :type s: str
        :rtype: bool
        """
        
