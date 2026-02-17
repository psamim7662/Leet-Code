def roman_to_int(s):
    d={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    total=0
    for i in range(len(s)):
        current=d[s[i]]
        if i<len(s)-1:
            next=d[s[i+1]]
            if current<next:
                total=total-current
            else:
                total=total+current
        else:
            total=total+current
    return total



c=input("Take the roman number")
print(roman_to_int(c))