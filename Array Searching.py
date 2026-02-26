def arr_search(arr,search):
    n=len(arr)
    for i in range(n):
        if arr[i]==search:
            return f"element found at index {i}"
    return f"The value is not present in the array"
arr=list(map(int,input("Enter the elements....:").split()))
print("The array is....:",arr)
search=int(input("Enter the element you want to search....:"))
result=arr_search(arr,search)
print(result)