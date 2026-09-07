class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l , r = 0, len(s) - 1
        out = 0 
        l = 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            out = max(out, r - l + 1)
        return out


            


        