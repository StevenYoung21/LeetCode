class Solution:
    def findMin(self, nums) -> int:

        l , r = 0 , len(nums)-1

        if len(nums) == 1 : return nums[0]
        if nums[-1] < nums[-2]: return nums[-1] 

        while( l<=r ):
            mid = l + (r-l) // 2 
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] < nums[l]:
                r = r - 1
            else: 
                l = l + 1

        return nums[0]

'''
思路:
首先考虑用二分法找到数组中最小的那个数, 按照数组移动的规律, 最小的数一定是小于前一个数, 而且也小于后一个数:
nums[mid] < nums[mid-1] and num[mid] < nums[mid+1]   
如: 4,5,6,7,0,1,2  之中的0, 小于 7 也小于 1

然后考虑怎么移动首位指针:
原数组是升序排列的, 如果有移动数组, 则移动到前面去的那一段一定是末尾较大的那些数, 如:
原串: 1 2 3 4 5  移动后: 4 5 1 2 3  
如果 mid 在右边较小的那串数组中时, 一定会有 nums[mid] < nums[l], 这时候把尾指针向左移动一位即可.
同理, mid 在左边较大数组中时, nums[mid] > nums[r], 头指针向右移动一位.

最后考虑边界情况:
1. 当最小值是一个元素时, 则原数组移动的次数正好等于数组的长度, 数组等于没有移动, 原数组是升序排列的, 则第一个数nums[0]就是最小值
2. 当最小值是最后一个元素时, 则数组最后一个元素一定小于倒数第二个元素, 所以当nums[-1] < nums[-2]时, 直接返回nums[-1]

'''



nums = [2,1]

s1 = Solution()
print(s1.findMin(nums))