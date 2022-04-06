
class Solution:
    def twoSum(self, numbers , target):
        
        length = len(numbers)
        

        for i in range(length):
            left , right = i+1 , length-1
            while(left<=right):
                mid = left + (right-left)//2
                if target - numbers[i] > numbers[mid]:
                    left = mid + 1
                elif target - numbers[i] < numbers[mid]:
                    right = right - 1
                else:
                    return [i+1,mid+1] 


## 二分查找超时


numbers = [2,7,11,15]
target = 9


s1 = Solution()
res = s1.twoSum(numbers,target)

print(res)