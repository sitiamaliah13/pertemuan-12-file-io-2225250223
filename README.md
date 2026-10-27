# Pertemuan 12 - File I/O dan Error Handling

Nama: Siti Amaliah  
NIM: 2225250223  
Kelas: 3E  

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.

## Struktur Folder

- latihan/01_tulis_file.py
- latihan/02_baca_file.py
- latihan/03_append_file.py
- latihan/04_proses_baris.py
- latihan/05_file_not_found.py
- latihan/06_value_error.py
- tugas/rekap_nilai_file.py
- data/catatan.txt
- data/nilai.txt
- data/hasil_rekap.txt

## Format File Input

Format data:

NIM,nilai

Contoh:

A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

## Cara Menjalankan

Jalankan dari root folder proyek:

python tugas/rekap_nilai_file.py

## Error yang Ditangani

- FileNotFoundError
- ValueError

## Test Case

| Kondisi | Hasil |
|---|---|
| Semua data valid | Semua data diproses |
| File tidak ditemukan | Program menampilkan pesan dan tidak crash |
| Nilai invalid | Baris invalid dilewati |
| Baris kosong | Baris kosong dilewati |
| Nilai 60 | Dihitung sebagai lulus |

## Hasil Pengujian

Jumlah data valid: 5  
Rata-rata: 83.40  
Minimum: 74.00  
Maksimum: 92.00  
Jumlah lulus: 5  

## Refleksi

Error yang ditemukan adalah ValueError ketika nilai A004 berisi teks "abc". Program menangani error tersebut dengan try-except sehingga baris yang tidak valid dilewati dan data lainnya tetap dapat diproses.

FileNotFoundError juga ditangani agar program tidak berhenti secara kasar ketika file input tidak ditemukan.

## Bantuan

Pengerjaan berdasarkan bahan ajar Pertemuan 12 dan dokumentasi konsep Python File I/O serta error handling.