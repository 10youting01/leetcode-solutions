class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        dic = {}
        diff = 0
        max_len = 0

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            if (right - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1
            if right - left + 1 > max_len:
                max_len = right - left + 1
            
        return max_len