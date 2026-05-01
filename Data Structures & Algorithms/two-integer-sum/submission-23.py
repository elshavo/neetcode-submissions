class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #valor, index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff],i] # diff porque num es del ciclo actual
            seen[num] = i




        
#nums = [2, 7, 11, 15]
#target = 9       
        
        
        
        
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
