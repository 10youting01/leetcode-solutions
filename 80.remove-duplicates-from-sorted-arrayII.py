class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 2: return 2
        two_num = 0
        twice = 1
        for pointer in range(1, len(nums)):
            if nums[pointer] == nums[two_num]:
                twice += 1
                if twice == 2:
                    two_num += 1
                    nums[two_num] = nums[pointer]
            else:
                twice = 0
                two_num += 1
                nums[two_num] = nums[pointer]
                twice += 1
        return two_num + 1
