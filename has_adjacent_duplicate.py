def has_adjacent_duplicate(L):
    for i in range(len(L) - 1):
        if L[i] == L[i + 1]:
            return True
    return False
