class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = 0
        j = 0
        a = []
        while k < m and j < n:
            if nums1[k] <= nums2[j]:
                a.append(nums1[k])
                k += 1
            elif nums2[j] < nums1[k]:
                a.append(nums2[j])
                j += 1
        while k < m:
            a.append(nums1[k])
            k += 1

        while j < n:
            a.append(nums2[j])
            j += 1

        for i, value in enumerate(a):
            nums1[i] = value
        return nums1


