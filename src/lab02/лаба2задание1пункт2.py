nums = [3,1,2,1,3]
def unique_sorted(nums):
    new_nums = sorted(set(nums))
    print(new_nums)
unique_sorted(nums)