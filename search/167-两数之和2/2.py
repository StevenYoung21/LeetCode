from tkinter import W


class Solution:
    def twoSum(self, numbers , target):
        
        length = len(numbers)
        
        for i in range(length):

            l , r = i+1 , length - 1

            while l <= r :
                mid = l + (r-l) // 2 
                if numbers[i] + numbers[mid] > target:
                    r = mid - 1
                elif numbers[i] + numbers[mid] < target:
                    l = mid +1
                else:
                    return[i+1,mid+1]   

## 二分查找

numbers = [2,3,4]

target = 6

s1 = Solution()

rseult = s1.twoSum(numbers,target)

print(rseult) 