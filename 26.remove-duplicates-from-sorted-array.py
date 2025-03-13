class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0

        for new in range(1, len(nums)):
            if nums[new] != nums[unique]:
                unique += 1
                nums[unique] = nums[new]
                
        return unique+1
        
        
