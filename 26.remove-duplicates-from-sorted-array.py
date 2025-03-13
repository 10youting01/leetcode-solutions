class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = dict.fromkeys(nums, 0)
        for i in range(len(nums)):
            dic[nums[i]] += 1
        for key, value in dic.items():
            if value > 1:
                for i in range(value-1):
                    nums.remove(key)
        return len(nums)
        
