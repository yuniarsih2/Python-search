# Temukan rotasi terkecil dalam sebuah list yang sudah dirotasikan

def binary_search_rotation(data):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid

    return low


my_lis = [6, 7, 8, 9, 1, 2, 3, 4, 5]
rotataion_index = binary_search_rotation(my_lis)
print(f"Indeks rotasi terkecil adalah {rotataion_index}")

# Indeks rotasi terkecil adalah 4
