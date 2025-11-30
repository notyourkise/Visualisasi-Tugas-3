import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io
import base64

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Visualisasi Data",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk tema Black & Gold Luxury
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a1a 0%, #0a0a0a 100%);
        border-right: 2px solid #d4af37;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: #d4af37;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #d4af37 !important;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px rgba(212, 175, 55, 0.3);
    }
    
    h1 {
        border-bottom: 3px solid #d4af37;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* Text color */
    p, label, .stMarkdown {
        color: #e8e8e8 !important;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        color: #d4af37 !important;
        font-size: 28px !important;
        font-weight: bold;
    }
    
    [data-testid="stMetricLabel"] {
        color: #c0c0c0 !important;
        font-size: 14px !important;
    }
    
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #d4af37;
        box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background-color: #2a2a2a;
        color: #d4af37;
        border: 2px solid #d4af37;
        border-radius: 8px;
    }
    
    /* Info boxes */
    .stAlert {
        background-color: #2a2a2a;
        color: #e8e8e8;
        border-left: 4px solid #d4af37;
    }
    
    /* Dataframe */
    .dataframe {
        background-color: #1a1a1a;
        color: #e8e8e8;
    }
    
    .dataframe th {
        background-color: #d4af37 !important;
        color: #1a1a1a !important;
        font-weight: bold;
    }
    
    /* Success message */
    .stSuccess {
        background-color: #2a2a2a;
        color: #d4af37;
        border-left: 4px solid #d4af37;
    }
    
    /* Divider */
    hr {
        border-color: #d4af37;
        opacity: 0.5;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #c5a028 100%);
        color: #1a1a1a;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 4px 6px rgba(212, 175, 55, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #e5c047 0%, #d4af37 100%);
        box-shadow: 0 6px 8px rgba(212, 175, 55, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# Header aplikasi dengan styling luxury
st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h1 style='font-size: 48px; margin-bottom: 10px;'>👑 LUXURY DASHBOARD</h1>
    <h2 style='font-size: 24px; color: #c0c0c0; font-weight: 300;'>Premium Data Visualization</h2>
    <p style='color: #888; font-style: italic;'>Tugas Praktikum - Administrasi Basis Data</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='margin: 30px 0; border: 1px solid #d4af37; opacity: 0.3;'>", unsafe_allow_html=True)

# Data dummy untuk visualisasi
data_penjualan = {
    'Produk': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headset', 
               'Webcam', 'Speaker', 'Printer', 'Scanner', 'USB Drive'],
    'Jumlah_Terjual': [45, 120, 85, 60, 95, 40, 55, 30, 25, 150],
    'Harga': [8500000, 150000, 450000, 2500000, 750000, 
              800000, 1200000, 3500000, 2800000, 100000],
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Ags', 'Sep', 'Okt']
}

# Data untuk peta (koordinat kota-kota di Indonesia)
data_lokasi = {
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Semarang', 
             'Makassar', 'Palembang', 'Tangerang', 'Depok', 'Bekasi'],
    'Latitude': [-6.2088, -7.2575, -6.9175, 3.5952, -6.9667, 
                 -5.1477, -2.9761, -6.1783, -6.4025, -6.2383],
    'Longitude': [106.8456, 112.7521, 107.6191, 98.6722, 110.4167, 
                  119.4322, 104.7754, 106.6319, 106.7942, 106.9756],
    'Penjualan': [450, 320, 280, 190, 240, 210, 175, 380, 350, 390]
}

df_penjualan = pd.DataFrame(data_penjualan)
df_lokasi = pd.DataFrame(data_lokasi)

# Sidebar untuk pemilihan visualisasi
st.sidebar.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h2 style='color: #d4af37; font-size: 28px;'>⚙️ Control Panel</h2>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<hr style='border-color: #d4af37; opacity: 0.3;'>", unsafe_allow_html=True)

