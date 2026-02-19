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



def access_1st_element(arr):
    n=len(arr)
    if n==0:
        print (f"You cann't access anything")
    else:
        first_element=arr[0]
        print(first_element)
    
  


arr=list(map(int,input("Enter the elements you want.....").split()))
# access=int(input("Take an "))
result=access_1st_element(arr)