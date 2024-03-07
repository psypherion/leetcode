def majelem(arr):
    candidate = 0;
    count = 0
    
    for i in arr:
        if count == 0:
            candidate = i
            count = 1
        elif i == candidate:
            count += 1
        else:
            count -= 1

    return candidate

if __name__ == "__main__":
    arr = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]
    print(majelem(arr))