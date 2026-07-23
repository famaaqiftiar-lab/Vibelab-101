# VibeLab 101

Materi interaktif tentang vibe coding untuk peserta yang belum memiliki
pengalaman coding. Aplikasi ini merupakan static website sehingga tidak
memerlukan Node.js, npm, database, atau instalasi package.

## Cara menjalankan dengan Python

### 1. Unduh project

1. Buka halaman repository ini.
2. Klik **Code**.
3. Pilih **Download ZIP**.
4. Ekstrak file ZIP ke folder pilihan.

Pastikan `index.html`, `serve.py`, dan folder `assets` tetap berada dalam folder
yang sama.

### 2. Buka terminal pada folder project

**Windows**

1. Buka folder hasil ekstrak di File Explorer.
2. Klik kolom alamat folder.
3. Ketik `powershell`, lalu tekan Enter.

**macOS atau Linux**

1. Buka Terminal.
2. Masuk ke folder hasil ekstrak menggunakan perintah `cd`.

Contoh:

```bash
cd Downloads/Vibelab-101-main
```

### 3. Jalankan aplikasi

**Windows**

```powershell
py serve.py
```

Jika perintah `py` tidak tersedia, coba:

```powershell
python serve.py
```

**macOS atau Linux**

```bash
python3 serve.py
```

Browser akan membuka alamat berikut secara otomatis:

```text
http://127.0.0.1:8000/
```

Tidak perlu menjalankan `npm install` atau proses build frontend.

### 4. Menghentikan aplikasi

Kembali ke terminal yang menjalankan server, lalu tekan:

```text
Ctrl+C
```

## Pilihan port

Jika port `8000` sedang digunakan aplikasi lain, tentukan port berbeda:

```bash
python3 serve.py --port 9000
```

Pada Windows:

```powershell
py serve.py --port 9000
```

Kemudian buka `http://127.0.0.1:9000/`.

Gunakan opsi berikut jika browser tidak perlu dibuka otomatis:

```bash
python3 serve.py --no-browser
```

## Penggunaan offline

Setelah repository selesai diunduh, aplikasi dapat dijalankan tanpa koneksi
internet. Progres materi, PRD, dan Rules disimpan pada browser yang digunakan.
Menghapus data browser dapat menghapus progres tersebut.

## Struktur file

```text
Vibelab-101/
├── assets/       # CSS dan JavaScript hasil build
├── index.html    # Halaman utama
├── serve.py      # Server lokal berbasis Python
└── README.md     # Tutorial penggunaan
```
