class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dis1 = {}
        dis2 = {}

        for i in range(len(s)):
            if s[i] not in dis1:
                dis1[s[i]] = 1
            else:
                dis1[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in dis2:
                dis2[t[j]] = 1
            else:
                dis2[t[j]] += 1

        if len(dis1) != len(dis2) : return False
 
        for k in dis1:
            if k not in dis2: return False
            else:
                if dis1[k] != dis2[k]:
                    return False
                # print (k)        

        return True


s = "a"

t = "ab"

s1 = Solution()
res = s1.isAnagram(s,t)

print(res)