num=list([1,2,3,4])
target=5
ans={}

for i,num in enumerate(num):
    if target-num in  ans:
        print(ans[target-num],i)
        break
    ans[num]=i