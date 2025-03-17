class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        dic = {}
        for i in range(len(answers)):
            if answers[i] not in dic or dic[answers[i]] == 0:
                res += answers[i]+1
                dic[answers[i]] = answers[i]
            else:
                dic[answers[i]] -= 1
        return res
# answers[i] = there are at most i+1 rabbits with same color, so answers[i] rabbits are left to answer to be the same group after answers[i] 
        
