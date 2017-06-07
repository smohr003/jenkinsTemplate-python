import itertools  

class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	#print(type(nums[0]))
        # your solution here
	if type(nums[0]) is not int: 
	    return 0    
	nums.sort()
 
        return nums[0] + nums[int(len(nums)/2)]
	#return 0 
