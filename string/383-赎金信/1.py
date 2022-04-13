from dis import dis


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dis1 = {}
        dis2 = {}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in dis1:
                dis1[ransomNote[i]] = 1
            else:
                dis1[ransomNote[i]] += 1

        for j in range(len(magazine)):
            if magazine[j] not in dis2:
                dis2[magazine[j]] = 1
            else:
                dis2[magazine[j]] += 1

        for k in dis1:
            if k not in dis2: return False
            else:
                if dis1[k] > dis2[k]:
                    return False
                # print (k)

        return True



ransomNote = "aaab"

magazine = "aaabbd"

s1 = Solution()
res = s1.canConstruct(ransomNote,magazine)

print(res)