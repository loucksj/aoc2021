def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    while len(nums1) + len(nums2) >= 3:
        removeLargest(nums1, nums2)
        removeSmallest(nums1, nums2)
    return averageOf(nums1, nums2)

#remove largest element between two sorted arrays
def removeLargest(nums1: list[int], nums2: list[int]):
    last1 = len(nums1) - 1
    last2 = len(nums2) - 1
    if len(nums1) > 0 and len(nums2) > 0:
        if nums1[last1] >= nums2[last2]:
            del nums1[last1]
        else:
            del nums2[last2]
    elif len(nums1) > 0:
        del nums1[last1]
    else:
        del nums2[last2]

#remove smallest element between two sorted arrays
def removeSmallest(nums1: list[int], nums2: list[int]):
    if len(nums1) > 0 and len(nums2) > 0:
        if nums1[0] <= nums2[0]:
            del nums1[0]
        else:
            del nums2[0]
    elif len(nums1) > 0:
        del nums1[0]
    else:
        del nums2[0]

def averageOf(nums1, nums2) -> float:
    return (sum(nums1) + sum(nums2)) / (len(nums1) + len(nums2))


if __name__ == '__main__':
    assert 2 == findMedianSortedArrays([1, 3], [2])