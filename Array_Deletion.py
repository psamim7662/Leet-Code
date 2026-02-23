##Deletion of first element from the array
# def arr_deletion(arr):
#     n=len(arr)
#     if n==0:
#         return "No possibility of Insertion"
#     for i in range(0,n-1):
#         arr[i]=arr[i+1]
#     arr.pop()
#     return arr

# arr=list(map(int,input("Enter the array Elements...:").split()))
# print("The array is..:",arr)
# # ele=int(input("Enter the element you want to delete...:"))
# result=arr_deletion(arr)
# print("The final array after the deletion...:",result)

##Deletion of last element from the Array
# def arr_deletion(arr):
#     n=len(arr)
#     if n==0:
#         return "No possibility of Deletion"
#     for i in range(n,-1):
#         arr[i]=arr[i+1]
#     arr.pop()
#     return arr

# arr=list(map(int,input("Enter the array Elements...:").split()))
# print("The array is..:",arr)
# # ele=int(input("Enter the element you want to delete...:"))
# result=arr_deletion(arr)
# print("The final array after the deletion...:",result)


###Deletion at any specific position of the array
# def arr_deletion(arr,index):
#     n=len(arr)
#     # pos=index
#     if index<0 or index>=n:
#         return "Deletion not possible"
#     for  i in range(index,n-1):
#         arr[i]=arr[i+1]
#     arr.pop()
#     return arr
# arr=list(map(int,input("Enter the elements..: ").split()))
# # ele=int(input("The element we want to insert..:"))
# pos=int(input("Enter the index position:"))
# result=arr_deletion(arr,pos)
# print("The final array after the deletion...:",result)



###Delete an element from the specific position
def arr_deletion(arr,key):
    n=len(arr)
    found=False
    for i in range(n):
        if arr[i]==key:
            index=i
            break
    if index==-1:
        return "Element not found"
    for i in range(index,n-1):
        arr[i]=arr[i+1]
    arr.pop()
    return arr

        


arr=list(map(int,input("Enter the elements.....:").split()))
key=int(input("Enter the vslue you want to delete...:"))
result=arr_deletion(arr,key)
print("The array after the deletion......",arr)
