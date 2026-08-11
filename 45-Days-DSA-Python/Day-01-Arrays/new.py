#two poniter approach for twoSum
def twoSum(arr, target):
    #sort the array 
    arr.sort()
    l = 0
    r = len(arr) - 1
    sum = 0
    while l < r:
        sum = arr[l] + arr[r]
        if sum == target:
            return [l, r]
        elif sum < target:
            l += 1
        else:

           r -= 1
arr = [2,7,11,15]
print(twoSum(arr, 9))     




