from turtle import left, right


class Solution:
    def search(self, nums, target: int) :
        
        ## 头尾指针
        left , right = 0 , len(nums)-1

        while left<=right:
            mid = left + (right-left)//2

            ## 如果目标值大于中间值.则左指针移动到中间值的右侧,即+1
            if target > nums[mid]:
                left = mid + 1 

            ## 如果目标值小于中间值.则右指针移动到中间值的左侧,即-1    
            elif target < nums[mid]:
                right = mid - 1

            ## 与目标值相等,则返回中间值的索引
            else:
                return mid
        return -1
            



nums = [-1,0,3,5,9,12]
target = 10

s1 = Solution()

rseult = s1.search(nums,target)

print(rseult) 