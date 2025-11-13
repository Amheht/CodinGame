# Written by Joseph Garcia

n = int(input())

nums = [[abs(int(n)),int(n)] for n in input().split()]

if n > 0:
    closest = nums[0]
    for i in range(1, len(nums)):
        if nums[i][0] < closest[0]:
            closest = nums[i]
        elif nums[i][0] == closest[0]:
            if nums[i][1] > closest[1]:
                closest = nums[i]
    print(closest[1])
else:
    print(0)
