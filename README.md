# Sistem Manajemen Hanari Bakery
### Proyek Akhir Praktikum Pemrograman Berorientasi Objek (PBO)

Repository ini berisi program CLI sederhana untuk mengelola produk bakery, resep, stok bahan, proses produksi, dan laporan keuntungan. Program dibuat menggunakan Python dengan pendekatan Object Oriented Programming.

## Deskripsi Proyek

**Sistem Hanari Bakery** merupakan aplikasi berbasis Python yang dikembangkan untuk membantu pengelolaan proses produksi pada sebuah bakery. Sistem ini menyediakan fitur pengelolaan bahan baku, resep, produk, proses produksi, serta perhitungan estimasi profit dari setiap produk yang dihasilkan.

Aplikasi mendukung beberapa jenis produk bakery, seperti:

- Roti Manis
- Croissant
- Muffin
- Butter Cookies

Fitur utama:

- Menampilkan daftar produk
- Menambahkan produk baru
- Mengupdate produk
- Menghapus produk
- Menampilkan daftar bahan
- Menjalankan proses produksi berdasarkan batch
- Mengurangi stok bahan setelah produksi
- Menghitung biaya produksi, omzet, dan laba

Proyek ini dikembangkan dengan menerapkan konsep **Object-Oriented Programming (OOP)** serta prinsip **SOLID**, sehingga struktur program menjadi lebih modular, mudah dipelihara, dan mudah dikembangkan apabila di kemudian hari terdapat penambahan fitur maupun jenis produk baru.

Aplikasi ini dibuat sebagai **Proyek Akhir Praktikum Pemrograman Berorientasi Objek (PBO)** Universitas Sebelas Maret (UNS) dan dikerjakan secara berkelompok.

---

## Tujuan Pengembangan

Pada proyek ini kami menerapkan prinsip SOLID agar kode:

* Lebih terstruktur
* Mudah dikembangkan
* Mudah dipelihara
* Memiliki tanggung jawab yang jelas pada setiap class
* Mengurangi ketergantungan antar komponen

---

## Struktur Folder & File

```text
hanari_bakery
│
├── main.py                     # Entry point program
│
├── data
│   ├── data_bahan.py           # Data awal bahan baku
│   ├── data_produk.py          # Data awal produk
│   └── data_resep.py           # Data awal resep
│
├── interfaces
│   ├── pengadonan.py           # Interface proses pengadonan
│   ├── pemanggangan.py         # Interface proses pemanggangan
│   ├── pengembangan.py         # Interface proses pengembangan
│   └── toping.py               # Interface proses pemberian topping
│
├── models
│   ├── bahan.py                # Class Bahan
│   ├── bakery_product.py       # Abstract class produk bakery
│   ├── resep.py                # Class Resep
│   ├── detail_resep.py         # Detail bahan dalam resep
│   ├── muffin.py               # Subclass BakeryProduct
│   ├── roti_manis.py           # Subclass BakeryProduct
│   ├── croissant.py            # Subclass BakeryProduct
│   ├── butter_cookies.py       # Subclass BakeryProduct
│   └── kue_kering.py           # Subclass BakeryProduct
│
├── services
│   ├── bahan_service.py        # Logika pengelolaan bahan
│   ├── resep_service.py        # Logika pengelolaan resep
│   ├── produk_service.py       # Logika pengelolaan produk
│   ├── proses_produksi_service.py # Simulasi proses produksi
│   ├── profit_service.py       # Perhitungan estimasi profit
│   └── bakery_service.py       # Penghubung seluruh service
│
├── views
│   ├── menu_view.py            # Menu utama
│   ├── input_view.py           # Input pengguna
│   ├── bahan_view.py           # Tampilan bahan
│   ├── resep_view.py           # Tampilan resep
│   ├── produk_view.py          # Tampilan produk
│   ├── production_view.py      # Tampilan proses produksi
│   └── profit_view.py          # Tampilan profit
│
├── README.md
└── .gitignore
```

---

# Pembagian Tugas Kelompok

| Nama Anggota | Username | Tugas |
|---|---|---|
| Ken Gayuh Nusa Islami | kengayuh5-arch | Mengerjakan bagian Models dan interface pengadonan |
| Arindya Aulia Wardah | arindyawardah-create | Mengerjakan bagian Models |
| Sekar Hanny Keisha Azahra | keskesiaw | Mengerjakan Views |
| Bintang Fajar Khoiru Rizal | BitangFajar-blip | Mengerjakan Models dan Main Program |
| Amelia Pinasti Nugraheni | ameliapinasti38-prog | Mengerjakan Interfaces |
| Dimas Alif Ardiansyah | MasCyberz | Mengerjakan bagian services dan data, Integrasi Program, dan Perbaikan Kode |

---

# Konsep OOP yang Diterapkan

## 1. Class & Object

Sistem dibangun menggunakan beberapa class yang memiliki tanggung jawab masing-masing.

Contohnya:

| Class | Fungsi |
|--------|--------|
| Bahan | Menyimpan informasi bahan baku |
| Resep | Menyimpan kumpulan bahan untuk suatu produk |
| BakeryProduct | Abstract class seluruh produk bakery |
| RotiManis | Produk roti manis |
| Croissant | Produk croissant |
| ButterCookies | Produk butter cookies |
| Muffin | Produk muffin |
| BahanService | Mengelola data bahan |
| ProdukService | Mengelola data produk |
| ProfitService | Menghitung estimasi keuntungan |

