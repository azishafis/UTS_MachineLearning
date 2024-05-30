import pandas as pd
import matplotlib.pyplot as plt

# Data
fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

info_mahasiswa = pd.DataFrame({
    "Fakultas": fakultas,
    "Jumlah Mahasiswa": jumlah_mahasiswa,
    "Akreditasi": akreditasi
})

print(info_mahasiswa)

# Memawarnakan Batang
colors = ['lightcoral', 'olive', 'mediumseagreen', 'deepskyblue', 'violet']

# Plot data
plt.figure(figsize=(10, 6))
bars = plt.bar(info_mahasiswa["Fakultas"], info_mahasiswa["Jumlah Mahasiswa"], color=colors)
plt.xlabel('FAKULTAS')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.xticks(size=10)
plt.yticks(size=10)

plt.legend(bars, fakultas, loc='center left', bbox_to_anchor=(1, 0.5))

# Menampilkan plot
plt.show()
