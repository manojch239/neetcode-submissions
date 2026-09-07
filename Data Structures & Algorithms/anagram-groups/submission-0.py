class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     def charsum(word):
    #         csum = 0
    #         for c in word:
    #             csum += ord(c)
    #         return csum
    #     hashmap = {}
    #     for word in strs:
    #         hashmap[word] = charsum(word)
        
    #     for word,charsum in hashmap:

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] +=1
            res[tuple(count)].append(s)
        return list(res.values())