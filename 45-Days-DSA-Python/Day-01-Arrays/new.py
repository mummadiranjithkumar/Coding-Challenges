#two poniter approach for twoSum
def twoSum(arr, target):
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



arr=[10,20,30,40]
target=40
index=0
found = False
for i in arr:
    if target == i:
        found = True
        print("found at: ", index)

    elif index < len(arr):
        index += 1
if found:
    print("Not Found")   






arr=[1,2,2,3,2,4]
target=2
count = 0
for i in arr:
    if target == i:
        count += 1

print("frquency of a number: ", count)

arr = [10,20,30,40]
count = 0
total = 0
for i in arr:
    count += 1
    total += i

avg = total / count
print("avg of numbers: ", avg)

arr = [10,20,30,40]
small = arr[0]
largest = arr[0]
sum = 0
count = 0
target = 40
for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]
    elif arr[i] > largest:
        largest = arr[i]
    sum += arr[i]
    count += 1
    if target == arr[i]:
        print(f"index of elemnt {target}: ", i)
print("maximum elemnt in the array: ", largest)
print("minimum element in the array: ", small)
print("sum of all elements in the array: ", sum)
print("no of elements in the array: ", count)



arr = [10,20,30,40,50]
li = []
for i in range(len(arr)-1, -1, -1):
    li.append(arr[i])
print("reversed list: ", li)
print(arr[-1:-1:-1])

l = 0
r = len(arr) - 1
li = []
while l <= r:
    li.append(arr[r])
    r -= 1
print(li)
l = 0
r = len(arr) - 1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
print("arr:", arr)


arr = [1,2,3,2,1]
l = 0
r = len(arr) - 1
palindrome = True
while l < r:
    
    if arr[l] != arr[r]:
        palindrome = False
        print("not palindrome")
        break

        
    elif l <= r:
        l += 1
        r -= 1
if palindrome:
    print("yes it is palidrome")
    
    


arr = [1,1,2,2,3,4,4]
l = 0
for i in range(i+1, len(arr)):
    if arr[i] != arr[l]:
        l += 1
        arr[l] = arr[i]
    
print("unique elements: ", arr[:l+1])
print("no of unique elemets: ", l+1)


