# Membuat fungsi menggunakan binary search
def binary_search_insertion_point(data, target):
    left = 0
    right = len(data) - 1
    insertion_point = len(data)

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            # Elemen sudah ada dalam daftar
            return mid

        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            insertion_point = mid

    # Elemen tidak ada dalam daftar
    return insertion_point


# Data yang sudah diurutkan
data = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Mencari posisi sisipan elemen
insertion_index = binary_search_insertion_point(data, target)

print("Elemen", target, "dapat disisipkan pada indeks", insertion_index,
      "untuk menjaga daftar tetap terurut.")

# Output Elemen 7 dapat disisipkan pada indeks 3 untuk menjaga daftar tetap terurut
