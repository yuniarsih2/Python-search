# Pencarian data dalam list terurut
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


names = ['alice', 'bob', 'charlie', 'david', 'emma', 'farnk', 'george']

target_name = input("masukkan nama yang ingin dicari: ")
index = binary_search(names, target_name)

if index != -1:
    print("nama ditemukan pada index", index)
else:
    print("nama tidak ditemukan")

# Output tampilan nama yang dicari beserta urutan indeksnya pada elemen
