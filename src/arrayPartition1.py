import itertools  

class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
	if type(nums[0]) != 'int': 
	    return 0    
	nums.sort()
 
        return nums[0] + nums[int(len(nums)/2)]
	#return 0 
