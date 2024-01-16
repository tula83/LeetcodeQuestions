def nth_sqrt(n,root):
    epsilion=1e-8
    low,high=0.0,max(1.0,n)

    while high-low > epsilion:

        mid=(low+high)/2
        mid_power=mid**root

        if abs(mid_power - n) < epsilion:
            return mid
        
        elif mid_power < n:
            low=mid

        
        else:
            high=mid
    return (low + high)/2



print(nth_sqrt(36,2))
