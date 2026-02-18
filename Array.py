#Array Implementation
# def array(arr):
#     print("The array is :",arr)


# arr=list(map(int,input("Take the elements as you wish...:").split()))

# array(arr)





#Traverse the array
def array(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")

arr=list(map(int,input("Take the elemnts as your wish...:").split()))
array(arr)
