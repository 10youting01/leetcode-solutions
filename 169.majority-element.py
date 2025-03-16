# Boyer–Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = None
        count = 0
        for i in range(len(nums)):
            if count == 0: # all settle up
                tmp = nums[i]
                count = 1
            elif tmp == nums[i]: # same as the previous one 
                count += 1
            else: # different 
                count -= 1
        return tmp

        
        
