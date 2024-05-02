
def helper_swap(nums: list, left: int, right:int) -> None:

    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp




def bubble(nums: list) -> None:

    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            # left = nums[i]
            # right = nums[j]

            if nums[i] > nums[j]:
# need to pass their indicies... 
                helper_swap(nums,i, j )
    return nums


numbers = [3,2,1]

#print(numbers)

print(bubble(numbers))













  

