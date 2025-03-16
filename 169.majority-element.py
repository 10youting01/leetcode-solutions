class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = dict.fromkeys(nums, 0)
        for i in range(n):
            dic[nums[i]] = dic[nums[i]]+1
        majority = max(dic, key=dic.get)
        return majority
        
