# def countingSort(arr):
#     if not arr:
#         return arr

#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     for num in arr:
#         count[num] += 1

#     arr[:] = []

#     for num, freq in enumerate(count):
#         arr.extend([num] * freq)

#     return arr

# unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sortedArr = countingSort(unsortedArr)
# print("Sorted array:", sortedArr)


# nums = [2, 7, 25, 18]
# target = 9
# class Solution(object):
#     def twoSum(self, nums, target):
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i
# Solution = Solution()
# print(Solution.twoSum(nums, target))

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next


# # --------- TEST CODE (required for VS Code) ---------
# # Create linked lists: 2 → 4 → 3 and 5 → 6 → 4

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))

# sol = Solution()
# result = sol.addTwoNumbers(l1, l2)

# # Print result
# while result:
#     print(result.val, end=" ")
#     result = result.next


# next
# class Solution:
#     def twoSum(self, nums, target):
#         num_map = {}  # Hash table to store number and its index
#         for i, num in enumerate(nums):
#             complement = target - num  # Find the complement
#             if complement in num_map:
#                 return [num_map[complement], i]  # Return indices of complement and current number
#             num_map[num] = i  # Store the number with its index

# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# print(solution.twoSum(nums, target))  # Output: [0, 1]

# class MyClass:
#     def function(self):
#         x = 5
#         return x

# fuc = MyClass()
# result = fuc.function()
# print(result)

# class Listnode:
#    def __init__ (self, val= 0 , next = None):
#        self.val = val
#        self.next = next

# class Solution:
#     def addtwonum(self, l1, l2):
#         dummy = Listnode()
#         res = dummy
#         total = carry = 0
#         while l1 or l2  or carry:
#             total = carry
#             if l1:
#                 total += l1.val
#                 l1 = l1.next
#             if l2 :
#                 total += l2.val
#                 l2 = l2.next
#             num = total % 10
#             carry  = total // 10
#             dummy.next = Listnode(num)
#             dummy = dummy.next
#         return res.next

# def build_linked_list(arr):
#     dummy = Listnode(0)
#     cur = dummy
#     for x in arr:
#         cur.next = Listnode(x)
#         cur = cur.next
#     return dummy.next


# l1 = [4, 6, 4]
# l2 = [3, 4, 3]
# ll1 = build_linked_list(l1)
# ll2 = build_linked_list(l2)
# sol = Solution()
# result = sol.addtwonum(ll1,ll2)

# while result:
#     print(result.val, end = " -> ")
#     result = result.next
# print("None")


# class Solution:
#     def longestsubs(self, text):
#         last_seen = {}
#         start = 0
#         max_length = 0

#         for end in range(len(text)):
#             current_char = text[end]

#             if current_char in last_seen and last_seen[current_char] >= start:
#                 start = last_seen[current_char] + 1

#             last_seen[current_char] = end
#             max_length = max(max_length, end - start + 1)

#         return max_length


# text = "abcabcabc"
# sol = Solution()
# result = sol.longestsubs(text)
# print(result)


# class solution:
#     def twomed(self, num1, num2):
#         merged = num1+num2
#         merged.sort()
#         total = len(merged)
#         if total % 2 == 1:
#             return  float(merged[total // 2])
#         else:
#             middle1  = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1)+ float(middle2)) / 2.0

# num1 = [1,3]
# num2 = [2]
# sol = solution()
# result = sol.twomed(num1, num2)
# print(result)

# zigzag pattern
# class solution:
#     def zigzag(self, s, numrows):
#         if numrows == 1 and numrows >= len(s):
#             return s
#         rows = [""] * numrows
#         curr_rows = 0
#         direction = -1
#         for sh in s:
#             rows[curr_rows] += sh
#             if curr_rows == 0 or curr_rows == numrows - 1:
#                 direction *= -1
#             curr_rows += direction
#         return "".join(rows)

# s = "yasinahmad"
# numrows = 3
# sol = solution()
# result = sol.zigzag(s, numrows)
# print(result)

