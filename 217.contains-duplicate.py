class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable.keys():
                return True
            else:
                hashtable[nums[i]] = i
        return False
