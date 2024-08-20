nums = [2,7,11,15]
target = 9
indic = []
n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            indic.append(i)
            indic.append(j)
print(indic)
