class Solution:
    def twoSum(self, numbers , target):
        
        length = len(numbers)
        
        for i in range(length):
            for j in range(i+1,length):
                if numbers[i] + numbers[j] == target:
                    return[i+1,j+1]


## 暴力解法超时



numbers = [2,7,11,15]
target = 9


s1 = Solution()
res = s1.twoSum(numbers,target)

print(res)