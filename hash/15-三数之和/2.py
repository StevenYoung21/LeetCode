
class Solution:
    def threeSum(self, nums) :
        if len(nums) < 3 : return []
        nums.sort()

        mapB = {}

        for i in range(len(nums)):
            if nums[i] not in mapB:
                mapB[nums[i]] = 1
            mapB[nums[i]] += 1

        # return mapB

        if 0 in mapB:
            if mapB[0] == len(nums) : return [[0,0,0]]

        res = set()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue            
            hash = {}
            for j in range(i+1,len(nums)):



                if nums[j] not in hash:
                    hash[0 - nums[i] - nums[j]] = 1
                else:
                    res.add((nums[i],0 - nums[i] - nums[j],nums[j]))

        return list(res)


nums = [1,-1,0,0]

s1 = Solution()
print(s1.threeSum(nums))