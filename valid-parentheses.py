class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ''
        for s in strs:
            msg += str(len(s)) + '#' + s
        return msg

    def decode(self, s: str) -> List[str]:
        i = 0
        strs  = []
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            strs.append(s[j+1:j+length+1])
            i = j + length + 1
        return strs
