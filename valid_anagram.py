class Solution(object):
    def isAnagram(self, s, t):
        # Method 1:
        
        # # anagram means both strings contain the same letters and same amount of each letter
        # hash1 = {}
        # hash2 = {}
        # # Base case if the lengths of both strings are not equal then they are not anagrams of each other
        # if len(s) != len(t):
        #     return False
        # # Base case if the lengths of the strings are 1 then if they are the same letter then they are anagrams
        # if (len(s) == 1):
        #     if(s[0] == t[0]):
        #         return True
        #     return False
        # # loop through both strings and add each char from each string to their respective hashmap
        # # if that letter exists in the hashmap then increment its value by 1 and if not then set its value to 1
        # for i in range(len(s)):
        #     if (s[i] not in hash1):
        #         hash1[s[i]] = 1
        #     else: 
        #         hash1[s[i]] += 1
        #     if (t[i] not in hash2):
        #         hash2[t[i]] = 1
        #     else:
        #         hash2[t[i]] += 1
        # # If the hashmaps are equal then both strings have the same letters and the same quantities of each letter and are therefore anagrams
        # if (hash1 == hash2):
        #     return True
        # else:
        #     return False





        # Method 2:
        
        # Time complexity O(nlogn + mlogm)
        # Space complexity of O(n) or O(1) depending on the sorting algorithm used
        # Check if the sorted values of each string are equivalent. If they are then they are anagrams because all equivalent anagrams
        # have the same sorted string
        # return sorted(s) == sorted(t)



        # Method 3:

        # Time Complexity O(n) where n is the length of s
        # Space Complexity O(2*26) = O(52) = O(1) because the letters consist of english lowercase letters only so only 26 different possible keys
        # Base case if the lengths are not equal then they aren't anagrams of each other
        if (len(s) != len(t)):
            return False
        # initialize 2 hashmaps to store the characters and their occurrences for each of the two strings
        map1, map2 = {}, {}
        # loop through the length of either s or t since they are the same length
        # check if the letter exists in each respective hashmap and if not then set the value to 0 + 1.
        # If it does exist then increment it by 1
        for i in range(len(s)):
            map1[s[i]] = map1.get(s[i], 0) + 1
            map2[t[i]] = map2.get(t[i], 0) + 1
        # return True if each hashmap is equivalent meaning they store the same letters and occurrence of each letter
        # return false if they are not equivalent meaning they are 2 strings of the same length with different letters or
        # different occurrences of each letter
        return map1 == map2
