class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums = []
        for i in arr2:
            for p in range(arr1.count(i)):
                nums.append(i)
                if(i in arr1):
                    arr1.remove(i)
        return nums+sorted(arr1)
