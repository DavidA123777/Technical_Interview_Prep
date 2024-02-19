class Solution(object):
    def twoSum(self, numbers, target):
        # we are given an array of integers numbers
        # we must find two indices such that numbers[index1] + numbers[index2] == target
        # however we must consider that we should add 1 to each index since we are starting by 1 instead of 0 in this case
        # Since the array of numbers are sorted we can use 2 pointers
        # start at the beginning and end if the left + right > target then decrement right pointer
        # if left + right < target then increment left pointer

        left, right = 0, len(numbers) - 1
        while (left < right):
            if (numbers[left] + numbers[right] == target):
                return [left + 1, right + 1]
            if (numbers[left] + numbers[right] < target):
                left += 1
            if (numbers[left] + numbers[right] > target):
                right -= 1
           
            

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
