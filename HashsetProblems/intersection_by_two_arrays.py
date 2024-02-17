class Solution(object):
    def intersection(self, nums1, nums2):
#         We are given 2 arrays of integers
#         We must create an array of their intersection (all elements common to both arrays)
#         I am going to start by creating a set which will store every value from nums1 besides duplicates
# Then I will loop through the second array and see if the element exists in the set, if it does then I will append them to a new set which will be returned at the end
        hashset = set();
        for num in nums1:
            hashset.add(num);
        intersection_set = set();
        for num in nums2:
            if num in hashset:
                intersection_set.add(num);
        return intersection_set

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
