# Temukan apakah suatu elemen ada dalam list

def sequential_seacrh(data, key):
    for item in data:
        if item == key:
            return True
    return False


my_list = [3, 6, 2, 9, 4, 7]
key = 6
found = sequential_seacrh(my_list, key)
if found:
    print("Elemen ditemukan.")
else:
    pring("Elemen tidak ditemukan.")

# Output Element ditemukan. elemen yang di temukan adalah 6
