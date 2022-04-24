from re import L


class Solution:
    def targetIndices(self, nums, target: int) :

        nums.sort()

        res = []

        def findLeft(nums, target):
            l , r = 0 , len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def findRight(nums, target):
            l , r = 0 , len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
                    

        Left = findLeft(nums,target)
        Right = findRight(nums,target)

        for i in range(Left,Right):
            res.append(i)

                
        if res != []:
           return res
        else:
            return []

nums = [1,2,2,3,5]
target = 1

s1 = Solution()
print(s1.targetIndices(nums,target))