def find_disjoint_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    
    result1 = list(set1 - set2)
    result2 = list(set2 - set1)
    
    return [result1, result2]