# # sting to intiger
# class solution:
#     def strint(self, s):
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31

#         i = 0
#         n = len(s)
#         # skip all spaces
#         while i < n and s[i] == " ":
#             i += 1
#         #    for sing find
#             sign = 1
#             if i < n  and s[i] == "-" or s[i] == "+":
#                 if s[i] == "-":
#                     sign = -1
#                 i += 1
#                 # for digit store
#             num = 0
#             while i < n and s[i].isdigit():
#                 digit = ord(s[i]) - ord("0")
#                 num = num * 10 + digit

#                 # for overflow check
#                 if sign* num > INT_MAX:
#                    return INT_MAX
#                 if sign* num < INT_MIN:
#                    return INT_MIN
#                 i += 1
#         return sign * num
# s = "  -42"
# sol = solution()
# result = sol.strint(s)
# print(result)


# merge k sorted list
# def merge_two_lists(a, b):
#     i = 0
#     j = 0
#     result = []

#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1

#     # Add remaining elements
#     while i < len(a):
#         result.append(a[i])
#         i += 1

#     while j < len(b):
#         result.append(b[j])
#         j += 1

#     return result

# def merge_k_lists(lists):
#     if not lists:
#         return []

#     result = lists[0]

#     for i in range(1, len(lists)):
#         result = merge_two_lists(result, lists[i])

#     return result


# a = [
#     [1,2,3],
#     [1,4,3],
#     [1,4]
# ]

# print(merge_k_lists(a))

# def fourSum(nums, target):
#     nums.sort()                # Step 1: Sort the array
#     n = len(nums)
#     result = []

#     # Fix first number (i)
#     for i in range(n - 3):

#         # Skip duplicate first numbers
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue

#         # Fix second number (j)
#         for j in range(i + 1, n - 2):

#             # Skip duplicate second numbers
#             if j > i + 1 and nums[j] == nums[j - 1]:
#                 continue

#             # Two pointers for remaining two numbers
#             left = j + 1
#             right = n - 1

#             while left < right:
#                 total = nums[i] + nums[j] + nums[left] + nums[right]

#                 if total == target:
#                     # Found one valid quadruplet
#                     result.append([nums[i], nums[j], nums[left], nums[right]])

#                     # Move both pointers
#                     left += 1
#                     right -= 1

#                     # Skip duplicate values
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#                 elif total < target:
#                     # Sum too small → move left forward
#                     left += 1

#                 else:
#                     # Sum too big → move right backward
#                     right -= 1

#     return result

# nums = [-1,-2,2,3,1,2]
# target = 0
# print(fourSum(nums,target))

# exchange node
# class listnode:
#     def __init__(self, val=0, next = None):
#         self.val= 0
#         self.next = None

# class solution:
#     def exnode(self, head):
#         dummy = listnode(0)
#         dummy.next = head
#         prev = dummy

#         while prev.next or prev.next.next:
#             first = prev.next
#             second = first.next

#             # swap
#             prev.next = second
#             first.next = second.next
#             second.next = first

#             prev = first
#         return dummy.next

# next permutation
# class Solution(object):
#     def nextPermutation(self, nums):
#         i = j = len(nums)-1
#         while i > 0 and nums[i-1] >= nums[i]:
#             i -= 1
#         if i == 0:   # nums are in descending order
#             nums.reverse()
#             return
#         k = i - 1    # find the last "ascending" position
#         while nums[j] <= nums[k]:
#             j -= 1
#             nums[k], nums[j] = nums[j], nums[k]
#             l, r = k+1, len(nums)-1  # reverse the second part
#             while l < r:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 l += 1
#                 r -= 1
# # long valid parentheses
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack=[]
#         l=['0']*len(s)
#         for ind,i in enumerate(s):
#             if i=='(':
#                 stack.append(ind)
#             else:
#                 if stack:
#                     l[stack.pop()]='1'
#                     l[ind]='1'
#         return max(len(i) for i in ''.join(l).split('0'))

