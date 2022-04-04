class Solution:
    def search(self, nums, target: int) -> int:
        len1 = len(nums)

        left = 0
        right = len1-1

        while(left <= right):

            mid = (right - left)//2 + left
            ## （右-左）//2 得到的是这两个下标中间的相对位置，要算mid在整个数组中的位置就还要加上left

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
        


nums =  [0,5]

target = 2

s1 = Solution()

rseult = s1.search(nums, target)

print(rseult) 
