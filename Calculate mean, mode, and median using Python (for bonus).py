#Name: Md Rahadul Islam;    Id: 231 123 038
# Problem: Write a code in Python to calculate the mean, mode, and median.

nums = sorted(map(int, input("Enter the numbers what you want to use in calculation: ").split()))
mean= sum(nums)/len(nums)
print("Here the value of mean is: ",mean)
median= (nums[len(nums)//2]+nums[(len(nums)-1)//2])/2
print("Here the value of Median is: ",median)

count = {}
max_count = 0
mode = None
for num in nums:
    count[num]= count.get(num,0)+1
    if count[num]>maximum_count:
        maximum_count=count[num]
        mode=num
    elif count[num]==maximum_count:
        mode="There are no unique mode. There are multiple numbers that are given more than once. But, if there is a number that is given more than once, it will be the mode."
print("Here the value of Mode is:",mode)

