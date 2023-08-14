arr = [3, 1, 9, 7, 5, -1, 7]
arr2 = [1,2,3,4,5,6,7,8,2,4]
target = 8

arr.sort()
def two_sum(arr, target):
    list = []
    l=0
    r= len(arr) - 1

    while(l < r):
        if(arr[l] + arr[r] == target):
            list.append([arr[l], arr[r]])
            l+=1
            r-=1
        elif(arr[l] + arr[r] < target):
            l+=1
        else:
            r-=1

    return list


def three_sum(nums, target):
    nums.sort()

    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return result

twoSum = two_sum(arr, target)
threeSum = three_sum(arr2, target)

print("Sorted array: ")
print(arr)

print("Two sum: ")
for i in range(0,len(twoSum)):
    print(twoSum[i])

print("Three sum: ")
for i in range(len(threeSum)):
    print(threeSum[i])