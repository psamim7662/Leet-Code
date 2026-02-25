###Update an element from the specific position
def arr_update(arr,index,new_value):
    n=len(arr)
    if index<0 or index>=n:
        return "Insertion not possible"
    arr[index]=new_value
    return arr

arr=list(map(int,input("Enter the elements.....:").split()))
index=int(input("Enter the index you want to update...:"))
new_value=int(input("Enter the value you want to replace...:"))
result=arr_update(arr,index,new_value)
print("The array after the update......",arr)