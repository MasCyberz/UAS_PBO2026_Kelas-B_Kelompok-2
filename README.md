# Sistem Manajemen Hanari Bakery - Penerapan OOP dan SOLID

Repository ini berisi program CLI sederhana untuk mengelola produk bakery, resep, stok bahan, proses produksi, dan laporan keuntungan. Program dibuat menggunakan Python dengan pendekatan Object Oriented Programming.

## Deskripsi Proyek

Sistem ini digunakan untuk membantu pencatatan operasional Hanari Bakery. Data awal yang tersedia meliputi bahan baku, resep, dan beberapa produk bakery.

Produk awal:

- Roti Manis
- Croissant
- Butter Cookies
- Muffin

Fitur utama:

- Menampilkan daftar produk
- Menambahkan produk baru
- Mengupdate produk
- Menghapus produk
- Menampilkan daftar bahan
- Menjalankan proses produksi berdasarkan batch
- Mengurangi stok bahan setelah produksi
- Menghitung biaya produksi, omzet, dan laba

---

## Tujuan Pengembangan

Pada proyek ini kami menerapkan prinsip SOLID agar kode:

* Lebih terstruktur
* Mudah dikembangkan
* Mudah dipelihara
* Memiliki tanggung jawab yang jelas pada setiap class
* Mengurangi ketergantungan antar komponen

---

## Struktur Project

```text
hanari_bakery
│
│
├── models
│   ├── bahan.py
│   ├── resep.py
│   ├── bakery_product.py
│   ├── roti_manis.py
│   ├── croissant.py
│   ├── butter_cookie.py (toping)
│   └── muffin.py (toping)
│
├── interfaces
│   ├── pengadonan.py
│   ├── pengembangan.py
│   ├── pemanggangan.py
│   └── toping.py
│
├── services
│   └── bakery_service.py
│
├── data
│   ├── data_bahan.py
│   └── data_produk.py
│		
├── views
│   ├── tambah_product_view.py
│   ├── product_view.py
│   ├── menu_view.py
│   ├── production_view.py
│   └── profit_view.py
├── main.py
```

---

# Pembagian Tugas Kelompok

| Nama Anggota | Tugas |
|---|---|
| Gayuh | Mengerjakan bagian Models dan interface pengadonan |
| Rindy | Mengerjakan bagian Models |
| Keisha | Mengerjakan Views |
| Bintang | Mengerjakan Models dan Main Program |
| Amelia | Mengerjakan Interfaces |
| Dimas | Mengerjakan bagian services dan data, Integrasi Program, dan Perbaikan Kode |

---

# Tutorial Menggunakan GitHub Desktop

## 01. Download dan Install GitHub Desktop
- Download GitHub Desktop melalui website resmi GitHub.
- Install aplikasi seperti biasa sampai selesai.

Link:
[https://desktop.github.com/](https://desktop.github.com/download/)

---

## 02. Login Akun GitHub
- Buka GitHub Desktop.
- Klik **Sign in to GitHub.com**.
- Login menggunakan akun GitHub masing-masing.

---

## 03. Clone Repository GitHub
- Pilih menu **File → Clone Repository**.
- Pilih repository kelompok yang sudah dibuat.
- Tentukan lokasi penyimpanan project di komputer.
- Klik **Clone**.

---

## 04. Sinkronisasi Perubahan Teman
- Sebelum mulai mengerjakan, klik **Fetch Origin** atau **Pull Origin** (jika ada pembaruan). Biasanya ini dibagian menu atas atau di kanan tengah atas yang berbentuk tombol
- Tujuannya agar file project selalu update dan tidak bentrok dengan perubahan anggota lain.

---

## 05. Membuka Folder Project
- Setelah repository berhasil di-clone, klik **Show in VSCode** (atau Show in Explorer jika ingin membuka foldernya manual).

---

## 06. Membuat Branch Baru (Bukan Branch Utama)
Sebelum mulai coding, pastikan kamu tidak bekerja langsung di branch main.
- Di GitHub Desktop, klik menu Current Branch di bagian atas.
- Klik tombol New Branch.
- Beri nama branch sesuai dengan fitur atau tugas yang sedang kamu kerjakan (contoh: analisis-srp atau perbaikan-bug-srp).
- Klik Create Branch.

---

## 07. Membuat atau Mengedit File
- Sekarang kamu sudah berada di branch barumu. Buka VS Code dan kerjakan bagianmu masing-masing.

---

## 08. Commit Perubahan
- Setelah selesai coding dan menyimpan file:
  - Buka GitHub Desktop
  - Isi kolom **Summary**, bagian kiri bawah
  - Contoh:
    ```bash
    Menambahkan analisis SRP - Ken Gayuh
    ```
- Klik tombol Commit to **[nama-branch-kamu]**.

---

## 09. Push ke GitHub
- Setelah commit berhasil, klik tombol **Publish branch** (atau Push origin), biasanya ini ada di menu atas atau di tampilan utama github desktop
- Tujuannya agar perubahan tersimpan di repository GitHub online.

---

## 10. Membuat Pull Request (PR)
Setelah sukses melakukan push, saatnya menggabungkan code kamu ke branch utama melalui review kelompok.
- Di GitHub Desktop, akan muncul tombol biru bertuliskan Create Pull Request. Klik tombol tersebut.
- Kamu akan otomatis diarahkan ke browser (halaman web GitHub).
- Periksa kembali perubahanmu, isi deskripsi PR jika diperlukan, lalu klik tombol Create pull request di halaman web tersebut.
- Selesai! Anggota kelompok lain atau ketua proyek sekarang bisa memeriksa dan melakukan merge code kamu ke branch **main**.

---

## 11. Sinkronisasi Perubahan Kembali
- Setelah mengerjakan, klik **Fetch Origin** atau **Pull Origin** lagi.
- Tujuannya agar file project selalu update dan tidak bentrok dengan perubahan anggota lain.

---

# Teknologi yang Digunakan

* Python 3
* GitHub
* GitHub Desktop
* Visual Studio Code
* Object Oriented Programming (OOP)

---

# Kesimpulan

Melalui proyek Sistem Manajemen Koleksi Perpustakaan ini, kami mempelajari penerapan prinsip-prinsip SOLID dalam pengembangan perangkat lunak berorientasi objek.

Dengan memisahkan tanggung jawab ke dalam Model, Repository, Service, dan View, kode menjadi lebih modular, mudah dipelihara, serta lebih siap untuk dikembangkan di masa mendatang.

---

## Author

Kelompok 2 
Mata Kuliah Pemrograman Berorientasi Object  
Universitas Sebelas Maret
