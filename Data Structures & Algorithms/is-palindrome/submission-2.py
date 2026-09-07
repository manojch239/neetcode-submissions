class Solution:
    def isPalindrome(self, s: str) -> bool:
        #turn in to alphanumeric
        # s = s.split(" ")
        news = ''
        for l in s:
            if l.isalnum():
                news += l.lower()
        # for letter in s:
        #     if not letter.isalnum():
        #         s.replace(letter,"")
        
        # i , j = 0, len(s) - 1

        # for i in range((len(s) // 2) + 1):

        #     if (s[i] == s[j] and i <= j):
        #          i += 1
        #          j -= 1
        #          out = True
        #     else: 
        #         out = False
        # return out

        return news == news[::-1]


            


        

        