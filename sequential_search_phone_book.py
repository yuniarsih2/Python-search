def sequential_search(nama, buku_telepon):
    for entry in buku_telepon:
        if entry['Nama'] == nama:
            return entry['No. Telepon']
    return "Nomor telepon tidak ditemukan"


# Daftar buku telepon yang tersedia
buku_telepon = [
    {'Nama': 'John Doe', 'No. Telepon': '081234567890'},
    {'Nama': 'Jane Smith', 'No. Telepon': '089876543210'},
    {'Nama': 'Michael Johnson', 'No. Telepon': '087811223344'},
    {'Nama': 'Emily Davis', 'No. Telepon': '082122232425'}
]

# Pencarian nomor telepon Jane
cari_nama = 'Jane Smith'
nomor_telepon = sequential_search(cari_nama, buku_telepon)
print("Nomor telepon", cari_nama, "adalah:", nomor_telepon)

# Output menampilkan nomer telepon jane
