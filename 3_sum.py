class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if ((nums[0] + nums[1] + nums[2]) == 0):
                return [[nums[0],nums[1],nums[2]]]
            else:
                return []
        triplets = set()
        left, right = 0, len(nums) -1
        # We can try sorting the nums array
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) -1
            while (left < right):
                if (nums[i] + nums[left] + nums[right] < 0):
                    left += 1
                elif (nums[i] + nums[left] + nums[right] > 0):
                    right -= 1
                else:
                    if ((nums[i], nums[left], nums[right]) in triplets):
                        left += 1 
                        continue
                    else:
                        triplets.add((nums[i], nums[left], nums[right]))
                        left += 1
        return triplets



        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
