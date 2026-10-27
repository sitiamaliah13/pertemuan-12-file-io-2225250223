def baca_data():
    data = []

    try:
        with open("data/nilai.txt", "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    continue

                nim = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Nilai tidak valid untuk {nim}.")

    except FileNotFoundError:
        print("File nilai.txt tidak ditemukan.")

    return data


def buat_rekap(data):
    if not data:
        return "Tidak ada data nilai yang valid."

    jumlah = len(data)
    rata_rata = sum(nilai for nim, nilai in data) / jumlah
    nilai_min = min(nilai for nim, nilai in data)
    nilai_max = max(nilai for nim, nilai in data)
    jumlah_lulus = sum(1 for nim, nilai in data if nilai >= 60)

    hasil = (
        f"Jumlah data: {jumlah}\n"
        f"Rata-rata: {rata_rata:.2f}\n"
        f"Nilai minimum: {nilai_min}\n"
        f"Nilai maksimum: {nilai_max}\n"
        f"Jumlah lulus (>= 60): {jumlah_lulus}\n"
    )

    return hasil


def simpan_rekap(hasil):
    with open("data/hasil_rekap.txt", "w", encoding="utf-8") as file:
        file.write(hasil)


data = baca_data()
hasil = buat_rekap(data)
print(hasil)
simpan_rekap(hasil)

print("Rekap berhasil disimpan.")