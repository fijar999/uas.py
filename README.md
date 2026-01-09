# 🧮 Program Kalkulator Sederhana (OOP & Modular)

## 📘 Deskripsi Program
Program ini merupakan **kalkulator sederhana** yang dibuat menggunakan konsep **Object Oriented Programming (OOP)** dan **modular programming**.  
Program meminta pengguna untuk memasukkan dua angka, lalu menghitung hasil penjumlahannya, dan menampilkan hasil dalam format tabel sederhana.  

Program ini juga dilengkapi dengan **validasi input** menggunakan konsep **exception handling (try-except)** untuk mencegah kesalahan saat pengguna memasukkan data yang tidak sesuai.

---

## 🧱 Struktur Program
Program dibagi menjadi beberapa modul agar lebih terstruktur dan mudah dikelola:

| File | Fungsi | Deskripsi |
|------|---------|-----------|
| `data.py` | Class `InputData` | Menyimpan data input pengguna (dua angka) |
| `proses.py` | Class `Proses` | Melakukan proses perhitungan (penjumlahan) |
| `view.py` | Class `View` | Menampilkan hasil perhitungan dalam bentuk tabel |
| `main.py` | Fungsi utama | Mengatur alur program dari input, proses, hingga output |

---

## ⚙️ Alur Program
1. Program menampilkan judul kalkulator.  
2. Pengguna memasukkan dua angka.  
3. Data disimpan di class `InputData`.  
4. Data diproses oleh class `Proses` untuk menghitung hasilnya.  
5. Hasil dikirim ke class `View` untuk ditampilkan.  
6. Jika input bukan angka, program menampilkan pesan error.

**Alur sederhana:**
