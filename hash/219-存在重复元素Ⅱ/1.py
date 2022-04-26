
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        length1 = len(nums)
        s1 = set(nums)
        length2 = len(s1)

        if length1 == length2 : return False 

        left = 0
        right = 0

        res = {}

        while right < length1:
            if nums[right] not in res :
                res[nums[right]] = right
            else:
                while left < right:
                    if nums[right] == nums[left]:
                        if right - res[nums[right]] <= k:
                            return True
                        else:
                            res[nums[right]] = right
                            left = 0
                            break
                    else:
                        left += 1
                
            right += 1

        return False


nums =  [1,2,3,1]

k = 3

s1 = Solution()

print(s1.containsNearbyDuplicate(nums,k))