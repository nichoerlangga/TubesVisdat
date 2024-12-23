# -*- coding: utf-8 -*-
"""Final Project Full Version.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CqAtL0e8yvR3QiJIICDJFu5k8y-CbVCS
"""

!pip install streamlit
!pip install pyngrok

# Commented out IPython magic to ensure Python compatibility.
# %%writefile main.py
# import streamlit as st
# import pandas as pd
# from unitSold import UnitSold
# from topSelling import TopSelling
# from mostCategory import MostCategory
# from revenue import Revenue
# from payment import Payment
# 
# # Fungsi untuk masing-masing halaman
# def home_page():
#     file_path = 'https://github.com/AlfiessaWidya/Dataset_Visual_Data/blob/master/bg.png?raw=true'
#     st.image(file_path)
#     st.title("Online Sales Data Analysis")
#     st.write("""
#         Data ini berisi informasi penjualan online yang mencakup kategori produk,
#         kuantitas, harga, wilayah, dan metode pembayaran. Visualisasi yang digunakan
#         mencakup tren total pendapatan dari waktu ke waktu, kategori produk terbanyak
#         terjual, 10 produk terlaris, dan distribusi produk yang terjual di setiap wilayah.
#         Data ini penting karena memungkinkan bisnis untuk memahami performa penjualan mereka,
#         mengidentifikasi produk yang paling menguntungkan, mengevaluasi preferensi pelanggan di
#         berbagai wilayah, dan mengoptimalkan strategi pemasaran serta pengelolaan stok. Dengan
#         demikian, perusahaan dapat membuat keputusan yang lebih informasi-dasar untuk meningkatkan
#         penjualan dan efisiensi operasional.
#     """)
# 
#     # Membaca data dari file CSV
#     data_url = "https://drive.google.com/uc?id=" + '1vhsQTLZmrJG-ADOx3T8NYL4JBDJQY5Qg'  # Ganti dengan path ke file data Anda
#     data = pd.read_csv(data_url)
# 
#     # Menampilkan data raw
#     st.subheader("Raw Data")
#     st.dataframe(data)  # Atau gunakan st.table(data) untuk tampilan tabel statis
# 
#     # Menampilkan daftar nama
#     st.subheader("Daftar Nama Kelompok")
#     nama_list = ["1301213146 | Brithany Zhafira Nurranty", "1301210499 | Elvira Wulandari", "1301213412 | Karina Diva Aulia Igani", "1301213275	| Alfiessa Widya Wirawan", "1301210511 | Muhammad Rivaditya Azzaka"]
#     for nama in nama_list:
#         st.markdown(nama)
# 
# def unit_solds_page():
#     st.title("Units Sold")
#     UnitSold.show()
# 
# def top_selling_page():
#     st.title("Top 10 Selling Products")
#     st.write("Showing top 10 selling products")
#     TopSelling.show()
# 
# def most_category_page():
#     st.title("The Most Sold Product Category")
#     MostCategory.show()
# 
# def revenue_page():
#     Revenue.show()
# 
# def payment_page():
#     st.title("Most Popular Payment Method")
#     Payment.show()
# 
# # Membuat sidebar
# st.sidebar.title("Menu")
# select = st.sidebar.radio("Select Category", (
#   "Home",
#   "Units Sold",
#   "Top Selling",
#   "Most Category",
#   "Revenue",
#   "Payment"
#   ))
# 
# # Menampilkan halaman berdasarkan pilihan
# if select == "Home":
#     home_page()
# elif select == "Units Sold":
#     unit_solds_page()
# elif select == "Top Selling":
#     top_selling_page()
# elif select == "Most Category":
#   most_category_page()
# elif select == "Revenue":
#   revenue_page()
# elif select == "Payment":
#   payment_page()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile unitSold.py
# import warnings
# import numpy as np
# import pandas as pd
# import streamlit as st
# import altair as alt
# from urllib.error import URLError
# 
# class UnitSold:
#     @staticmethod
#     def show():
#       st.write("Showing the sold units in each region")
# 
#       def get_UN_data():
#           data_url = 'https://raw.githubusercontent.com/AlfiessaWidya/Dataset_Visual_Data/master/sales_data.csv'
#           df = pd.read_csv(data_url)
#           return df
# 
#       try:
#           df = get_UN_data()
# 
#           # Drop rows where 'Region' is NaN
#           df = df.dropna(subset=['Region'])
# 
#           # Set 'Region' as index
#           df = df.set_index("Region")
# 
#           # Get unique regions for multiselect options
#           unique_regions = df.index.unique().tolist()
# 
#           # Provide a default selection if 'Asia' and 'Europe' exist in the data
#           default_selection = unique_regions
# 
#           countries = st.multiselect(
#               "Choose countries", unique_regions, default_selection
#           )
#           if not countries:
#               st.error("Please select at least one country.")
#           else:
#               data = df.loc[countries]
# 
#               # Convert relevant columns to numeric, coercing errors to NaN
#               data['Units Sold'] = pd.to_numeric(data['Units Sold'], errors='coerce')
# 
#               # Fill NaN values with 0 in Units Sold column (or handle them as appropriate)
#               data['Units Sold'] = data['Units Sold'].fillna(0)
# 
#               st.write("### Units Sold (in millions)", data.sort_index())
# 
#               # Prepare data for Altair visualization
#               melted_data = pd.melt(
#                   data.reset_index(),
#                   id_vars=["Region", "Date", "Product Category", "Product Name", "Payment Method"],
#                   value_vars=["Units Sold"],
#                   var_name="Metric",
#                   value_name="Value"
#               )
# 
#               chart = (
#                   alt.Chart(melted_data)
#                   .mark_area(opacity=0.3)
#                   .encode(
#                       x="Product Name:N",
#                       y=alt.Y("Value:Q", stack=None),
#                       color="Region:N",
#                       tooltip=["Date", "Product Category", "Product Name", "Value", "Payment Method"]
#                   )
#               )
#               st.altair_chart(chart, use_container_width=True)
# 
# 
#       except URLError as e:
#           st.error(
#               """ *This demo requires internet access.* Connection error: %s """
#               % e.reason )
# 
# 
#       st.title("Jenis Visualisasi: Area Chart")
#       st.write("""Bagan ini menunjukkan unit terjual untuk berbagai produk di berbagai wilayah. Sebagai bagan area, ini memperlihatkan total penjualan per produk (area di bawah garis),
#       bukan penjualan individual per wilayah. Sumbu X menunjukkan nama produk, sumbu Y menunjukkan jumlah total unit terjual (nilai bertumpuk),
#       dan garis berwarna menunjukkan wilayah berbeda (misalnya Asia, Eropa, Amerika Utara).
#       Area di bawah setiap garis menunjukkan total unit terjual di wilayah tersebut untuk setiap produk..""")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile topSelling.py
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# # Top 10 Selling Products
# # bentuk scatter
# # Fungsi untuk memuat data dari Google Drive
# 
# class TopSelling:
#     @staticmethod
#     def show():
# 
#       @st.cache_data
#       def get_UN_data():
#           data = "https://drive.google.com/uc?id=" + '1vhsQTLZmrJG-ADOx3T8NYL4JBDJQY5Qg'
#           df = pd.read_csv(data)
#           df['Date'] = pd.to_datetime(df['Date'])
#           return df
# 
#       # Memuat data
#       df = get_UN_data()
# 
#       # Mengelompokkan data berdasarkan nama produk dan menjumlahkan total pendapatan
#       top_selling_products = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(10).reset_index()
# 
#       # Membuat grafik scatter plot dengan Plotly
#       scatter_plot = px.scatter(top_selling_products, x='Product Name', y='Total Revenue',
#                                 size='Total Revenue', color='Product Name',
#                                 hover_name='Product Name', log_y=True, size_max=60)
# 
#       scatter_plot.update_layout(
#           title='',
#           xaxis_title='Product Name',
#           yaxis_title='Total Revenue',
#           xaxis=dict(tickangle=-45),
#           title_x=0.5,
#           height=600,
#           width=800
#       )
# 
#       # Menambahkan fitur zoom dan panning
#       scatter_plot.update_layout(
#           dragmode='zoom',
#           hovermode='closest'
#       )
# 
#       # Menampilkan grafik di Streamlit
#       st.plotly_chart(scatter_plot, use_container_width=True)
# 
#       st.title("Jenis Visualisasi: Scatter Plot")
#       st.write("""Digunakan untuk memvisualisasikan hubungan antara dua variabel numerik.
#       Setiap titik data direpresentasikan oleh titik pada grafik.
#       Posisi titik pada sumbu X dan Y menunjukkan nilai kedua variabel untuk titik data tersebut.""")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile revenue.py
# import pandas as pd
# import streamlit as st
# import altair as alt
# import calendar
# # tren total  pendapatan dari waktu  ke waktu
# # Fungsi untuk memuat data dari Google Drive
# 
# class Revenue:
#     @staticmethod
#     def show():
# 
#       @st.cache_data
#       def get_UN_data():
#           data = "https://drive.google.com/uc?id=" + '1vhsQTLZmrJG-ADOx3T8NYL4JBDJQY5Qg'
#           df = pd.read_csv(data)
#           df['Date'] = pd.to_datetime(df['Date'])
#           return df
# 
#       # Memuat data
#       df = get_UN_data()
# 
#       # Ekstraksi nama bulan dan tahun dari kolom Date
#       df['Month'] = df['Date'].dt.month_name()
#       df['Year'] = df['Date'].dt.year
# 
#       # Sidebar untuk memilih tahun
#       selected_year = 2024
# 
#       # Filter data berdasarkan tahun yang dipilih
#       filtered_df = df[df['Year'] == selected_year]
# 
#       # Menampilkan judul
#       st.title(f'Revenue Over Time for {selected_year}')
# 
#       # Membuat grafik garis dengan Altair
#       line_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
#           x=alt.X('Month', sort=list(calendar.month_name)[1:]),  # Memastikan bulan diurutkan dengan benar
#           y='Total Revenue',
#           tooltip=['Month', 'Total Revenue']
#       ).properties(
#           title='Showing revenue over time',
#           width=800,
#           height=400
#       ).configure_axis(
#           labelAngle=45
#       )
# 
#       # Menampilkan grafik di Streamlit
#       st.altair_chart(line_chart, use_container_width=True)
# 
# 
#       st.title("Jenis Visualisasi: Line Chart")
#       st.write("""Grafik garis digunakan untuk memvisualisasikan tren data dari waktu ke waktu.
#       Setiap titik data direpresentasikan oleh titik pada grafik, dan titik-titik tersebut dihubungkan dengan garis.
#       Posisi titik pada sumbu X menunjukkan waktu, dan posisi titik pada sumbu Y menunjukkan nilai data.
#       Dalam kasus ini, sumbu X menunjukkan bulan, dan sumbu Y menunjukkan total pendapatan.""")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile payment.py
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# 
# class Payment:
#     @staticmethod
#     def show():
# 
#         @st.cache_data
#         def get_data():
#             # URL to the Google Drive file
#             data = "https://drive.google.com/uc?id=" + '1vhsQTLZmrJG-ADOx3T8NYL4JBDJQY5Qg'
#             # Reading the CSV data
#             df = pd.read_csv(data)
#             return df
# 
#         # Loading the data
#         df = get_data()
# 
#         # Counting the number of transactions per Payment Method
#         payment_methods = df['Payment Method'].value_counts().reset_index(name='Count').rename(columns={'index': 'Payment Method'})
# 
#         # Printing the dataframe (for debugging purposes, can be removed)
#         print(payment_methods)
# 
#         # Creating a bar chart with Plotly
#         fig = px.bar(payment_methods, x='Payment Method', y='Count',
#                      title='Showing most popular payment methods used by customers',
#                      color='Payment Method',
#                      labels={'Count': 'Number of Transactions'})
# 
#         # Displaying the chart in Streamlit
#         st.plotly_chart(fig, use_container_width=True)
# 
#         st.title("Jenis Visualisasi: Bar Chart")
#         st.write("""Menunjukkan metode pembayaran yang paling populer digunakan oleh pelanggan. Sumbu X menunjukkan berbagai metode pembayaran (Kartu Kredit, Kartu Debit, PayPal).
#         Sumbu Y menunjukkan jumlah transaksi untuk setiap metode pembayaran. Setiap metode pembayaran di sumbu X memiliki batang yang sesuai di sumbu Y.
#         Panjang batang menunjukkan jumlah transaksi untuk metode pembayaran tersebut.""")

