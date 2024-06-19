class Solution:
    def search(self, nums, target: int) -> int: # type: ignore
        """
        [6,7,1,2,3,4,5]
        """
        def find_rotate_index(numbers):
            left = 0 
            right = len(numbers) - 1
            while left < right:
                mid = (left + right) // 2
                if numbers[right] < numbers[mid]:
                    left = mid + 1
                else:
                    right = mid
            return left 
        
        rotate_index = find_rotate_index(nums)
        if rotate_index == -1:
            return -1 

        n = len(nums)
        left = rotate_index 
        right = len(nums) + rotate_index - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid % n] < target:
                left = mid + 1 
            elif nums[mid % n] > target:
                right = mid - 1
            else:
                return mid % n
        return -1
