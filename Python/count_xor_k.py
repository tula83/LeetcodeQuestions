def count_xor_k(arr,k):
    xor_count={0:1}
    xor_value=0
    count=0

    for item in arr:
        xor_value^=item
        if xor_value^k in xor_count:
            count+=xor_count[xor_value^k]
        xor_count[xor_value]=xor_count.get(xor_value,0)+1
    return count


print(count_xor_k([4, 2, 2, 6, 4],6))