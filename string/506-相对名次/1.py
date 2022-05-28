class Solution:
    def findRelativeRanks(self, score):

        topThree = ["Gold Medal","Silver Medal","Bronze Medal"]

        res = []

        dic = {}

        for i in score:
            if i not in dic:
                dic[i] = i

        keysSort = sorted(dic.keys(), reverse=True)
        
        k = 1

        for i in range(len(keysSort)):
            if i < 3:
                dic[keysSort[i]] = topThree[i]
            if i >=3 :
                dic[keysSort[i]] = str(k)

            k += 1
            
        res = list(dic.values()) 

        return res



score = [5,4,3,2,1]


s1 = Solution()

print(s1.findRelativeRanks(score))