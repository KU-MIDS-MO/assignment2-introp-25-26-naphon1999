def swap_ends(L, k):
    if k <= 0:
        return L.copy(), 0
    if k > len(L)//2 :
        return L.copy(), 0
    if L == []:
        return L.copy(), 0
    
    new_list = L.copy()
    for i in range(k):
        new_list[i], new_list[-k + i] = new_list[-k + i], new_list[i]
    return new_list, k
