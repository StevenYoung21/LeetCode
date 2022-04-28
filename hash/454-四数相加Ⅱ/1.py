class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:

        mapA = {}
        count = 0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] not in mapA:
                    mapA[nums1[i] + nums2[j]] = 1
                else:
                    mapA[nums1[i] + nums2[j]] += 1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if 0 - nums3[i] - nums4[j] in mapA:
                    count += mapA[0 - nums3[i] - nums4[j]]

        return count

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

s1 = Solution()
print(s1.fourSumCount(nums1,nums2,nums3,nums4))