class Solution:
    def specialArray(self, nums) -> int:

        maxNum = max(nums)
        sor = sorted(nums, reverse = True)

        if maxNum == 0 and len(nums) > 0 : return -1

        if nums == [0] : return 0

        if sor[-1] >= len(nums) : return len(nums)

        for i in range(1,len(sor)):
            if sor[i] < i and i <= sor[i-1]:
                return i 

        return -1




nums = [0,4,3,0,4]

s1 = Solution()

rseult = s1.specialArray(nums)

print(rseult)