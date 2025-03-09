class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for i in range(len(magazine)):
            if magazine[i] in mag:
                mag[magazine[i]] = mag.get(magazine[i], 0) + 1
            else:
                mag[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in mag and mag.get(ransomNote[i], 0) >= 1:
                mag[ransomNote[i]] = mag.get(ransomNote[i], 0) - 1
            else:
                return False
        return True
        
        
