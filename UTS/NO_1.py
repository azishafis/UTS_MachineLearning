import pandas as pd

# Data yang diberikan
data_kampus = {
    'HARI': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'DATANG': [2, 3, 4, 1, 2, 5, 2],
    'BIAYA': [30000*2, 35000*3, 25000*4, 15000*1, 20000*2, 30000*5, 35000*2],
    'MAHASISWA': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']
}

# Membuat DataFrame
df_kampus = pd.DataFrame(data_kampus)

# Menampilkan DataFrame
print("Dataset:")
print(df_kampus)
print("\n")

# a)
rata_rata_datang_minggu = df_kampus['DATANG'].mean()
print("Jawaban NO 1A")
print("Rata-rata mahasiswa datang pada minggu ini: ",rata_rata_datang_minggu,"\n")

# b)
hari_biaya_tertinggi = df_kampus.loc[df_kampus['BIAYA'].idxmax()]['HARI']
print("Jawaban NO 1B")
print("Biaya tertinggi terjadi pada hari: " ,hari_biaya_tertinggi,"\n")

# c)
hari_biaya_diatas_110000 = df_kampus[df_kampus['BIAYA'] > 110000]['HARI'].tolist()
print("Jawaban NO 1C")
print("Hari di mana biaya lebih dari 110000: ",', '.join(hari_biaya_diatas_110000),"\n")

# d)
print("Jawaban NO 1D")
mahasiswa_tersering_datang = df_kampus['MAHASISWA'].value_counts().idxmax()
print("Mahasiswa yang paling banyak datang ke kampus: ",mahasiswa_tersering_datang,"\n")

# e) Siapa yang datang pada hari Minggu?
mahasiswa_datang_minggu = df_kampus[df_kampus['HARI'] == 'Minggu']['MAHASISWA'].tolist()
print("Jawaban NO 1E")
print("Mahasiswa yang datang pada hari Minggu: ",', '.join(mahasiswa_datang_minggu),"\n")

# f) Berapa biaya tertinggi dan terendah?
biaya_paling_tinggi = df_kampus['BIAYA'].max()
biaya_paling_rendah = df_kampus['BIAYA'].min()
print("Jawaban NO 1F")
print("Biaya tertinggi: ",biaya_paling_tinggi)
print("Biaya terendah: ",biaya_paling_rendah,"\n")

# g) Berapa frekuensi datang tertinggi dan terendah?
frekuensi_datang_tertinggi = df_kampus['DATANG'].max()
frekuensi_datang_terendah = df_kampus['DATANG'].min()
print("Jawaban NO 1G")
print("Frekuensi datang tertinggi: ",frekuensi_datang_tertinggi)
print("Frekuensi datang terendah: ",frekuensi_datang_terendah)