Setiap objek dibuat dari class tersebut ketika program dijalankan.

---

## 2. Inheritance

Inheritance digunakan agar seluruh produk bakery memiliki karakteristik dasar yang sama.

```text
                 BakeryProduct
                      ▲
        ┌─────────────┼──────────────┐
        │             │              │
   RotiManis     Croissant      KueKering
                                      ▲
                                      │
                    ButterCookies & Muffin 

                      
```


Seluruh subclass mewarisi atribut dan method dari `BakeryProduct`.

---

## 3. Polymorphism

Polymorphism diterapkan melalui method yang dioverride oleh masing-masing subclass.

---

## 4. Encapsulation

Semua data penting disimpan sebagai atribut private.

Data hanya dapat diakses melalui getter dan setter sehingga lebih aman.

```python
get_stok()
set_stok()
```

Dengan demikian perubahan data dapat dikontrol.

---

## 5. Abstraction

Abstraction diterapkan menggunakan:

### Abstract Class

```text
BakeryProduct
```

Class ini menjadi dasar seluruh produk bakery.

Selain itu digunakan juga beberapa interface:

- Pengadonan
- Pemanggangan
- Pengembangan
- Toping

Interface mendefinisikan proses produksi tanpa mengetahui implementasinya.

---

# Penerapan Prinsip SOLID

## S — Single Responsibility Principle

Setiap class hanya memiliki satu tanggung jawab.

Contoh:

- `BahanService` hanya mengelola bahan.
- `ProdukService` hanya mengelola produk.
- `ProfitService` hanya menghitung keuntungan.
- `ResepService` hanya mengelola resep.

Hal ini membuat kode lebih mudah dipahami.

---

## O — Open Closed Principle

Sistem dapat dikembangkan tanpa mengubah kode lama.

Misalnya ingin menambahkan produk baru:

```text
Donat
Bagel
Sourdough
```

Cukup membuat subclass baru dari `BakeryProduct` tanpa mengubah class yang sudah ada.

---

## L — Liskov Substitution Principle

Semua subclass dapat digunakan menggantikan `BakeryProduct`.

Contoh:

```python
produk = Croissant()

proses(produk)
```

Method tetap berjalan meskipun objek yang diberikan berbeda.

---

## I — Interface Segregation Principle

Interface dipisahkan berdasarkan fungsi.

Contohnya:

```text
Pengadonan
Pemanggangan
Pengembangan
Toping
```

Tidak semua produk harus mengimplementasikan seluruh proses.

Sebagai contoh:

- Croissant menggunakan Pengembangan.
- Butter Cookies tidak memerlukan Pengembangan.

---

## D — Dependency Inversion Principle

Service tidak bergantung langsung pada implementasi tertentu.

Contoh:

`ProsesProduksiService`

tidak bergantung pada jenis produk tertentu, tetapi hanya pada abstraksi `BakeryProduct`.

Dengan demikian sistem menjadi lebih fleksibel.

---

# Cara Menggunakan GitHub Desktop

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

# Cara Menjalankan Program

## Menjalankan Program

Masuk ke folder proyek:

```bash
cd hanari_bakery
```

Kemudian jalankan:

```bash
python main.py
```

atau

```bash
py main.py
```

Program akan menampilkan menu utama yang dapat digunakan untuk mengelola seluruh fitur bakery.

---

# Teknologi yang Digunakan

* Python 3
* GitHub
* GitHub Desktop
* Visual Studio Code
* Object Oriented Programming (OOP)

---

# Kesimpulan

Melalui proyek **Sistem Hanari Bakery**, kelompok kami berhasil mengembangkan sebuah aplikasi berbasis Python yang menerapkan konsep **Object-Oriented Programming (OOP)** serta prinsip **SOLID** dalam pengelolaan proses produksi bakery.

Penerapan konsep OOP seperti **Class & Object, Inheritance, Polymorphism, Encapsulation,** dan **Abstraction** membantu dalam membangun struktur program yang lebih terorganisir. Sementara itu, penerapan prinsip **SOLID** membuat setiap komponen memiliki tanggung jawab yang jelas, mudah dipelihara, serta lebih fleksibel ketika dilakukan pengembangan di masa mendatang.

Selama proses pengerjaan proyek, anggota kelompok memperoleh pengalaman dalam merancang struktur class, membangun hubungan antarobjek, menerapkan interface dan abstract class, serta membagi tanggung jawab program ke dalam beberapa service dan view. Pendekatan tersebut membuat proses pengembangan menjadi lebih sistematis dan memudahkan kolaborasi antaranggota kelompok.

Secara keseluruhan, proyek ini tidak hanya memenuhi tujuan pembelajaran mata kuliah Praktikum Pemrograman Berorientasi Objek, tetapi juga memberikan pengalaman dalam mengembangkan perangkat lunak secara kolaboratif dengan menerapkan praktik desain perangkat lunak yang baik.

---

## Author

Kelompok 2 
Mata Kuliah Pemrograman Berorientasi Objek  
Universitas Sebelas Maret
