def min_max(arr):
    if not arr:
        return None,none
    mini=min(arr)
    maxi=max(arr)
    return mini,maxi
array={1,8,3,2,7}
mini_value ,maxi_value=min_max(array)
print(mini_value)
print(maxi_value)
