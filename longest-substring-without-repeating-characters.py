class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in dic and dic[s[right]] >= left:
                left = max(left, dic[s[right]] + 1)
            if right - left + 1 > max_len:
                max_len = right - left + 1
            dic[s[right]] = right

        return max_len

