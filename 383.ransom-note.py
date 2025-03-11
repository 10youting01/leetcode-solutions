class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)
        # Counter is used to count the occurrences of each letter in ransomNote and magazine.
        # Then, we check if ransomNote's letter counts are all less than or equal to magazine's.
        
        
