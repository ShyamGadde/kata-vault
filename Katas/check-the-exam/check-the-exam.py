def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if not arr2[i]:
            continue
        if arr1[i] == arr2[i]:
            score += 4
        else:
            score -=1
    
    return score if score > 0 else 0