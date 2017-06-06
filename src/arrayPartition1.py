import itertools  

class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
	#max_sum = 0 
	#itertools.(nums, 2)
	#for i in range(len(nums)): 
        #    for j in  
	nums.sort()
 
        return nums[0] + nums[int(len(nums)/2)]

