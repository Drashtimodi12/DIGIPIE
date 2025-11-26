# List Tasks

# Add an element at end
nums = [3, 1, 5, 2, 4]
nums.append([1, 4])
print(nums)

print("------------------------")

# Insert element at index 2
nums[2] = 6
print(nums)

print("------------------------")

# Remove element by value
nums.remove(3)
print(nums)

print("------------------------")

# Sort list
nums1 = [3, 1, 5, 2, 4]
nums1.sort()
print(nums1)

print("------------------------")

# Reverse list
nums1.sort(reverse=True)
print(nums1)

print("------------------------")

# Check if two lists have same elements — order doesn’t matter

a = [1,2,3]
b = [3,1,2]


if sorted(a) == sorted(b):
    print("Same")
else:
    print("Different")