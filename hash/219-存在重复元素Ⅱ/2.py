
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        length1 = len(nums)
        s1 = set(nums)
        length2 = len(s1)

        if length1 == length2 : return False 


        res = set()

        for i in range(length1):

            if len(res) > k:
                res.remove(nums[i-k-1])

            if nums[i] not in res:
                res.add(nums[i])
            else:
                return True                

        return False


nums =  [1,2,3,1,2,3]

k = 2

s1 = Solution()

print(s1.containsNearbyDuplicate(nums,k))