class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0

        while len(nums1) != m:
            del nums1[-1]
        while len(nums2) != n:
            del nums2[-1]

        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                m += 1
                j += 1
            i += 1

        if i == m:
            for p in range(j, n):
                nums1.append(nums2[p])


a = Solution()
nums1 = [0]
nums2 = [1, 2, 3, 5, 6]
a.merge(nums1, 0, nums2, len(nums2))
print(nums1)
