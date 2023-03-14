class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums_dict = {}
        intersect_list = []

        for num in nums1: 
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for num in nums2: 
            if num in nums_dict:
                if nums_dict[num] > 0:
                    intersect_list.append(num)
                    nums_dict[num] -= 1

        return intersect_list 
        