#Accessing any element in the array
# def access_arr(arr,access):
#     n=len(arr)
#     for i in range(n):
#         if arr[i]==access:
#             return f"Element found at index {i}"
#     return "Element not found at  any index."
        
    
# arr=list(map(int,input("Enter the elements you want....").split()))
# access=int(input("Take an element you want to access...:"))
# result=access_arr(arr,access)
# print(result)



# def access_1st_element(arr):
#     n=len(arr)
#     if n==0:
#         print (f"You cann't access anything")
#     else:
#         first_element=arr[0]
#         print(first_element)
    
# arr=list(map(int,input("Enter the elements you want.....").split()))
# # access=int(input("Take an "))
# result=access_1st_element(arr)


# def access_last_element(arr):
#     n=len(arr)

#     # for i in range(len(arr)):
#     if n==0:
#         return "You cann't access anything"
#     else:
#         last_element=arr[n-1]
#         print("The last elemnet is...:",last_element)
    
  


# arr=list(map(int,input("Enter the elements you want.....").split()))
# # access=int(input("Take an "))
# result=access_last_element(arr)


def access_neg_index(arr,neg_index):
    n=len(arr)

    if n==0:
        return"you can't access anything"
    real_index=n+neg_index
    if real_index<0 or real_index>=n:
        return "Index is out of range"
    return arr[real_index]
    

arr=list(map(int,input("Enter the elements...:").split()))
neg_index=int(input("Enter the negative index you wants to access...."))
result=access_neg_index(arr,neg_index)
print(result)
