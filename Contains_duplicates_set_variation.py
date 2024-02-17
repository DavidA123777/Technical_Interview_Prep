class Solution(object):
    def containsDuplicate(self, nums):
#         hash_map = {}
#         for num in nums:
#             if (num in hash_map):
#                 return True
#             hash_map[num] = 1
#         return False

        hashset = set();
        for num in nums:
            if num in hashset:
                return True;
            else:
                hashset.add(num);
        return False;


        """
        :type nums: List[int]
        :rtype: bool
        """
        
