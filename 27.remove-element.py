#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_num = nums.count(val)
        while val_num != 0:
            nums.remove(val)
            val_num -= 1
        return len(nums)
    
# if __name__ == '__main__':
#     sol = Solution()
#     nums = [3,2,2,3]
#     ans = sol.removeElement(nums, 3)
#     print(ans)
        
# @lc code=end

'''
1. list.count(x): find out how many times x are in the list
2. while + list.remove(x): remove all the x in the list
3. len?
'''