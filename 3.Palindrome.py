# Given an integer x ,return true if x is palindrome integer.

# def palindrome(x):
#     # x=abs(x)
#     # sign=-1 if x<0 else 1
#     x=str(x)
#     rev=str(x)[::-1]
#     if x==rev:
#         return True
#     else:
#         return False
# x=input("Take the string you want to check:")
# print(palindrome(x))

def palindrome(x):
    if (x<0 or (x%10==0 and x!=0)):
        return False
    rev=0
    while(x>rev):
        digit=x%10
        rev=rev*10+digit
        x=x//10
    if(x==rev or x%10==rev):
            return True
    else:
            return False
          

x=int(input("Take an integer value you want to check palindrome or not:"))
print(palindrome(x))