class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = s.lower()
        s = ''.join([char for char in s if char.isalnum()])

        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        for i in range(len(s)//2):
            if s1[i] != s2[-(i+1)]:
                return False
        return True
