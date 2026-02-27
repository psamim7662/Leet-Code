def parenthesisation(S):
    open_bracket=['(','{','[']
    close_bracket=[')','}',']']
    d=dict(zip(close_bracket,open_bracket))
    if (S[0] in close_bracket or S[-1] in open_bracket):
        return False
    ind=0
    result=[]
    while(ind<len(S)):
        if(S[ind] in open_bracket):
            result.append(S[ind])
        else:
            need=d[S[ind]]
            if(len(result)>0 and result[-1]==need):
                result.pop()
            else:
                return False
        ind=ind+1
    if(len(result)==0):
        return True
    else:
        return False


S=[{}]
res=parenthesisation(S)
print(res)