# Commented out IPython magic to ensure Python compatibility.
# %%writefile mostCategory.py
# import pandas as pd
# import streamlit as st
# import plotly.express as px
# # pie
# # Kategori produk terbanyak
# # Fungsi untuk memuat data dari Google Drive
# 
# class MostCategory:
#     @staticmethod
#     def show():
# 
#       @st.cache_data
#       def get_UN_data():
#           data = "https://drive.google.com/uc?id=" + '1vhsQTLZmrJG-ADOx3T8NYL4JBDJQY5Qg'
#           df = pd.read_csv(data)
#           df['Date'] = pd.to_datetime(df['Date'])
#           return df
# 
#       # Memuat data
#       df = get_UN_data()
# 
#       # Mengelompokkan data berdasarkan kategori produk dan menjumlahkan total unit yang terjual
#       p_category = df.groupby('Product Category')['Units Sold'].sum().reset_index()
# 
#       # Membuat grafik pie dengan plotly
#       fig = px.pie(p_category, names='Product Category', values='Units Sold',
#                    title='Showing the most sold product by category',
#                    color_discrete_sequence=["olive", "orange", "pink", "salmon", "yellow", "gray"],
#                    hole=0.3)
# 
#       # Menambahkan keterangan presentase
#       fig.update_traces(textinfo='percent+label')
# 
#       # Menampilkan grafik di Streamlit
#       st.plotly_chart(fig, use_container_width=True)
# 
#       st.title("Jenis Visualisasi: Pie Chart")
#       st.write("""Menunjukkan proporsi atau persentase data dalam suatu kategori.
#       Dalam hal ini, grafik pie menunjukkan proporsi penjualan produk berdasarkan kategori produk.""")

!npm install localtunnel

!streamlit run main.py &>/content/logs.txt &

!wget -q -O - https://loca.lt/mytunnelpassword

!streamlit run main.py & npx localtunnel --port 8501