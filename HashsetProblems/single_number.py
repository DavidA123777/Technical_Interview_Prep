# Hash set solution for single number. Return the only value which appears only 1 time while every other number is there twice\
class Solution(object):
    def singleNumber(self, nums):
#         We must use constant space which means either no data structures or a set
#         We must find the value of the number which is not repeated twice
#         We must use linear runtime complexity meaning only one loop through for a search (brute force solution wont count)
        hashset = set();
          
        answer = 0;
#         We can add items to the set and if they appear twice then we can remove it from the set

        for num in nums:
            if (num in hashset):
                hashset.remove(num);
            else:
                hashset.add(num);
#         We will then only be left with one item in the hashset which we can return like this:
        for num in hashset:
            return num;
        """
        :type nums: List[int]
        :rtype: int
        """
        
