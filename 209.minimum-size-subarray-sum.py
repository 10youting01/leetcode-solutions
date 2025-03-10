class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if max(nums) >= target:
            return 1
        
        minlen = float('inf')
        sumsub = 0
        left = 0
        for right in range(len(nums)):
            # sumsub = sum(nums[left:right]) # O(n^2) for summing
            sumsub += nums[right]
            while sumsub >= target:
                minlen = min(minlen, right-left+1)
                sumsub -= nums[left]
                left += 1
        return minlen if minlen != float('inf') else 0
