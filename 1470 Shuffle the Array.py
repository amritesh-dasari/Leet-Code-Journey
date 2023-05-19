def shuffle(nums, n):
    lst1=nums[:n]
    lst2=nums[n:]
    for i in range(1,n+1):
        lst1.insert(2*i-1,lst2[i-1])
    return lst1