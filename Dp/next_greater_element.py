def  next_greater_element(arr):
    s=[]
    n=len(arr)

    for i in range(n):
        while s and s[-1].get("value") < arr[i]:
            d=s.pop()
            arr[d.get("index")]=arr[i]
        s.append({'value':arr[i],'index':i})
    while s:
        d=s.pop()
        arr[d.get("index")]=-1
    return arr

print(next_greater_element([4,1,2]))

