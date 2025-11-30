# 📊 Dokumentasi Tugas Praktikum

## Dashboard Visualisasi Data dengan Streamlit

---

## 🎯 Kriteria Tugas yang Terpenuhi

### ✅ Requirement Wajib:

1. **Menggunakan Streamlit** ✓
2. **Dropdown dengan 3-5 pilihan** ✓ (Ada 5 pilihan)
3. **Data dummy 10 items menggunakan list** ✓
4. **Berbagai jenis chart:**
   - Pie Chart ✓
   - Bar Chart ✓
   - Line Chart ✓
   - Map Visualization ✓
   - Area Chart ✓

### ⭐ Poin Bonus:

5. **Gambar header** ✓ (Setiap visualisasi punya gambar header)
6. **Title** ✓ (Setiap chart punya title yang jelas)
7. **Deskripsi/Penjelasan** ✓ (Setiap visualisasi ada penjelasan lengkap)
8. **Deploy (+10 poin)** ✓ (Siap di-deploy ke Streamlit Cloud)

---

## 📋 Fitur Aplikasi

### 1. Line Chart - Tren Penjualan Bulanan

- **Fungsi:** Menampilkan tren penjualan dari bulan ke bulan
- **Data:** 10 data bulan dengan jumlah penjualan
- **Fitur:** Markers interaktif, hover information
- **Statistik:** Total penjualan, rata-rata, dan penjualan tertinggi

### 2. Bar Chart - Perbandingan Penjualan Produk

- **Fungsi:** Membandingkan penjualan antar produk
- **Data:** 10 produk dengan jumlah terjual
- **Fitur:** Horizontal bar chart dengan gradient warna
- **Highlight:** Produk terlaris ditampilkan

### 3. Pie Chart - Distribusi Penjualan

- **Fungsi:** Menampilkan persentase distribusi penjualan
- **Data:** 10 produk dengan persentase kontribusi
- **Fitur:** Donut chart dengan label interaktif
- **Visualisasi:** Warna-warna cerah untuk setiap segment

### 4. Map Visualization - Sebaran Geografis

- **Fungsi:** Menampilkan distribusi penjualan berdasarkan lokasi
- **Data:** 10 kota di Indonesia dengan koordinat
- **Fitur:** Scatter plot di peta dengan ukuran bubble
- **Tambahan:** Tabel detail penjualan per kota

### 5. Area Chart - Kumulatif Penjualan

- **Fungsi:** Menampilkan trend dengan area terisi
- **Data:** 10 bulan dengan jumlah penjualan
- **Fitur:** Filled area chart dengan gradient
- **Analisis:** Bulan tertinggi dan terendah

---

## 💻 Struktur Data

### Data Penjualan (10 items):

```python
{
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset',
               'Webcam', 'Speaker', 'Printer', 'Scanner', 'USB Drive'],
    'Jumlah_Terjual': [45, 120, 85, 60, 95, 40, 55, 30, 25, 150],
    'Harga': [8500000, 150000, 450000, 2500000, 750000,
              800000, 1200000, 3500000, 2800000, 100000],
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt']
}
```

### Data Lokasi (10 items):

```python
{
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang',
             'Makassar', 'Palembang', 'Tangerang', 'Depok', 'Bekasi'],
    'Latitude': [-6.2088, -7.2575, -6.9175, 3.5952, -6.9667,
                 -5.1477, -2.9761, -6.1783, -6.4025, -6.2383],
    'Longitude': [106.8456, 112.7521, 107.6191, 98.6722, 110.4167,
                  119.4322, 104.7754, 106.6319, 106.7942, 106.9756],
    'Penjualan': [450, 320, 280, 190, 240, 210, 175, 380, 350, 390]
}
```

---

## 🎨 Teknologi yang Digunakan

- **Streamlit** - Framework web app
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations
- **PIL (Pillow)** - Image processing untuk header

---

## 🚀 Cara Menjalankan

### Lokal:

```bash
pip install -r requirements.txt
streamlit run Tugas3.py
```

### Deploy:

Lihat file `PANDUAN_DEPLOY.md` untuk instruksi lengkap

---

## 📊 Screenshot Aplikasi

### Tampilan Utama

- Header dengan judul dan deskripsi
- Sidebar dengan dropdown menu
- Info dan tips penggunaan

### Setiap Visualisasi Memiliki:

1. ✅ Gambar header berwarna (berbeda untuk setiap chart)
2. ✅ Title yang descriptive
3. ✅ Deskripsi lengkap tentang fungsi visualisasi
4. ✅ Chart interaktif dengan Plotly
5. ✅ Metrics dan statistik tambahan

---

## 🎓 Nilai Tambah

### UI/UX:

- Responsive layout dengan columns
- Color-coded untuk setiap jenis visualisasi
- Emoji untuk visual appeal
- Warning dan info boxes

### Interaktivity:

- Hover tooltips pada semua chart
- Zoom dan pan pada visualisasi
- Download chart sebagai PNG

### Profesionalitas:

- Code terstruktur dengan baik
- Commenting yang jelas
- Error handling
- Best practices Streamlit

---

## 👨‍💻 Informasi Tugas

**Mata Kuliah:** Administrasi Basis Data  
**Semester:** 5  
**Topik:** Visualisasi Data dengan Streamlit

---

## ✨ Kesimpulan

Aplikasi ini memenuhi **SEMUA** requirement dari tugas:

- ✅ Streamlit framework
- ✅ Dropdown dengan 5 pilihan visualisasi
- ✅ 10 data dummy menggunakan list/dictionary
- ✅ 5 jenis chart (Pie, Bar, Line, Map, Area)
- ✅ **BONUS:** Gambar header untuk setiap visualisasi
- ✅ **BONUS:** Title yang jelas
- ✅ **BONUS:** Deskripsi detail
- ✅ **+10 POIN:** Siap deploy ke Streamlit Cloud

**Total Poin Bonus yang Bisa Didapat:** Maximum! 🎉

---

_Terima kasih! Semoga mendapat nilai terbaik! 🌟_
