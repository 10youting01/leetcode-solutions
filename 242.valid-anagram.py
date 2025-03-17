class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = dict.fromkeys(t, 0)
        for char in t:
            dic[char] += 1
        for char in s:
            if char not in dic or dic[char] < 0:
                return False
            else:
                dic[char] -= 1
        if any(dic.values()):
                return False
        return True
