class Solution:
    def removeDuplicates(self, nums) -> int:

        slow = 0
        fast = 0

        while fast < len(nums) - 1 :
            if nums[fast] != nums[fast+1]:
                nums[slow+1] = nums[fast+1]
                fast += 1
                slow += 1
            else:
                fast += 1

        return slow+1


nums =  [0,0,1,1,1,2,2,3,3,4]


s1 = Solution()
res = s1.removeDuplicates(nums)

print(res)