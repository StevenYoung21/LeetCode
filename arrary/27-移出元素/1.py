class Solution:
    def removeElement(self, nums, val: int) -> int:

        slow = 0
        fast = 0
        length = len(nums)

        while fast < length:

            if nums[fast] != val:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
            else:
                 fast += 1           


        return slow 

nums = [3,2,2,3]

val = 3

s1 = Solution()
res = s1.removeElement(nums,val)

print(res)