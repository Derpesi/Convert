# Senaqo Vector App
Aplikasi pembuat vektor otomatis dari teks menggunakan Google Gemini API dan Vtracer.

## Persiapan & Instalasi
1. Pastikan Anda sudah menginstal Python (minimal versi 3.9) di komputer/server Anda.
2. Buka Terminal atau Command Prompt di dalam folder ini.
3. Instal semua library yang dibutuhkan dengan menjalankan perintah:
   `pip install -r requirements.txt`

## Cara Menjalankan
1. Buka file `main.py` menggunakan teks editor (Notepad/VS Code).
2. Cari tulisan `MASUKKAN_API_KEY_ANDA_DISINI` dan ganti dengan API Key Gemini Anda.
3. Jalankan server dengan perintah:
   `python main.py`
4. Buka browser (Chrome/Safari) dan akses alamat:
   `http://localhost:8000`

## Catatan Penggunaan
- Aplikasi ini akan menghasilkan file berekstensi `.svg` dengan node/path yang halus (mode spline).
- File SVG ini sudah kompatibel untuk langsung ditarik ke software desain atau aplikasi *digitizing* bordir.
