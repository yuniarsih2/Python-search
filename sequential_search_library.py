# Mencari buku di perpustakaan

def is_similar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()

    if title1[0] == title2[0]:
        return True

    return False


def sequential_seacrh(books, book_title):
    for book in books:
        if is_similar(book['title'], book_title):
            return book['shelf']

    return "Buku tidak ditemukan"


books = [
    {'title': 'Python Programming', 'shelf': 'A1'},
    {'title': 'Data Structures and Algorithms', 'shelf': 'B2'},
    {'title': 'Introduction to Machine Learning', 'shelf': 'C3'},
    {'title': 'Database Management Systems', 'shelf': 'D4'}
]

book_title = input("Masukan judul buku yang ingin di cari: ")
shelf_location = sequential_seacrh(books, book_title)
print(shelf_location)

# Output menampilkan buku yang di cari
