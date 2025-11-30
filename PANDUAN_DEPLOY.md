# 🚀 Panduan Deploy ke Streamlit Cloud

## Langkah 1: Persiapan GitHub

### 1.1 Buat Repository Baru di GitHub

1. Buka https://github.com
2. Klik tombol **"+"** di pojok kanan atas
3. Pilih **"New repository"**
4. Beri nama repository (contoh: `dashboard-visualisasi`)
5. Pilih **Public** (untuk deployment gratis)
6. **JANGAN** centang "Add a README file"
7. Klik **"Create repository"**

### 1.2 Upload Code ke GitHub

Jalankan perintah berikut di terminal (dari folder project):

```bash
git init
git add .
git commit -m "Tugas Praktikum - Dashboard Visualisasi Data"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```

**Catatan:** Ganti `USERNAME` dengan username GitHub Anda dan `NAMA-REPO` dengan nama repository yang Anda buat.

## Langkah 2: Deploy ke Streamlit Cloud

### 2.1 Akses Streamlit Cloud

1. Buka https://share.streamlit.io
2. Klik **"Sign in"**
3. Pilih **"Continue with GitHub"**
4. Login dengan akun GitHub Anda
5. Berikan akses yang diperlukan

### 2.2 Deploy Aplikasi

1. Klik tombol **"New app"** atau **"Create app"**
2. Isi form deployment:

   - **Repository:** Pilih repository yang sudah dibuat
   - **Branch:** `main`
   - **Main file path:** `Tugas3.py`
   - **App URL (optional):** Bisa dikustom atau biarkan default

3. Klik **"Deploy!"**

### 2.3 Tunggu Proses Deployment

- Proses deployment memakan waktu 2-5 menit
- Anda akan melihat log deployment berjalan
- Tunggu sampai status berubah menjadi **"Your app is live!"**

## Langkah 3: Akses Aplikasi

Setelah deployment selesai:

- URL akan tersedia dalam format: `https://[username]-[repo-name]-[random].streamlit.app`
- Copy URL tersebut
- Share ke dosen! ✅

## Tips Deployment

### ✅ Checklist Sebelum Deploy:

- [ ] File `Tugas3.py` ada dan berjalan dengan baik
- [ ] File `requirements.txt` ada dan berisi semua dependencies
- [ ] Tidak ada error saat run lokal
- [ ] File sudah di-push ke GitHub

### 🔧 Troubleshooting

**Problem: Aplikasi error saat deploy**

- Solution: Cek requirements.txt, pastikan semua package tercantum

**Problem: Module not found**

- Solution: Tambahkan package yang kurang di requirements.txt, lalu commit & push

**Problem: App tidak mau start**

- Solution: Cek log di Streamlit Cloud, biasanya ada petunjuk error

### 📱 Update Aplikasi

Jika ingin update aplikasi setelah deploy:

```bash
git add .
git commit -m "Update aplikasi"
git push
```

Streamlit Cloud akan otomatis re-deploy!

## 🎯 Untuk Dosen

Aplikasi ini memiliki:

- ✅ 5 jenis visualisasi (Pie, Bar, Line, Map, Area)
- ✅ Dropdown untuk memilih visualisasi
- ✅ 10 data dummy menggunakan list
- ✅ Gambar header untuk setiap visualisasi
- ✅ Title dan deskripsi lengkap
- ✅ Deployed dan accessible via URL public (+10 poin!)

## 📧 Contoh Link Deployment

`https://username-dashboard-visualisasi-abc123.streamlit.app`

---

**Selamat! Aplikasi Anda sekarang sudah live dan bisa diakses dari mana saja! 🎉**
