def max_consecutive_ones(arr):
    n=len(arr)
    current_ones,till=0,-9999

    for i in range(n):
        if arr[i]==1:
            current_ones+=1
            till=max(till,current_ones)
        else:
            current_ones=0
    if till==-9999:
        return ' not found please check input!!! '
    return till

print(f'maximum consecutive ones {max_consecutive_ones([1,0,2,1,1,1])}')
