class Solution(object):
    def twoSum(self, nums, target):
        # Given an array of integers nums
        # integer target is the target sum
        # return the indices of the two numbers that add up to target
        # Exactly one solution and has to be two separate indices
        # base case nums is exactly 2 numbers

        if (len(nums) == 2):
            return([0,1])
        # We can create a hash map to store each of the elements that exist in the map already
        # We can then check if target - the current element is in the map
        # if that is the case then we return the index of the current element and the element of the target - current element
        # {key: val} {num: index}
        map1 = {}
        counter = 0
        for i in range(len(nums)):
            target_minus_current = target - nums[i]
            if (target_minus_current in map1):
                return ([map1[target_minus_current], i])
            else:
                map1[nums[i]] = i    
