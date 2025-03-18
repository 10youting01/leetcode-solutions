class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        thres = n // 3
        first = None
        second = None
        countf = 0
        counts = 0
        ans = []
        
        for num in nums:
            if num == first:
                countf += 1
            elif num == second:
                counts += 1
            elif countf == 0:
                first = num
                countf += 1
            elif counts == 0:
                second = num
                counts += 1
            else:
                countf -= 1
                counts -= 1
        if first != None and nums.count(first)>thres:
            ans.append(first)
        if second != None and nums.count(second)>thres:
            ans.append(second)
        return ans
            
