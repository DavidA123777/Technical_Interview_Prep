class Solution(object):
    def maxArea(self, height):
        # Solution using two pointers
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # height is an array of integers with length n
        # line going from the height of one line to the other line
        # we need a variable to store the max area so far
        # return the max amount of water a container can store
        left, right = 0, len(height) - 1

        # we take the min height of the two pointers
        # we take the length as the difference between the two pointers
        # we will have a max_area and update the pointers accordingly
        max_area = 0
      
        while left < right:
          # Take the minimum of the two heights 
            height1 = min(height[left],height[right])
          # the length is the difference between the two pointers
            length = right - left
          # area = base * height
            area = height1 * length
          # if the calculated area is larger than the currenly max area then replace max area with this larger area
            if (area > max_area):
                max_area = area
            # if the height of the left pointer is less than the height of the right pointer increment the left pointer so you can possibly find a larger area
            if (height[left] < height[right]):
                left += 1
                continue
            # if the height of the left pointer is greater than the height of the right pointer decrement the right pointer so you can possibly find a larger area
            if (height[left] > height[right]):
                right -= 1
                continue
            # if they are the same height then either increment left pointer or decrement right pointer
            left += 1
        # return the max area generated
        return max_area

        """
        :type height: List[int]
        :rtype: int
        """
        
