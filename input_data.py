
# File: main.py

from data import InputData
from proses import Proses
from view import View

def main():
    print("=== Program Penjumlahan Dua Angka ===")

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        # Simpan data
        data = InputData(angka1, angka2)

        # Lakukan proses
        proses = Proses(data)

        # Tampilkan hasil
        tampil = View(proses)
        tampil.tampilkan_tabel()

    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

if __name__ == "__main__":
    main()
