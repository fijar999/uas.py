
# File: view.py


class View:
    """Class untuk menangani input dan output"""

    def __init__(self, proses):
        self.proses = proses

    def tampilkan_tabel(self):
        """Menampilkan hasil dalam format tabel sederhana"""
        hasil = self.proses.hitung_jumlah()
        print("\n======= HASIL PERHITUNGAN =======")
        print(f"{'Angka 1':<10}: {self.proses.data.angka1}")
        print(f"{'Angka 2':<10}: {self.proses.data.angka2}")
        print(f"{'Hasil':<10}: {hasil}")
        print("=================================")
