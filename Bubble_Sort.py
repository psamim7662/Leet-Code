def Bubble_Sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
           if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
            #    i=i+1
        
    return arr
      
# arr=[1,2,3]
arr=[3,2,1]
arr=list(map(int,input("Enter the elements...:").split()))
print("The array is...:",arr)
sorted=Bubble_Sort(arr)
print("Array after Bubble Sort...",sorted)



##If array already sorted
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False

        for j in range(n-1-i):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
         break
    return arr
    

arr=list(map(int,input("Enter the elements...:").split()))
print("The array is ......:",arr)
sorted=bubble_sort(arr)
print("Array after sorting...:",arr)