
class Solution:
    def threeSum(self, nums) :
        if nums == []: return []
        mapB = {}

        for i in range(len(nums)):
            if nums[i] not in mapB:
                mapB[nums[i]] = 1
            else:
                mapB[nums[i]] += 1

        if 0 in mapB:
            if mapB[0] == len(nums) and len(nums) >= 3: return [[0,0,0]]


        # return mapB
        mapA = mapB.copy()

        # res = []
        res = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] in mapA:
                    mapA[nums[i]] -= 1
                if nums[j] in mapA:
                    mapA[nums[j]] -= 1   
                if 0 - nums[i] - nums[j] in mapA and mapA[0 - nums[i] - nums[j] ] > 0:
                    temp = [nums[i],nums[j],0 - nums[i] - nums[j]]
                    temp.sort()
                    s2 = tuple(temp)
                    res.add(s2)
                    mapA[0 - nums[i] - nums[j]] -= 1
                else:
                    mapA[nums[j]] += 1   
                    mapA[nums[i]] += 1
            mapA = mapB.copy()

            if 0 in mapA:
                if mapA.get(0) >=3:
                    res.add((0,0,0))

            res2 = []

            for i in res:
                res2.append(list(i))

            # res.sort()
        return res2
        s1 = []

        for i in range(len(res)):
            if res[i] not in s1:
                s1.append(res[i])

        return s1


nums = [1]

s1 = Solution()
print(s1.threeSum(nums))