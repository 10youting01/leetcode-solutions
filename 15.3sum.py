class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        zeros = []
        for i in range(len(nums)-2):
            # i > 0 if for [i-1], and this check is for avoid same i for same 
answer
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    zeros.append([nums[i], nums[left], nums[right]])
                    # To avoid same answer with same i
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