# def countingSort(arr):
#     if not arr:
#         return arr
        
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     for num in arr:
#         count[num] += 1

#     arr[:] = []

#     for num, freq in enumerate(count):
#         arr.extend([num] * freq)

#     return arr

# unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sortedArr = countingSort(unsortedArr)
# print("Sorted array:", sortedArr)


# nums = [2, 7, 25, 18]
# target = 9
# class Solution(object):
#     def twoSum(self, nums, target):
#         num_map = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_map:
#                 return [num_map[complement], i]
#             num_map[num] = i
# Solution = Solution()
# print(Solution.twoSum(nums, target))

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0

#         while l1 or l2 or carry:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0

#             total = val1 + val2 + carry
#             carry = total // 10

#             current.next = ListNode(total % 10)
#             current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return dummy.next


# # --------- TEST CODE (required for VS Code) ---------
# # Create linked lists: 2 → 4 → 3 and 5 → 6 → 4

# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))

# sol = Solution()
# result = sol.addTwoNumbers(l1, l2)

# # Print result
# while result:
#     print(result.val, end=" ")
#     result = result.next


# next
# class Solution:
#     def twoSum(self, nums, target):
#         num_map = {}  # Hash table to store number and its index
#         for i, num in enumerate(nums):
#             complement = target - num  # Find the complement
#             if complement in num_map:
#                 return [num_map[complement], i]  # Return indices of complement and current number
#             num_map[num] = i  # Store the number with its index

# nums = [2, 7, 11, 15]
# target = 9
# solution = Solution()
# print(solution.twoSum(nums, target))  # Output: [0, 1]

# class MyClass:
#     def function(self):
#         x = 5
#         return x

# fuc = MyClass()
# result = fuc.function()
# print(result)

# class Listnode:
#    def __init__ (self, val= 0 , next = None):
#        self.val = val
#        self.next = next

# class Solution:
#     def addtwonum(self, l1, l2):
#         dummy = Listnode()
#         res = dummy
#         total = carry = 0 
#         while l1 or l2  or carry:
#             total = carry 
#             if l1:
#                 total += l1.val
#                 l1 = l1.next
#             if l2 :
#                 total += l2.val
#                 l2 = l2.next
#             num = total % 10
#             carry  = total // 10
#             dummy.next = Listnode(num)
#             dummy = dummy.next
#         return res.next

# def build_linked_list(arr):
#     dummy = Listnode(0)
#     cur = dummy
#     for x in arr:
#         cur.next = Listnode(x)
#         cur = cur.next
#     return dummy.next


# l1 = [4, 6, 4]
# l2 = [3, 4, 3]
# ll1 = build_linked_list(l1)
# ll2 = build_linked_list(l2)
# sol = Solution()
# result = sol.addtwonum(ll1,ll2)

# while result:
#     print(result.val, end = " -> ")
#     result = result.next
# print("None")


# class Solution:
#     def longestsubs(self, text):
#         last_seen = {}
#         start = 0
#         max_length = 0

#         for end in range(len(text)):
#             current_char = text[end]

#             if current_char in last_seen and last_seen[current_char] >= start:
#                 start = last_seen[current_char] + 1

#             last_seen[current_char] = end
#             max_length = max(max_length, end - start + 1)

#         return max_length


# text = "abcabcabc"
# sol = Solution()
# result = sol.longestsubs(text)
# print(result)


# class solution:
#     def twomed(self, num1, num2):
#         merged = num1+num2
#         merged.sort()
#         total = len(merged)
#         if total % 2 == 1:
#             return  float(merged[total // 2])
#         else:
#             middle1  = merged[total // 2 - 1]
#             middle2 = merged[total // 2]
#             return (float(middle1)+ float(middle2)) / 2.0
        
# num1 = [1,3]
# num2 = [2]
# sol = solution()
# result = sol.twomed(num1, num2)
# print(result)

