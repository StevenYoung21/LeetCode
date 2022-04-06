
from turtle import right


class Solution:
    def twoSum(self, numbers , target):
        
        length = len(numbers)
        
        left , right = 0 , length-1

        for i in range(length):
            if numbers[left] + numbers[right] > target:
                right = right -1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return[left+1,right+1]

## 双指针


numbers = [2,7,11,15]
target = 9


s1 = Solution()
res = s1.twoSum(numbers,target)

print(res)