class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            keys = ''.join(sorted(s))
            if keys not in hashmap.keys():
                hashmap[keys] = [s]
            else:
                hashmap[keys].append(s)
        return list(hashmap.values())
