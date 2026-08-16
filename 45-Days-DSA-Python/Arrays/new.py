# #two poniter approach for twoSum
# def twoSum(arr, target):
#     l = 0
#     r = len(arr) - 1
#     sum = 0
#     while l < r:
#         sum = arr[l] + arr[r]
#         if sum == target:
#             return [l, r]
#         elif sum < target:
#             l += 1
#         else:


#            r -= 1
# arr = [2,7,11,15]
# print(twoSum(arr, 9))     



# arr=[10,20,30,40]
# target=40
# index=0
# found = False
# for i in arr:
#     if target == i:
#         found = True
#         print("found at: ", index)

#     elif index < len(arr):
#         index += 1
# if found:
#     print("Not Found")   






# arr=[1,2,2,3,2,4]
# target=2
# count = 0
# for i in arr:
#     if target == i:
#         count += 1

# print("frquency of a number: ", count)

# arr = [10,20,30,40]
# count = 0
# total = 0
# for i in arr:
#     count += 1
#     total += i

# avg = total / count
# print("avg of numbers: ", avg)

# arr = [10,20,30,40]
# small = arr[0]
# largest = arr[0]
# sum = 0
# count = 0
# target = 40
# for i in range(len(arr)):
#     if arr[i] < small:
#         small = arr[i]
#     elif arr[i] > largest:
#         largest = arr[i]
#     sum += arr[i]
#     count += 1
#     if target == arr[i]:
#         print(f"index of elemnt {target}: ", i)
# print("maximum elemnt in the array: ", largest)
# print("minimum element in the array: ", small)
# print("sum of all elements in the array: ", sum)
# print("no of elements in the array: ", count)



# arr = [10,20,30,40,50]
# li = []
# for i in range(len(arr)-1, -1, -1):
#     li.append(arr[i])
# print("reversed list: ", li)
# print(arr[-1:-1:-1])

# l = 0
# r = len(arr) - 1
# li = []
# while l <= r:
#     li.append(arr[r])
#     r -= 1
# print(li)
# l = 0
# r = len(arr) - 1

# while l < r:
#     arr[l], arr[r] = arr[r], arr[l]
#     l += 1
#     r -= 1
# print("arr:", arr)


# arr = [1,2,3,2,1]
# l = 0
# r = len(arr) - 1
# palindrome = True
# while l < r:
    
#     if arr[l] != arr[r]:
#         palindrome = False
#         print("not palindrome")
#         break

        
#     elif l <= r:
#         l += 1
#         r -= 1
# if palindrome:
#     print("yes it is palidrome")
    
    

# #remove duplicates from the list
# arr = [1,1,2,2,3,4,4]
# l = 0
# for i in range(1, len(arr)):
#     if arr[i] != arr[l]:
#         l += 1
#         arr[l] = arr[i]
    
# print("unique elements: ", arr[:l+1])
# print("no of unique elemets: ", l+1)

# #remove value from the list
# class Solution(object):
#     def removeElement(self, nums, val):
#         l = 0

#         for i in range(len(nums)):
#             if nums[i] == val:
#                 continue
#             else:
#                 nums[l] = nums[i]
#                 l += 1

#         return nums[:l]


# obj = Solution()

# nums = [0,1,2,2,3,0,4,2]
# val = 2

# print(obj.removeElement(nums, val))    
        

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):

#         i = m - 1          # Last valid element in nums1
#         j = n - 1          # Last element in nums2
#         k = m + n - 1      # Last position in nums1

#         while i >= 0 and j >= 0:

#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1

#             k -= 1

#         # Copy remaining elements from nums2 (if any)
#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

# nums1 = [1,2,3,0,0,0]
# m = 3

# nums2 = [2,5,6]
# n = 3

# obj = Solution()
# obj.merge(nums1, m, nums2, n)

# print(nums1)




# def moveZerosToEnd(nums):
#     j = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[j] = nums[i]
#             j += 1
#     while j < len(nums):
#         nums[j] = 0
#         j += 1
#     return nums
# nums = [0,1,0,3,12]
# print(moveZerosToEnd(nums))

# def plusOne(digits):
#     for i in range(len(digits)-1,-1,-1):
#         if digits[i] < 9:
#             digits[i]= digits[i] + 1
#             return digits
#         digits[i] = 0
            
#     return [1] + digits
# print(plusOne([1,2,3,4]))


#prefix sum
nums1 = []

def prefixSum(nums):
    res = 0
    for i in range(len(nums)):
        res += nums[i]
        nums1.append(res)
    return nums1
nums = [1, 2, 3, 4]
print(prefixSum(nums))


#range prefix sum from 1 to 3


def rangePrefixSum(nums2):
    
    res1 = 0
    for i in range(1, 4):
        res1 += nums2[i]
    return res1
nums2 = [2, 4, 1, 5, 3]
print(rangePrefixSum(nums2))

