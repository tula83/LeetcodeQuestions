def  minimum_cost(days,costs):
    min_cost=[1e9]
    
    compute(days,costs,0,0,min_cost)
    return min_cost



def compute(days,costs,day_index,current_cost,min_cost):

    if day_index>=len(days):
        min_cost[0]=min(min_cost[0],current_cost)
        return
    
    compute(days,costs,day_index+1,current_cost+costs[0],min_cost)

    #buy a 7-day pass

    i=day_index
    while i<len(days) and  days[i]-days[day_index]<7:
        i+=1
    compute(days,costs,i,current_cost+costs[1],min_cost)

    #buy 30 days pass

    j=day_index

    while j<len(days) and days[j]-days[day_index] < 30:
        j+=1
    compute(days,costs,j,current_cost+costs[2],min_cost)





days=[1,4,6,7,8,20]
costs = [2,7,15]
#result=minimum_cost(days,costs)
#print(f'minimum cost {result[0]}')


#another optimized approach

def  calculate_min_cost(days,costs):
    st_days=set(days)
    dp=[0]*366
    for i in range(1,366):
        if i in st_days:
            dp[i]=min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        else:
            dp[i]=dp[i-1]
    return dp[365]

print(f'maximum of  cost of tickets {calculate_min_cost(days,costs)}')