pilihan_chart = st.sidebar.selectbox(
    "🎨 Pilih Visualisasi:",
    ["📈 Line Chart", "📊 Bar Chart", "🥧 Pie Chart", "🗺️ Map Visualization", "📉 Area Chart"]
)

st.sidebar.markdown("<hr style='border-color: #d4af37; opacity: 0.3;'>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
            padding: 20px; border-radius: 10px; border: 1px solid #d4af37; margin-top: 20px;'>
    <p style='color: #d4af37; font-weight: bold; margin-bottom: 10px;'>💡 Premium Tips</p>
    <p style='color: #c0c0c0; font-size: 14px; line-height: 1.6;'>
    Gunakan dropdown di atas untuk mengeksplorasi berbagai jenis visualisasi data premium.
    Setiap chart dirancang dengan detail untuk memberikan insight terbaik.
    </p>
</div>
""", unsafe_allow_html=True)

# Fungsi untuk membuat gambar placeholder
def create_placeholder_image(text, color1, color2):
    from PIL import Image, ImageDraw, ImageFont
    # Gradient background
    img = Image.new('RGB', (1200, 250), color='black')
    draw = ImageDraw.Draw(img)
    
    # Create gold gradient effect
    for y in range(250):
        ratio = y / 250
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.rectangle([(0, y), (1200, y + 1)], fill=(r, g, b))
    
    # Add decorative border
    draw.rectangle([(0, 0), (1199, 249)], outline=(212, 175, 55), width=3)
    
    try:
        font = ImageFont.truetype("arial.ttf", 50)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = ((1200 - text_width) // 2, (250 - text_height) // 2)
    
    # Text shadow for luxury effect
    shadow_offset = 3
    draw.text((position[0] + shadow_offset, position[1] + shadow_offset), text, fill=(0, 0, 0), font=font)
    draw.text(position, text, fill=(212, 175, 55), font=font)
    
    return img

# Menampilkan visualisasi berdasarkan pilihan
if pilihan_chart == "📈 Line Chart":
    st.markdown("<h2 style='color: #d4af37; text-align: center; font-size: 36px;'>📈 Line Chart - Tren Penjualan Bulanan</h2>", unsafe_allow_html=True)
    
    # Gambar header
    img = create_placeholder_image("PREMIUM LINE CHART VISUALIZATION", (26, 26, 26), (13, 13, 13))
    st.image(img, width='stretch')
    
    # Deskripsi dalam box luxury
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 25px; border-radius: 15px; border: 2px solid #d4af37; 
                margin: 20px 0; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);'>
        <p style='color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px;'>📊 Analisis Premium</p>
        <p style='color: #e8e8e8; line-height: 1.8; font-size: 15px;'>
        Line chart ini menampilkan tren penjualan produk dari bulan ke bulan dengan presisi tinggi. 
        Visualisasi premium ini sangat berguna untuk melihat pola kenaikan atau penurunan 
        penjualan sepanjang waktu dan membantu dalam perencanaan inventory strategis.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Membuat line chart dengan tema gold
    fig = px.line(df_penjualan, 
                  x='Bulan', 
                  y='Jumlah_Terjual',
                  title='<b>Tren Penjualan Premium - Analisis Bulanan</b>',
                  markers=True,
                  labels={'Jumlah_Terjual': 'Jumlah Terjual', 'Bulan': 'Bulan'})
    
    fig.update_traces(
        line_color='#00d4ff', 
        line_width=4, 
        marker=dict(size=12, color='#00d4ff', line=dict(color='#0080ff', width=2))
    )
    
    fig.update_layout(
        height=550,
        hovermode='x unified',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#e8e8e8', size=13),
        title_font=dict(size=22, color='#d4af37'),
        xaxis=dict(
            showgrid=True, 
            gridcolor='#333333',
            color='#d4af37',
            linecolor='#d4af37'
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='#333333',
            color='#d4af37',
            linecolor='#d4af37'
        ),
        hoverlabel=dict(
            bgcolor="#2a2a2a",
            font_size=13,
            font_color="#d4af37"
        )
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Statistik tambahan dengan styling luxury
    st.markdown("<div style='margin: 30px 0;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Total Penjualan", f"{df_penjualan['Jumlah_Terjual'].sum()} unit")
    with col2:
        st.metric("📊 Rata-rata per Bulan", f"{df_penjualan['Jumlah_Terjual'].mean():.0f} unit")
    with col3:
        st.metric("🏆 Penjualan Tertinggi", f"{df_penjualan['Jumlah_Terjual'].max()} unit")
    st.markdown("</div>", unsafe_allow_html=True)

elif pilihan_chart == "📊 Bar Chart":
    st.markdown("<h2 style='color: #d4af37; text-align: center; font-size: 36px;'>📊 Bar Chart - Perbandingan Penjualan Produk</h2>", unsafe_allow_html=True)
    
    # Gambar header
    img = create_placeholder_image("PREMIUM BAR CHART VISUALIZATION", (46, 41, 38), (23, 20, 19))
    st.image(img, width='stretch')
    
    # Deskripsi
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 25px; border-radius: 15px; border: 2px solid #d4af37; 
                margin: 20px 0; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);'>
        <p style='color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px;'>📊 Analisis Premium</p>
        <p style='color: #e8e8e8; line-height: 1.8; font-size: 15px;'>
        Bar chart premium ini menampilkan perbandingan jumlah penjualan antar produk dengan visualisasi eksklusif. 
        Dengan analisis ini, kita dapat dengan mudah mengidentifikasi produk champion dan produk yang 
        memerlukan strategi pemasaran yang lebih agresif.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Membuat bar chart
    df_sorted = df_penjualan.sort_values('Jumlah_Terjual', ascending=True)
    
    fig = px.bar(df_sorted, 
                 x='Jumlah_Terjual', 
                 y='Produk',
                 orientation='h',
                 title='<b>Perbandingan Premium - Top Produk Analysis</b>',
                 labels={'Jumlah_Terjual': 'Jumlah Terjual', 'Produk': 'Nama Produk'})
    
    fig.update_traces(
        marker=dict(
            color=df_sorted['Jumlah_Terjual'],
            colorscale=[[0, '#FF6B6B'], [0.3, '#FFA500'], [0.6, '#FFD700'], [0.8, '#00D4FF'], [1, '#00FF88']],
            line=dict(color='#ffffff', width=1)
        )
    )
    
    fig.update_layout(
        height=600,
        showlegend=False,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#e8e8e8', size=13),
        title_font=dict(size=22, color='#d4af37'),
        xaxis=dict(
            showgrid=True, 
            gridcolor='#333333',
            color='#d4af37',
            linecolor='#d4af37'
        ),
        yaxis=dict(
            showgrid=False,
            color='#d4af37',
            linecolor='#d4af37'
        ),
        hoverlabel=dict(
            bgcolor="#2a2a2a",
            font_size=13,
            font_color="#d4af37"
        )
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Produk terlaris
    top_product = df_penjualan.loc[df_penjualan['Jumlah_Terjual'].idxmax()]
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #d4af37 0%, #c5a028 100%); 
                padding: 20px; border-radius: 10px; margin-top: 20px;
                box-shadow: 0 4px 6px rgba(212, 175, 55, 0.3);'>
        <p style='color: #1a1a1a; font-weight: bold; font-size: 18px; margin: 0;'>
        🏆 <b>Champion Product:</b> {top_product['Produk']} dengan {top_product['Jumlah_Terjual']} unit terjual
        </p>
    </div>
    """, unsafe_allow_html=True)

