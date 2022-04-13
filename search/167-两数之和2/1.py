class Solution:
    def twoSum(self, numbers , target):
        
        length = len(numbers)
        
        l , r = 0 , length - 1

        while l <= r :
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l+1,r+1]

        return length

## 双指针

numbers = [2,3,4]

target = 6

s1 = Solution()

rseult = s1.twoSum(numbers,target)

print(rseult) 