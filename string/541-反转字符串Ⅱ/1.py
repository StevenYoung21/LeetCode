

class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        res = ''
        
        i = 0

        while i < len(s):

            p1 = s[i:i+k][::-1]
            p2 = s[i+k:i+k+k]
            res += p1 + p2    
            i += 2*k

        return res

            
    
            

s = "abcdefg"

k =2

s1 = Solution()
print(s1.reverseStr(s,k))

