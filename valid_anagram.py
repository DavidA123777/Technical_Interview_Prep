class Solution(object):
    def isAnagram(self, s, t):
        # anagram means both strings contain the same letters and same amount of each letter
        hash1 = {}
        hash2 = {}
        # Base case if the lengths of both strings are not equal then they are not anagrams of each other
        if len(s) != len(t):
            return False
        # Base case if the lengths of the strings are 1 then if they are the same letter then they are anagrams
        if (len(s) == 1):
            if(s[0] == t[0]):
                return True
            return False
        # loop through both strings and add each char from each string to their respective hashmap
        # if that letter exists in the hashmap then increment its value by 1 and if not then set its value to 1
        for i in range(len(s)):
            if (s[i] not in hash1):
                hash1[s[i]] = 1
            else: 
                hash1[s[i]] += 1
            if (t[i] not in hash2):
                hash2[t[i]] = 1
            else:
                hash2[t[i]] += 1
        # If the hashmaps are equal then both strings have the same letters and the same quantities of each letter and are therefore anagrams
        if (hash1 == hash2):
            return True
        else:
            return False
