class Solution(object):
    def intersect(self, nums1, nums2):
        inte = []

        for i in range(len(nums1)):
            p = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    inte.append(nums2[j])
                    p=1
                    break
            if p == 1:
                nums2.pop(j)

        print(inte)


s = Solution()

s.intersect([4,9,5],[9,4,9,8,4])

