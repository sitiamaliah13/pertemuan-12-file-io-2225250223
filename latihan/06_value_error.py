teks = input("Masukkan nilai: ")

try:
    nilai = float(teks)
    print("Nilai berhasil dibaca:", nilai)
except ValueError:
    print("Input harus berupa angka.")