class Solution(object):
    def isHappy(self, n):
# We have a number n
# we must take the sum of the squares of its digits and see if it equals 1
# if not then we must keep the process going        
        hashset = set()
        while n != 1:
            if n in hashset:
                return False;
            hashset.add(n);
            n = str(n);
            sum = 0;
            for val in n:
                sum += int(val) * int(val);
            n = sum;
            # n = sum(int(digit)**2 for digit in str(n))
        return True;

        """
        :type n: int
        :rtype: bool
        """
        
        
        
        
#         Wrong initial solution:
#         sum = 0;
#         hashset = set();
#         string_n = str(n);
        
#         while (sum != 1):
            
#             sum = 0;
#             arr = [];
#             for digit in string_n:
#                 arr.append(int(digit))
#             for num in arr:
#                 sum += (num*num);
        
#             newVal = "";
#             for val in arr:
#                 val = str(val);
#                 newVal += val;
                
#             if(newVal in hashset):
#                 return False            
#             hashset.add(newVal);
#             string_n = newVal
            
