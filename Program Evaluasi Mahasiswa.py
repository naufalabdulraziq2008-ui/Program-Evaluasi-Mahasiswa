# 1. Input nilai mahasiswa
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

# 2. Menghitung nilai akhir
nilai_akhir = (20 / 100 * tugas) + (30 / 100 * uts) + (50 / 100 * uas)

# 3. Menampilkan nilai akhir
print("\n===== HASIL EVALUASI MAHASISWA =====")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Kehadiran   : {kehadiran:.2f}%")

# 4. Menentukan status kelulusan
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status      : LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status      : LULUS")
else:
    print("Status      : BELUM LULUS")