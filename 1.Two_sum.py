# Given an array of integers nums and an integer target,return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,and you may not use the same element twice.
# def two_sums(nums,tar):
#     n=len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#            if nums[i]+nums[j]==tar:
#              return[i,j]
#     return[]
    
# nums=list(map(int,input("Enter the integers you want to take as an input:").split()))
# tar=int(input("Take a number you want to sum:"))
# result=two_sums(nums,tar)
# print("The reult is :",result)






# def two_sums1(nums,tar):
#    n=len(nums)
#    for i in range(n-1):
#       for j in range(n-1,i,-1):
#          if nums[i]+nums[j]==tar:
#             return[i,j]
#    return[]
         

# nums=list(map(int,input("Take the input array fron the user:").split()))
# tar=int(input("Enter the target value"))
# result=two_sums1(nums,tar)
# print("The sum is:",result)



def two_sums2(nums,tar):
    n=len(nums)
    d={}
    for i in  range(n):
        complement=tar-nums[i]
        if complement in d:
            return[d[complement],i]
        d[nums[i]]=i
        # return[i,complement]
    return[]

nums=list(map(int,input("Take the input array from the user:").split()))
tar=int(input("Enter the target value:"))
result=two_sums2(nums,tar)
print(result)