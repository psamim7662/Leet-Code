def longest_common_prefix(arr):
    if not arr:
        return ""
    prefix=arr[0]
    for i in range(len(prefix)):
        for string in arr:
            if string[i]!=prefix[i] or i>=len(string):
                return prefix[:i]
    return prefix
    

    


arr=input("Enter strings...:").split()
print("Longest common prefix is:",longest_common_prefix(arr))