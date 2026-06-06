class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # dic1 = Counter(s1)
        dic1 = {}
        for s in s1:
            dic1[s] = dic1.get(s, 0) + 1
        for i in range(len(s1)):
            dic1[s2[i]] = dic1.get(s2[i], 0) - 1
        if all(v == 0 for v in dic1.values()):
                return True

        for left in range(1, len(s2) - len(s1) + 1):
            right = left + len(s1) - 1
            dic1[s2[left-1]] = dic1.get(s2[left-1], 0) + 1
            dic1[s2[right]] = dic1.get(s2[right], 0) - 1
            if all(v == 0 for v in dic1.values()):
                return True


        return False

