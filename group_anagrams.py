class Solution(object):
    def groupAnagrams(self, strs):
        # key is string sorted and value is a list of anagrams related to that sorted key
        hashmap = {}
      # loop through each string in the array of strings
        for string in strs:
          # if its an empty string the sorted string is empty else sort the string in alphabetical order in order to determine the bucket to place the anagram word in
            if string == "":
                sorted_string = ""
            else:
                sorted_string = ''.join(sorted(string))
                # if the sorted string is not in the hashmap that means we have not yet encountered this anagram and we must initialize a new list with the initial string but 
                # have the sorted string as the key to refer to this bucket. This is because all anagrams have the same sorted combination of letters otherwise they aren't anagrams
  
            if (sorted_string not in hashmap):
                hashmap[sorted_string] = [string]
            # If we have seen this sorted string then the anagram exists in our hashmap and we must place this string into the list of this specific anagram
            else:
                hashmap[sorted_string].append(string)
            # return the values of the hashmap since we only need the lists of lists of anagrams not the sorted keys referring to each anagram
        return hashmap.values()


        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
