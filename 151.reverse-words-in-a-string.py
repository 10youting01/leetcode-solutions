class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ans = ""
        for word in s:
            if ans == "":
                ans = ''.join((word, ans))
            else:
                ans = ''.join((word, ' ', ans))
        return ans
