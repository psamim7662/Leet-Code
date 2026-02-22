### Inserting at the first index
# def insert_array(arr,ele):
#     n=len(arr)
#     if n==0:
#         return "No possibility of insertion"
#     arr.append(0)
#     for i in range(n,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=ele
#     return arr
    

# arr=list(map(int,input("Enter the array elements.....:").split()))
# print("The array is....",arr)
# ele=int(input("Enter the elememnt you want to insert..:"))
# result=insert_array(arr,ele)
# print("The array after the insertion...:",arr)

### Inserting at the end of the array
# def insert_arr(arr,ele):
#     n=len(arr)
#     if n==0:
#         return "Not possible to insert"
#     arr.append(0)
#     for i in range(n,-1):
#         arr[i]=arr[i-1]
#     arr[n]=ele
#     return arr

# arr=list(map(int,input("Enter the elements you want to take as input....:").split()))
# ele=int(input("Enter the elemnet you want to insert...:"))
# result=insert_arr(arr,ele)
# print("The final array after the insertion...:",arr)

### Inserting at any specific position of the array
def insert_arr(arr,ele,index):
    n=len(arr)
    # pos=index
    if pos<0 or pos>n:
        return "Insertion not possible"
    arr.append(0)
    for  i in range(n,pos,-1):
        arr[i]=arr[i-1]
    arr[pos]=ele
    return arr
arr=list(map(int,input("Enter the elements..: ").split()))
ele=int(input("The element we want to insert..:"))
pos=int(input("Enter the index position:"))
resul=insert_arr(arr,ele,pos)
print("The final array after the insertion...:",arr)
     