# zigzag pattern
# class solution:
#     def zigzag(self, s, numrows):
#         if numrows == 1 and numrows >= len(s):
#             return s
#         rows = [""] * numrows
#         curr_rows = 0
#         direction = -1  
#         for sh in s:
#             rows[curr_rows] += sh
#             if curr_rows == 0 or curr_rows == numrows - 1:
#                 direction *= -1
#             curr_rows += direction
#         return "".join(rows)

# s = "yasinahmad"
# numrows = 3
# sol = solution()
# result = sol.zigzag(s, numrows)
# print(result)

# # sting to intiger
# class solution:
#     def strint(self, s):
#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31

#         i = 0 
#         n = len(s)
#         # skip all spaces
#         while i < n and s[i] == " ":
#             i += 1
#         #    for sing find
#             sign = 1 
#             if i < n  and s[i] == "-" or s[i] == "+":
#                 if s[i] == "-":
#                     sign = -1
#                 i += 1
#                 # for digit store
#             num = 0 
#             while i < n and s[i].isdigit():
#                 digit = ord(s[i]) - ord("0")
#                 num = num * 10 + digit
            
#                 # for overflow check
#                 if sign* num > INT_MAX:
#                    return INT_MAX
#                 if sign* num < INT_MIN:
#                    return INT_MIN
#                 i += 1
#         return sign * num
# s = "  -42"
# sol = solution()
# result = sol.strint(s)
# print(result)


# merge k sorted list
# def merge_two_lists(a, b):
#     i = 0
#     j = 0
#     result = []
   
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1

#     # Add remaining elements
#     while i < len(a):
#         result.append(a[i])
#         i += 1

#     while j < len(b):
#         result.append(b[j])
#         j += 1

#     return result

# def merge_k_lists(lists):
#     if not lists:
#         return []

#     result = lists[0]

#     for i in range(1, len(lists)):
#         result = merge_two_lists(result, lists[i])

#     return result


# a = [
#     [1,2,3],
#     [1,4,3],
#     [1,4]
# ]

# print(merge_k_lists(a))

# def fourSum(nums, target):
#     nums.sort()                # Step 1: Sort the array
#     n = len(nums)
#     result = []

#     # Fix first number (i)
#     for i in range(n - 3):

#         # Skip duplicate first numbers
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue

#         # Fix second number (j)
#         for j in range(i + 1, n - 2):

#             # Skip duplicate second numbers
#             if j > i + 1 and nums[j] == nums[j - 1]:
#                 continue

#             # Two pointers for remaining two numbers
#             left = j + 1
#             right = n - 1

#             while left < right:
#                 total = nums[i] + nums[j] + nums[left] + nums[right]

#                 if total == target:
#                     # Found one valid quadruplet
#                     result.append([nums[i], nums[j], nums[left], nums[right]])

#                     # Move both pointers
#                     left += 1
#                     right -= 1

#                     # Skip duplicate values
#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#                 elif total < target:
#                     # Sum too small → move left forward
#                     left += 1

#                 else:
#                     # Sum too big → move right backward
#                     right -= 1

#     return result

# nums = [-1,-2,2,3,1,2]
# target = 0
# print(fourSum(nums,target))


# class listnode:
#     def __init__(self, val=0, next = None):
#         self.val= 0
#         self.next = None

# class solution:
#     def exnode(self, head):
#         dummy = listnode(0)
#         dummy.next = head
#         prev = dummy
        
#         while prev.next or prev.next.next:
#             first = prev.next
#             second = first.next

#             # swap
#             prev.next = second
#             first.next = second.next
#             second.next = first

#             prev = first
#         return dummy.next

def nextpermutation(nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    k = i-1
    while nums[j] <= nums[k]:
        j -= 1
    nums[k],nums[j] = nums[j],nums[k]
    l,r = k+1,len(nums)-1    
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1
    return nums
        
s = [1,3,5,4,2]
a = nextpermutation(s)
print(a)