n = int(input())
nums = [int(i) for i in input().split()]
nums.sort(reverse=True)
#test
print(nums)
print(sum(nums[::2]) - sum(nums[1::2]))