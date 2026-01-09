
# File: proses.py


class Proses:
    """Class untuk melakukan perhitungan"""
    def __init__(self, data):
        self.data = data

    def hitung_jumlah(self):
        """Mengembalikan hasil penjumlahan dua angka"""
        return self.data.angka1 + self.data.angka2
