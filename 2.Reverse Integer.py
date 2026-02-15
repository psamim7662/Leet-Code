# # Given a Signed 32-bit integer x,return x with its digits reversed.If reversing x causes the 
# # value to go outside the signed 32-bit integer range(-2^31 to 2^31),then return 0.
def revs_int(x):
    if x>=0:
        val=int(str(x)[::-1])
    else:
        val=-int(str(abs(x))[::-1])
    if val<-2**31 or val>2**31-1:
        return 0
    else:
        return val

x=int(input("Take an signed bit integr number:"))
# val=("The  reverse integer is:")
result=revs_int(x)
print(result)


def revs_int(x):
    min=-2**31
    max=2**31
    rev=0
    sign=-1 if x<0 else 1
    x=abs(x)

    while x!=0:
        pop=x%10
        x=x//10

        if rev>(max-pop)//10:
            return 0
        rev=rev*10+pop
    return rev*sign

x=int(input("Take an signed bit integer number:"))
print("The reverse integer is:",revs_int(x))