elif pilihan_chart == "🥧 Pie Chart":
    st.markdown("<h2 style='color: #d4af37; text-align: center; font-size: 36px;'>🥧 Pie Chart - Distribusi Penjualan Produk</h2>", unsafe_allow_html=True)
    
    # Gambar header
    img = create_placeholder_image("PREMIUM PIE CHART VISUALIZATION", (39, 28, 46), (19, 14, 23))
    st.image(img, width='stretch')
    
    # Deskripsi
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 25px; border-radius: 15px; border: 2px solid #d4af37; 
                margin: 20px 0; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);'>
        <p style='color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px;'>📊 Analisis Premium</p>
        <p style='color: #e8e8e8; line-height: 1.8; font-size: 15px;'>
        Pie chart eksklusif ini menunjukkan distribusi persentase penjualan untuk setiap produk dengan detail premium. 
        Visualisasi luxury ini membantu memahami kontribusi relatif setiap produk terhadap 
        total penjualan dan mengidentifikasi produk yang mendominasi market share.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Membuat pie chart dengan tema gold & black
    fig = go.Figure(data=[go.Pie(
        labels=df_penjualan['Produk'],
        values=df_penjualan['Jumlah_Terjual'],
        hole=.5,
        marker=dict(
            colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', 
                    '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#FAD7A0'],
            line=dict(color='#1a1a1a', width=2)
        ),
        textinfo='label+percent',
        textfont=dict(size=13, color='#ffffff', family='Arial Black'),
        textposition='inside',
        hovertemplate='<b>%{label}</b><br>Jumlah: %{value}<br>Persentase: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title='<b>Distribusi Premium - Market Share Analysis</b>',
        height=650,
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#e8e8e8', size=13),
        title_font=dict(size=22, color='#d4af37'),
        showlegend=True,
        legend=dict(
            bgcolor='#2a2a2a',
            bordercolor='#d4af37',
            borderwidth=2,
            font=dict(color='#e8e8e8')
        ),
        hoverlabel=dict(
            bgcolor="#2a2a2a",
            font_size=13,
            font_color="#d4af37"
        )
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Informasi tambahan
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 20px; border-radius: 10px; border: 1px solid #d4af37; margin-top: 20px;'>
        <p style='color: #d4af37; font-weight: bold;'>💡 Premium Insight</p>
        <p style='color: #c0c0c0; font-size: 14px;'>
        Donut chart premium memberikan tampilan yang lebih modern dan eksklusif, 
        memudahkan analisis distribusi dengan visualisasi luxury class.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif pilihan_chart == "🗺️ Map Visualization":
    st.markdown("<h2 style='color: #d4af37; text-align: center; font-size: 36px;'>🗺️ Map - Sebaran Penjualan Geografis</h2>", unsafe_allow_html=True)
    
    # Gambar header
    img = create_placeholder_image("PREMIUM MAP VISUALIZATION", (58, 19, 15), (29, 9, 7))
    st.image(img, width='stretch')
    
    # Deskripsi
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 25px; border-radius: 15px; border: 2px solid #d4af37; 
                margin: 20px 0; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);'>
        <p style='color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px;'>📊 Analisis Premium</p>
        <p style='color: #e8e8e8; line-height: 1.8; font-size: 15px;'>
        Peta eksklusif ini menampilkan distribusi geografis penjualan di berbagai kota premium di Indonesia. 
        Ukuran marker menunjukkan volume penjualan di setiap lokasi strategis, membantu 
        mengidentifikasi wilayah dengan performa penjualan terbaik untuk ekspansi bisnis.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Membuat map visualization dengan tema luxury
    fig = px.scatter_geo(df_lokasi,
                         lat='Latitude',
                         lon='Longitude',
                         size='Penjualan',
                         hover_name='Kota',
                         hover_data={'Latitude': False, 'Longitude': False, 'Penjualan': True},
                         title='<b>Geographical Premium Distribution - Indonesia Market</b>',
                         size_max=50)
    
    fig.update_traces(
        marker=dict(
            color='#00FF88',
            line=dict(color='#00aa55', width=2),
            opacity=0.9
        )
    )
    
    fig.update_geos(
        center=dict(lat=-2.5, lon=118),
        projection_scale=4,
        showcountries=True,
        showcoastlines=True,
        showland=True,
        landcolor='#2a2a2a',
        coastlinecolor='#d4af37',
        countrycolor='#d4af37',
        bgcolor='#1a1a1a',
        oceancolor='#0d0d0d'
    )
    
    fig.update_layout(
        height=650,
        geo=dict(bgcolor='#1a1a1a'),
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#e8e8e8', size=13),
        title_font=dict(size=22, color='#d4af37'),
        hoverlabel=dict(
            bgcolor="#2a2a2a",
            font_size=13,
            font_color="#d4af37"
        )
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Tabel data lokasi dengan styling HTML custom
    st.markdown("<h3 style='color: #d4af37; margin-top: 30px;'>📋 Data Detail Premium - Penjualan per Kota</h3>", unsafe_allow_html=True)
    
    # Buat HTML table custom
    df_sorted = df_lokasi.sort_values('Penjualan', ascending=False)
    
    table_html = """
    <div style='overflow-x: auto;'>
        <table style='width: 100%; border-collapse: collapse; background: #1a1a1a; border: 2px solid #d4af37; border-radius: 10px;'>
            <thead>
                <tr style='background: linear-gradient(135deg, #d4af37 0%, #c5a028 100%);'>
                    <th style='padding: 15px; text-align: left; color: #1a1a1a; font-weight: bold; border: 1px solid #d4af37;'>No</th>
                    <th style='padding: 15px; text-align: left; color: #1a1a1a; font-weight: bold; border: 1px solid #d4af37;'>Kota</th>
                    <th style='padding: 15px; text-align: center; color: #1a1a1a; font-weight: bold; border: 1px solid #d4af37;'>Latitude</th>
                    <th style='padding: 15px; text-align: center; color: #1a1a1a; font-weight: bold; border: 1px solid #d4af37;'>Longitude</th>
                    <th style='padding: 15px; text-align: center; color: #1a1a1a; font-weight: bold; border: 1px solid #d4af37;'>Penjualan (unit)</th>
                </tr>
            </thead>
            <tbody>
    """
    
    no = 1
    for idx, row in df_sorted.iterrows():
        table_html += f"""
                <tr style='border-bottom: 1px solid #333;'>
                    <td style='padding: 12px; color: #e8e8e8; border: 1px solid #333;'>{no}</td>
                    <td style='padding: 12px; color: #d4af37; font-weight: bold; border: 1px solid #333;'>{row['Kota']}</td>
                    <td style='padding: 12px; color: #c0c0c0; text-align: center; border: 1px solid #333;'>{row['Latitude']:.4f}</td>
                    <td style='padding: 12px; color: #c0c0c0; text-align: center; border: 1px solid #333;'>{row['Longitude']:.4f}</td>
                    <td style='padding: 12px; color: #00FF88; font-weight: bold; text-align: center; border: 1px solid #333;'>{row['Penjualan']}</td>
                </tr>
        """
        no += 1
    
    table_html += """
            </tbody>
        </table>
    </div>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)

elif pilihan_chart == "📉 Area Chart":
    st.markdown("<h2 style='color: #d4af37; text-align: center; font-size: 36px;'>📉 Area Chart - Kumulatif Penjualan Premium</h2>", unsafe_allow_html=True)
    
    # Gambar header
    img = create_placeholder_image("PREMIUM AREA CHART VISUALIZATION", (58, 32, 9), (29, 16, 4))
    st.image(img, width='stretch')
    
    # Deskripsi
    st.markdown("""
    <div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
                padding: 25px; border-radius: 15px; border: 2px solid #d4af37; 
                margin: 20px 0; box-shadow: 0 4px 6px rgba(212, 175, 55, 0.2);'>
        <p style='color: #d4af37; font-weight: bold; font-size: 18px; margin-bottom: 10px;'>📊 Analisis Premium</p>
        <p style='color: #e8e8e8; line-height: 1.8; font-size: 15px;'>
        Area chart premium ini menampilkan tren kumulatif penjualan produk dengan visualisasi eksklusif. 
        Area yang terisi memberikan representasi visual luxury yang jelas tentang 
        volume penjualan dan memudahkan perbandingan antara periode waktu berbeda dengan presisi tinggi.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Membuat area chart dengan tema gold
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_penjualan['Bulan'],
        y=df_penjualan['Jumlah_Terjual'],
        fill='tozeroy',
        name='Penjualan Premium',
        line=dict(color='#FF6EC7', width=3),
        fillcolor='rgba(255, 110, 199, 0.4)',
        mode='lines+markers',
        marker=dict(size=10, color='#FF6EC7', line=dict(color='#C724B1', width=2)),
        hovertemplate='<b>%{x}</b><br>Penjualan: %{y} unit<extra></extra>'
    ))
    
    fig.update_layout(
        title='<b>Area Chart Premium - Analisis Kumulatif Penjualan</b>',
        xaxis_title='<b>Bulan</b>',
        yaxis_title='<b>Jumlah Terjual</b>',
        height=550,
        hovermode='x unified',
        plot_bgcolor='#1a1a1a',
        paper_bgcolor='#1a1a1a',
        font=dict(color='#e8e8e8', size=13),
        title_font=dict(size=22, color='#d4af37'),
        xaxis=dict(
            showgrid=True, 
            gridcolor='#333333',
            color='#d4af37',
            linecolor='#d4af37'
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='#333333',
            color='#d4af37',
            linecolor='#d4af37'
        ),
        hoverlabel=dict(
            bgcolor="#2a2a2a",
            font_size=13,
            font_color="#d4af37"
        )
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # Analisis tren dengan luxury styling
    st.markdown("<div style='margin: 30px 0;'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🏆 Bulan Tertinggi", df_penjualan.loc[df_penjualan['Jumlah_Terjual'].idxmax(), 'Bulan'])
    with col2:
        st.metric("📉 Bulan Terendah", df_penjualan.loc[df_penjualan['Jumlah_Terjual'].idxmin(), 'Bulan'])
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr style='margin: 50px 0; border: 1px solid #d4af37; opacity: 0.3;'>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 30px 0; background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%); 
            border-radius: 15px; border: 2px solid #d4af37; margin: 20px 0;'>
    <p style='color: #d4af37; font-size: 24px; font-weight: bold; margin-bottom: 10px;'>👑 LUXURY DASHBOARD</p>
    <p style='color: #c0c0c0; font-size: 16px; margin-bottom: 5px;'>Dibuat dengan ❤️ & ✨ menggunakan Streamlit Premium</p>
    <p style='color: #888; font-size: 14px; font-style: italic;'>Data premium untuk keperluan demonstrasi eksklusif</p>
    <p style='color: #d4af37; font-size: 12px; margin-top: 15px;'>© 2025 Premium Data Visualization | Black & Gold Edition</p>
</div>
""", unsafe_allow_html=True)

# Informasi deployment di sidebar
st.sidebar.markdown("<hr style='border-color: #d4af37; opacity: 0.3; margin: 30px 0;'>", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style='background: linear-gradient(135deg, #2a2a2a 0%, #1a1a1a 100%); 
            padding: 20px; border-radius: 10px; border: 1px solid #d4af37;'>
    <p style='color: #d4af37; font-weight: bold; font-size: 16px; margin-bottom: 10px;'>🚀 Premium Deployment</p>
    <p style='color: #c0c0c0; font-size: 13px; line-height: 1.6;'>
    <b>Cara Deploy ke Streamlit Cloud:</b><br>
    1. Push code ke GitHub<br>
    2. Buka <a href='https://share.streamlit.io' style='color: #d4af37;'>share.streamlit.io</a><br>
    3. Login dengan GitHub<br>
    4. Deploy aplikasi premium ini<br>
    5. Dapatkan link public eksklusif!
    </p>
</div>
""", unsafe_allow_html=True)
